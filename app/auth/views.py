from . import auth
from ..import db
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
# from app.email import create_mail



@auth.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        profile_pic = "photos/default.png"
        bio = "User has no bio"
        new_user = User(name = username, email = email, password = password,profile_pic = profile_pic, bio = bio)
        # new_user.save_user()
        db.session.add(new_user)
        db.session.commit()
        # create_mail("Hey Karibu","email/email",new_user.email,name = new_user.name)
        return redirect(url_for('auth.login'))
    title = 'Data Fanatics Blog- Register'
    return render_template("auth/register.html",form = form, title = title)
    #Return redirect


@auth.route("/login", methods = ["GET","POST"])
def login():
    login_form= LoginForm()

    
    if login_form.validate_on_submit():
        # user_email = login_form.email.data
        # user_password = login_form.password.data
        # remember = login_form.remember_me.data
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember_me)
            flash("Hola!! You Must Be A Data Fanatic Well Lets Get started")
            return redirect(request.args.get('next') or url_for('main.index'))
           
        flash("Invalid username or pasword")
    title = 'Data Fanatics Blog- Login'
    return render_template("auth/login.html",login_form = login_form, title = title)    



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))