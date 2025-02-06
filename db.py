from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME = 'database.db'  # Move DB_NAME here

db = SQLAlchemy()

def db_init(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_database(app):
    if not path.exists(DB_NAME):  # No need for 'website/' prefix
        with app.app_context():
            db.create_all()
        print('Created Database!')
