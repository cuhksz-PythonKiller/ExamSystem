#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : SingleChoice.py
@Time : 2022/8/22 21:22
@Software: PyCharm
@Describe: 单选题数据结构对象
"""


class SingleChoice:
    def __init__(self, problemid, problemTypeNum, problem):
        self.problemid = problemid
        self.problemTypeNum = problemTypeNum
        self.problem = problem

    def set_choice(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def __str__(self):  # 打印print(对象)
        return "题号：%d 题型：单选题 题目：%s A.%s B.%s C.%s D.%s" % (self.problemid, self.problem, self.A, self.B, self.C, self.D)