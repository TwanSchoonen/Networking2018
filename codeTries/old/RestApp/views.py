from database import db
from user import User
from authorization import auth, super

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

@people.route('/data', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}

@people.route('/data', methods=['GET'])
@auth.login_required
def get_user():
    return jsonify({'username': g.user.username})

@people.route('/dataall', methods=['GET'])
@super.login_required
def get_all_users():
    return jsonify({'data': '%s' % User.query.all()})
    
@people.route('/data', methods=['DELETE'])
@auth.login_required
def delete_user():
    user = User.query.filter_by(username=g.user.username).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True}), 201

@people.route('/dataall', methods=['DELETE'])
@super.login_required
def delete_all_users():
    users = User.query.all()
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True}), 201

@people.route('/data', methods=['PUT'])
@auth.login_required
def put_user():
    user = User.query.filter_by(username=g.user.username).first()
    if not request.json:
        abort(400)
    # if 'username' in request.json and type(request.json['username']) != unicode:
    #     abort(400)

    username = request.json.get('username')
    password = request.json.get('password')

    user.username = request.json.get('username')
    user.password_hash = password_hash(password)

    db.session.commit()
    return jsonify({'user' : user.username})

