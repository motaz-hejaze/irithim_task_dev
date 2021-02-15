from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////irithim.db'
db = SQLAlchemy(app)

class User(db.Model):
    USER_TYPES = (
        'Admin',
        'Member'
    )
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    user_type = db.Column(db.String(10), choicess=USER_TYPES, nullable=False)

    def __repr__(self):
        return self.username


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    assigned_member = db.Column(db.)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    list_id = db.Column()
    main_comments_count = db.Column(db.Integer())

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer)
    content = db.Column(db.Text())
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)
    replies = db.






