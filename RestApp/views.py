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
    user_name = request.json.get('username')
    first_name = request.json.get('firstname')
    last_name = request.json.get('lastname')
    birth_date = request.json.get('birthdate')
    street_name = request.json.get('streetname')
    house_number = request.json.get('housenumber')
    city = request.json.get('city')
    balance = request.json.get('balance')
    password = request.json.get('password')
    
    if user_name is None or password is None or first_name is None or last_name is None or birth_date is None or street_name is None or house_number is None or city is None or balance is None:
        abort(400) # missing arguments
    if User.query.filter_by(user_name = user_name).first() is not None:
        abort(400) # existing user
    user = User(user_name = user_name)
    user.first_name = first_name
    user.last_name = last_name
    user.birth_date = birth_date
    user.street_name = street_name
    user.house_number = house_number
    user.city = city
    user.balance = balance
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.user_name, 'firstname': user.first_name, 'lastname': user.last_name,
                    'birthdate': user.birth_date, 'streetname': user.street_name, 'housenumber': user.house_number,
                    'city': user.city, 'balance': user.balance}), 201

@people.route('/data', methods=['GET'])
@auth.login_required
def get_user():
    return jsonify({'username': g.user.user_name, 'firstname': g.user.first_name, 'lastname': g.user.last_name,
                    'birthdate': g.user.birth_date, 'streetname': g.user.street_name, 'housenumber': g.user.house_number,
                    'city': g.user.city, 'balance': g.user.balance})


@people.route('/dataall', methods=['GET'])
@super.login_required
def get_all_users():
    return jsonify({'data': '%s' % User.query.all()})
    
@people.route('/data', methods=['DELETE'])
@auth.login_required
def delete_user():
    user = User.query.filter_by(user_name=g.user.user_name).first()
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
    user = User.query.filter_by(user_name=g.user.user_name).first()
    if not request.json:
        abort(400)
    # if 'username' in request.json and type(request.json['username']) != unicode:
    #     abort(400)
    
    user.user_name = request.json.get('username')
    user.hash_password(request.json.get('password'))

    db.session.commit()
    return jsonify({'user' : user.user_name}), 201

