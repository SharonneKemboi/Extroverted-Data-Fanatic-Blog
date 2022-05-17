from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import AddPostForm,AddComment,EditBio
from ..models import User,Post,Comment
from .. import db,photos
import markdown2
from flask_login import login_required, current_user
import datetime
from ..requests import random_post



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    posts = Post.query.order_by(Post.date.desc()).all()
    title = "Home"
    shanny = random_post()
    quote = shanny["quote"]
    quote_author = shanny ["author"]
    return render_template('index.html', title = title, posts = posts, quote = quote , quote_author=quote_author)

@main.route("/posts/<category>")
def categories(category):

    posts = None
    if category == "all":
        posts = Post.query.order_by(Post.time.desc())
    else:
        posts = Post.query.filter_by(category = category).order_by(Post.time.desc()).all()

    return render_template("posts.html", posts = posts, title = category.upper())


@main.route("/<uname>/add/post", methods = ["GET","POST"])
@login_required
def add_post(uname):
    form = AddPostForm()
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)
    title = "Create post"
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]

        new_post = Post(title = title, content = post, category = category,user = user,date =date, time = time)
        new_post.save_post()
        posts = Post.query.all()

        return redirect(url_for("main.categories",category = category))

    return render_template("add_post.html", form = form, title = title) 


@main.route("/<user>/post/<post_id>/add/comment", methods = ["GET","POST"])
@login_required
def comment(user,post_id):
    user = User.query.filter_by(id = user).first()
    post = Post.query.filter_by(id = post_id).first()
    form = AddComment()

    title = "Add comment"
    if form.validate_on_submit():
        content = form.content.data
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]
       
        new_comment = Comment(content = content, user = user, post = post, time = time, date = date )
        new_comment.save_comment()
        return redirect(url_for("main.view_comments", post_id = post_id))
    return render_template("comment.html", post=post, title = title,form = form)

@main.route("/<post_id>/comments")
@login_required
def view_comments(post_id):

     

    post = Post.query.filter_by(id = post_id).first()
    title = "Comments"
    comments = post.get_post_comments()

    return render_template("view_comments.html", comments = comments, post = post,title = title)


@main.route("/profile/<user_id>")
@login_required
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    posts = Post.query.filter_by(user_id = user.id).order_by(Post.time.desc())
    title = user.name.upper()
    return render_template("profile.html", posts = posts, user = user, title = title)


@main.route("/<user_id>/profile")
def user(user_id):
    user = User.query.filter_by(id = user_id).first()
    posts = Post.query.filter_by(user_id = user.id).order_by(Post.time.desc())
    title = user.name.upper()
    return render_template("user.html", posts = posts, user = user,title = title)

    
@main.route("/pic/<user_id>/update", methods = ["POST"])
@login_required
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()
    title = "Edit Profile"
    if "profile-pic" in request.files:
        pic = photos.save(request.files["profile-pic"])
        file_path = f"photos/{pic}"
        user.profile_pic = file_path
        db.session.commit()
    return redirect(url_for("main.profile", user_id = user.id))



@main.route("/<user_id>/profile/edit",methods = ["GET","POST"])
@login_required
def update_profile(user_id):

    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    form = EditBio()

    if form.validate_on_submit():
        bio = form.bio.data
        user.bio = bio
        db.session.commit() 
        return redirect(url_for('main.profile',user_id = user.id)) 
    return render_template("update_profile.html",form = form, title=title)

