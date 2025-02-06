from flask import Flask, request, render_template, Response
from flask_login import LoginManager
from werkzeug.utils import secure_filename
from models import User, Note
from db import db, create_database, db_init

DB_NAME = 'database.db'

# Blueprints should be imported after initializing the app
from views import views
from auth import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jhkgfdjsaegfkesdyfh637'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQL_TRACK_MODIFICATIONS'] = False

db_init(app)  # Initialize the database
create_database(app)  # Create the database if not exists

# Initialize login manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Register blueprints
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
