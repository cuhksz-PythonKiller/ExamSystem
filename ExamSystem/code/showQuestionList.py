#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Python Killer
@license: (C) Copyright 2022-2022
@contact: nanyanzheng@link.cuhk.edu.cn
@File : showQuestionList.py
@Time : 2022/8/22 21:46
@Software: PyCharm
@Describe: 展示小题的数据
"""

# 从pandas的dataframe构造小题对象的构造函数
from code.model.FillBlanks import FillBlanks
from code.model.Judge import Judge
from code.model.MultipleChoice import MultipleChoice
from code.model.SingleChoice import SingleChoice
import pandas as pd
import logging

# 大题类型，字典存储
PROBLEM_SET_DICT = {
    'Basic python': 'BasicPython',
    'loop&logic': 'LoopAndLogic',
    'Function': 'Function',
    'Virtualization': 'Virtualization',
    'Nump& Pandas&others': 'NumpAndPandas'
}


def __build_single_choice(df_problem_row):
    singleChoice = SingleChoice(df_problem_row['problemid'], df_problem_row['type'], df_problem_row['problem'])
    singleChoice.set_choice(df_problem_row['A'], df_problem_row['B'], df_problem_row['C'], df_problem_row['D'])
    logging.info(f'question[{singleChoice.problemid}]: {singleChoice.problem}.')
    return singleChoice


def __build_multiple_choice(df_problem_row):
    multipleChoice = MultipleChoice(df_problem_row['problemid'], df_problem_row['type'], df_problem_row['problem'])
    multipleChoice.set_choice(df_problem_row['A'], df_problem_row['B'], df_problem_row['C'], df_problem_row['D'])
    logging.info(f'question[{multipleChoice.problemid}]: {multipleChoice.problem}.')
    return multipleChoice


def __build_judge(df_problem_row):
    judge = Judge(df_problem_row['problemid'], df_problem_row['type'], df_problem_row['problem'])
    judge.set_choice(df_problem_row['A'], df_problem_row['B'])
    logging.info(f'question[{judge.problemid}]: {judge.problem}.')
    return judge


def __build_fill_blanks(df_problem_row):
    fillBlanks = FillBlanks(df_problem_row['problemid'], df_problem_row['type'], df_problem_row['problem'])
    logging.info(f'question[{fillBlanks.problemid}]: {fillBlanks.problem}.')
    return fillBlanks


def __build_code_problem(df_problem_row):
    pass


# 这个函数给前端调用，返回一个大题的所有小题
# 前端提供输入参数：problem_title 大题名称，后端是表名
# 返回值：小题对象的列表
def build_problem_list(problem_title):
    logging.info(f'user choose {problem_title}')
    # 读问题表：
    sheet_choose = PROBLEM_SET_DICT[problem_title]
    # 提取该题库对应的sheet
    df_problem_all = pd.read_excel('excel_all.xlsx', sheet_name=sheet_choose)
    result_list = []
    for index, row in df_problem_all.iterrows():
        problem_type = row['type']
        if problem_type == 1:  # 要改
            result_list.append(__build_single_choice(row))
        elif problem_type == 2:
            result_list.append(__build_judge(row))
        elif problem_type == 3:
            result_list.append(__build_multiple_choice(row))
        elif problem_type == 4:
            result_list.append(__build_fill_blanks(row))
        else:
            continue
    return result_list


if __name__ == '__main__':
    # 这个字典的values就是前端传的5种题型的参数
    TITLE_DICT = {
        '1': 'Basic python',
        '2': 'loop&logic',
        '3': 'Function',
        '4': 'Virtualization',
        '5': 'Nump& Pandas&others'
    }
    print('------Question Type Selection-----')
    print('1: Basic python')
    print('2: loop&logic')
    print('3: Function')
    print('4: Virtualization')
    print('q: quit')
    print('------------------------------------')
    title_num = input('Enter your choice:')
    # 选中的大题的标题，对应题库表
    title = TITLE_DICT[title_num]
    # 大题的小题列表
    questions = build_problem_list(title)
    for q in questions:
        print(str(q))
