from database import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    birth_date = db.Column(db.String(10))
    street_name = db.Column(db.String(32))
    house_number = db.Column(db.String(32))
    city = db.Column(db.String(32))
    balance = db.Column(db.Float)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '<User %r>' % self.username




