#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : CodeProblem.py
@Time : 2022/8/22 21:44
@Software: PyCharm
@Describe: 代码题
"""


class CodeProblem:
    def __init__(self, problemid, problemTypeNum, problem):
        self.problemid = problemid
        self.problemTypeNum = problemTypeNum
        self.problem = problem

    def __str__(self):
        return "题号：%d 题型：填空题 题目：%s" % (self.problemid, self.problem)
