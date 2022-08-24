#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhengnanyan
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 872397486@qq.com
@File : __init__.py.py
@Time : 2022/8/22 21:19
@Site : 
@Software: PyCharm
'''
import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='ExamSystem.log', level=logging.INFO, format=LOG_FORMAT)