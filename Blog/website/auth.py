from django.shortcuts import redirect
from flask import Blueprint,render_template, request, url_for

auth =  Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    username = request.form.get('username');
    print(username)
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('view.home'))