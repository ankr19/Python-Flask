from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user, user_accessed
from .models import Post, User
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


@view.route('/delete-post/<int:id>')
@login_required
def delete_post(id):
    id = int(id)
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash('Post does not exist.', category="error")
    elif current_user.id != post.author:
        flash('you do not have authorized to delete this post', category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='success')
    return redirect(url_for('view.home'))

@view.route('/update-post/<int:id>')
@login_required
def update_post(id):
    id = int(id)
    post = Post.query.filter_by(id=id).first()
    db.session.add(post)
    db.session.commit()
    flash('Post Updated', category='success')
    return render_template('update.html',post=post)


@view.route('/posts/<string:username>')
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('No user with username exists', category='error')
        return redirect(url_for('view.home'))

    posts = Post.query.filter_by(author=user.id).all()
    return render_template('post.html', user=current_user,posts=posts, username=user.username)
