#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : User.py
@Time : 2022/8/22 22:25
@Software: PyCharm
@Describe: 用户
"""

class User:
    def __init__(self,id,name,passwd):
        self.id=id
        self.name=name
        self.passwd=passwd


    def set_right(self, right):
        self.righ = right

    def set_wrong(self, wrong):
        self.wrong = wrong

    def __str__(self):
        return f"用户名：{self.name} 正确题：{self.righ} 错误题：{self.wrong}"