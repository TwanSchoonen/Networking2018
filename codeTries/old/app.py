#!flask/bin/python
import os, json
from flask import Flask, jsonify, make_response, abort, request, url_for

USERS = []
USERID = 0
USERSFOLDER = '../testUsers/'

auth = HTTPBasicAuth()

def populate_users():
    json_files = [pos_json for pos_json in os.listdir(USERSFOLDER) if pos_json.endswith('.json')]
    global USERID
    USERID = len(json_files)

    for user in json_files:
        with open(USERSFOLDER + user) as json_data:
            d = json.load(json_data)
            USERS.append(d)
 
def write_user_file(user): 
    with open(USERSFOLDER + 'usr' + user['usrId'] + '.json', 'w') as outfile:
        json.dump(user, outfile)
 
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None
 
@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
 
@app.route('/users/<string:user_id>', methods=['GET'])
def get_task(user_id):
    user = [user for user in USERS if user['usrId'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route('/users', methods=['GET'])
def get_tasks():
    return jsonify({'users': USERS}) 
    
@app.route('/users', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    global USERID
    USERID = USERID + 1
    user_id_str = str(USERID)
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
    write_user_file(user)
    
    USERS.append(user)
    return jsonify({'user': user}), 201


app = Flask(__name__.split('.')[0])

if __name__ == '__main__':
    app.run(debug = True)
    populate_users()
    user = data.UserData("dir")
    print(user.name)
