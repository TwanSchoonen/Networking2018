#!flask/bin/python
from flask import Flask, make_response, jsonify

app = Flask(__name__)

#app.debug = True

# Basic error handling
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# The view shows everything
from users.view import mod
app.register_blueprint(mod)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
