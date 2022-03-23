#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 14:18
# @Author  : xxxMoneyCatxxx
# @File    : forms.py
# @Software: $sim

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
