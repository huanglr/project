# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp

class LoginForm(Form):
    username = StringField(validators=[Required(), Length(1, 64), ])
    password = PasswordField(validators=[Required(), ])
    remember_me = BooleanField()

