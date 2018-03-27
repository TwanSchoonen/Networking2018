#!/usr/bin/env python
from database import db
from flask import Flask
import os.path
from views import people

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)    
    app.register_blueprint(people, url_prefix='')
    return app;

def setup_database(app):
    with app.app_context():
        db.create_all()
    

if __name__ == '__main__':
    app = create_app()
    # Check if there already is a database file
    if not os.path.exists('db.sqlite'):
        setup_database(app)
    app.run()
    #app.run(host='0.0.0.0')
