from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user, user_accessed
from .models import Post
from . import db

view = Blueprint('view', __name__)


@view.route('/')
@view.route('/home')
@login_required
def home():
    posts = Post.query.all()
    return render_template('home.html', user=current_user, posts=posts)


@view.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        if not text:
            flash("Post cannot be empty", category="error")
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("posted create!", category="success")
            return redirect(url_for('view.home'))
    return render_template('create_post.html', user=current_user)


@view.route('/delete-post/<id:int>')
@login_required
def delete_post():
    