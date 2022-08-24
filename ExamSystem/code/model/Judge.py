#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : Judge.py
@Time : 2022/8/22 21:43
@Software: PyCharm
@Describe: 判断题
"""

class Judge:
    def __init__(self,problemid,problemTypeNum,problem):
        self.problemid=problemid
        self.problemTypeNum=problemTypeNum
        self.problem=problem

    def set_choice(self,A,B):
        self.A=A
        self.B=B

    def __str__(self):
        return "题号：%d 题型：判断题 题目：%s A.%s B.%s" % (self.problemid,self.problem,self.A,self.B)