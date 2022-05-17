from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from datetime import datetime
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    This is the class which we will use to create the users for the app
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    profile_pic  = db.Column(db.String)
    posts = db.relationship("Post", backref= "user", lazy="dynamic")
    comments = db.relationship("Comment", backref="user", lazy="dynamic")
    password_hash = db.Column(db.String)
    

    def save_user(self):
        db.session.add(self)
        db.session.commit()


    @property
    def password(self):
        raise AttributeError("Oooops! Try Again")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def get_user_posts(self):
        user = User.query.filter_by(id = self.id).first()
        return user.posts

    def get_user_comments(self):
        user  = User.query.filter_by(id = self.id).first()
        return user.comments


class Post(db.Model):
    """
    This is the class which we will use to create the posts for the app
    """
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    category = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref = "post", lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def get_post_comments(self):
        post = Post.query.filter_by(id = self.id).first()

        comments = Comment.query.filter_by(post_id = post.id).order_by(Comment.time.desc())
        return comments

        

class Comment(db.Model):
    """
    This is the class which we will use to create the comments for the posts
    """

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

