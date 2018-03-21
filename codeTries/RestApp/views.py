from database import db
from user import User
from authorization import auth

import os
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from flask.blueprints import Blueprint

people = Blueprint('people', __name__,
                 template_folder='templates',
                 static_folder='static')
 
# Basic error handling
@people.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@people.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@people.route('/')
def home_user_amount():
    return "Amount of users: %s" % len(User.query.all())

@people.route('/data', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username = username)
    user.hash_password(password) 
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('people.new_user',
                                 id=user.id, _external=True)})

@people.route('/data', methods=['GET'])
@auth.login_required
def get_user():
    return jsonify({'data': 'Hello, %s!' % g.user.username})

@people.route('/dataall', methods=['GET'])
@auth.login_required
def get_all_users():
    return jsonify({'data': '%s' % User.query.all()})
    
@people.route('/data', methods=['DELETE'])
@auth.login_required
def delete_user():
    user = User.query.filter_by(username=g.user.username).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})

@people.route('/dataall', methods=['DELETE'])
@auth.login_required
def delete_all_users():
    users = User.query.all()
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})

# #not done yet
# @mod.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'description' in request.json and type(request.json['description']) is not unicode:
#         abort(400)
#     if 'done' in request.json and type(request.json['done']) is not bool:
#         abort(400)
#     task[0]['title'] = request.json.get('title', task[0]['title'])
#     task[0]['description'] = request.json.get('description', task[0]['description'])
#     task[0]['done'] = request.json.get('done', task[0]['done'])
#     return jsonify({'task': task[0]})

