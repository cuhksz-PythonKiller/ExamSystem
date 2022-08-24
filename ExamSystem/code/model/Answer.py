#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : Answer.py
@Time : 2022/8/22 21:44
@Software: PyCharm
@Describe: 答案
"""


class Answer:
    def __init__(self,problemid,type,answer):
        self.problemid=problemid
        self.type=type
        self.answer=answer

    def __str__(self):
        return f"题号：{self.problemid} 题型：{self.type} 答案：{self.answer}"