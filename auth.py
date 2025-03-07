from flask import Blueprint, render_template,request, flash, redirect, url_for
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login successful!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password incorrect, try again!', category='error')

        else:
            flash('Email does not exist!', category='error')
    
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists!', category='error')
        elif len(username) < 4:
            flash('Username must be greater than 4 characters!', category='error')
        elif password1 != password2:
            flash('Passwords do not match!', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters!', category='error')
        else: 
            # add user to database
            new_user = User(username=username,email=email,password=generate_password_hash(password1))

            db.session.add(new_user)

            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('auth.login'))

    return render_template('signup.html', user=current_user)