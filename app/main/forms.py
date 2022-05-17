from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddPostForm(FlaskForm):
    title = StringField("Pitch Title", validators = [DataRequired()])
    post = TextAreaField("Go", validators = [DataRequired()])
    category = SelectField("category", choices=[("data-science", "data-science"),("data-analytics","data-analytics"),("data-cleaning","data-cleaning"),("data-visualization","data-visualization"),("data-mining","data-mining"),("random","random")],validators = [DataRequired()])
    submit = SubmitField("Add post")


class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")    


class EditBio(FlaskForm):
    bio = StringField("Bio")
    submit = SubmitField("Update")     

 