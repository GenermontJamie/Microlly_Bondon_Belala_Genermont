from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,TextField ,TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from wtfpeewee.orm import model_form
from models import Publication, User


#Définition des différents formulaires


class PublicationForm(FlaskForm):
    pass

NewPublicationForm = model_form(Publication, exclude=('created_at', 'user', 'modified_at'))

class UserForm(FlaskForm):
    pass

NewUserForm = model_form(User)

class EditPublicationForm(FlaskForm):
    title = TextAreaField('title',validators=[DataRequired()])
    body = TextAreaField('body',validators=[DataRequired()])
    pass

NewEditPublicationForm = model_form(Publication, exclude=('created_at', 'user', 'modified_at'))


class LoginForm(FlaskForm):
    pass

NewLoginForm = model_form(User, exclude=('first_name', 'last_name', 'email','birthday'))