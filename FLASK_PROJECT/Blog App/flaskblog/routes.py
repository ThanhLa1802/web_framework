from flask.globals import request
from flask_wtf import form
from flaskblog.models import User, Post
from flask import Flask, render_template, flash, url_for, abort
from werkzeug.utils import redirect
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskblog import app
from flaskblog import db
from flaskblog import bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import os 
import secrets
from PIL import Image
from flask_dance.contrib.github import make_github_blueprint, github

#decorator
@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts  = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")
@app.route("/register", methods = ["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(user_name = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been create!', 'success' )
        return redirect(url_for('login'))
        
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #next page is account
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home')) 
        else:
            flash('Login Unsucessful. Please check email and password','danger')       
    return render_template('login.html', title = "Login", form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    #get name picture
    _, f_text = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_text
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    out_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail
    i.save(picture_path)

    return picture_fn

#infor account
@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        
        current_user.user_name = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!','success')
        return redirect(url_for('account'))
    
    elif request.method =='GET':
        form.username.data = current_user.user_name
        form.email.data = current_user.email
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)

    return render_template('account.html', title = 'Account', image_file = image_file, form= form)

@app.route("/post/new", methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post_title = form.title.data
        post_content = form.content.data
        post = Post(title = post_title,content = post_content, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('home'))
    return render_template("create_post.html", title = "Create Post", form = form , name = "New Post")

@app.route("/post/<int:post_id>", methods = ['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = 'post', post = post)

@app.route("/gitlogin")
def gitlogin():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    print(resp.json())
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

@app.route("/post/<int:post_id>/update", methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated!",'success')
        return redirect (url_for('post', post_id = post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title = 'Update Post', form = form, name = "Update Post")

@app.route("/post/<int:post_id>/delete", methods = ['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted!",'success')
    return redirect (url_for('home'))
    