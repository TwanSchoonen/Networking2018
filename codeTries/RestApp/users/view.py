from .userdata import UserData
from flask import Blueprint, jsonify, make_response, request, abort

mod = Blueprint('users', __name__)

users = UserData("testUsers/")


@mod.route('/')
def home():
    return 'Current amount of users in the databass: ' + str(users.userID) 

@mod.route('/data', methods=['GET'])
def get_tasks():
    return jsonify({'users': users.userList}) 

@mod.route('/data/<string:firstName>', methods=['GET'])
def get_task(firstName):
    user = [user for user in users.userList
            if user['firstName'] == firstName]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})


@mod.route('/data', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)  
    users.userID += 1
    user_id_str = str(users.userID)
    user = {
        "balance": "100", 
        "bankNumber": "JC44-5356-4200", 
        "dateOfRegister": "13/3/2018", 
        "firstName": "Johnny", 
        "lastLogin": "14/3/2018", 
        "lastName": "Cage", 
        "telephone": '0642345614',
        'usrId': user_id_str,
    }
    users.write_user_file(user)
    users.userList.append(user)
    return jsonify({'user': user}), 201

#not done yet
@mod.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

#not done yet
@mod.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
