#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : MultipleChoice.py
@Time : 2022/8/22 21:25
@Software: PyCharm
@Describe: 多选题
"""


class MultipleChoice:
    def __init__(self, problemid, problemTypeNum, problem):
        self.problemid = problemid
        self.problemTypeNum = problemTypeNum
        self.problem = problem

    def set_choice(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def __str__(self):
        return "题号：%d 题型：多选题 题目：%s A.%s B.%s C.%s D.%s" % (self.problemid, self.problem, self.A, self.B, self.C, self.D)