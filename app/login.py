#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 17:35
# @Author  : xxxMoneyCatxxx
# @File    : login.py
# @Software: PyCharm

from . import login


@login.user_loader
def load_user(user_id):
    return User.get(user_id)
