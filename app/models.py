from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

## User Class Inherits required methods from UserMixin
## db.Model creates tables
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    trips = db.relationship('Trip', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tripname = db.Column(db.String(64), index=True)
    destination = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    friend_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Trip {}>'.format(self.tripname)

## Flask login ##
@login.user_loader
def load_user(id):
    """ creates User object """
    return User.query.get(int(id))
