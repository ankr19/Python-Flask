from flask import Blueprint, render_template, request, url_for, redirect, flash
from . import db
from .models import User
from flask_login import  login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged In", category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.home'))
            else:
                flash("Creditial is wrong", category='error')
        else:
            flash("Creditial is wrong",category='error')

    return render_template('login.html',user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        epassword = request.form.get('epassword')
        
        email_exist = User.query.filter_by(email=email).first()
        username_exist = User.query.filter_by(username=username).first()
        
        if email_exist:
            flash("Email is already is in use", category="error")
        elif username_exist:
            flash("Username is already in use", category='error')
        elif password!=epassword:
            flash('Password don\'t match', category='error')
        elif len(username) < 2:
            flash("User name is short", category='error')
        elif len(password) < 6:
            flash("Password is short", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User Created')
            return redirect(url_for('view.home'))

    return render_template('signup.html',user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.home'))
