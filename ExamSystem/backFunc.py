# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:25:35 2022

@author: Pan Yue
"""
import pandas as pd
import random

global list_problemChosen

def problemChoose(problem_set):
#定义函数，获取题目类型的数字与名字之间的对应关系，返回一个字典
    def getProblemType_dict():
        df_ProblemType=pd.read_excel('excel_all.xlsx',sheet_name='ProblemType')
        ProblemType_dict={}
        for i in range(0,len(df_ProblemType)):
            TypeNum=df_ProblemType.loc[i,'TypeNum']
            TypeName=df_ProblemType.loc[i,'TypeName']
            ProblemType_dict[TypeNum]=TypeName
        return ProblemType_dict
    ProblemType_dict=getProblemType_dict()
    
    
    
    #判断用户选择的是何种题型
    #创建一个字典，将用户选择的题库与excel中的sheet_name 对应
    #problem_set_dict={
    #    'Basic python':'BasicPython','loop&logic':'LoopAndLogic', 
    #    'Function':'Function','Virtualization':'Virtualization',
    #    'Nump& Pandas&others':'NumpAndPandas'
    #}
    
    
    #problem_set='loop&logic'#这是从前端传回来的数据，用户选择何种题库
    #sheet_choose=problem_set_dict[problem_set]
    sheet_choose=problem_set
    #提取该题库对应的sheet
    df_problem_all=pd.read_excel('excel_all.xlsx',sheet_name=sheet_choose)
    
    
    class SingleChoice:
        def __init__(self,problemid,problemTypeNum,problem):
            self.problemid=problemid
            self.problemTypeNum=problemTypeNum
            self.problem=problem
    
        def func_choice(self,A,B,C,D):
            self.A=A
            self.B=B
            self.C=C
            self.D=D
    
    class MultipleChoice:
        def __init__(self,problemid,problemTypeNum,problem):
            self.problemid=problemid
            self.problemTypeNum=problemTypeNum
            self.problem=problem
    
        def func_choice(self,A,B,C,D):
            self.A=A
            self.B=B
            self.C=C
            self.D=D
           
    class Judge:
        def __init__(self,problemid,problemTypeNum,problem):
            self.problemid=problemid
            self.problemTypeNum=problemTypeNum
            self.problem=problem
    
        def func_choice(self,A,B):
            self.A=A
            self.B=B
            
    
    class FillBlanks:
        def __init__(self,problemid,problemTypeNum,problem):
            self.problemid=problemid
            self.problemTypeNum=problemTypeNum
            self.problem=problem
    
    class CodeProblem:
        def __init__(self,problemid,problemTypeNum,problem):
            self.problemid=problemid
            self.problemTypeNum=problemTypeNum
            self.problem=problem
    
    
    
    def SingleChoice_ABCD(m,problem_index,problemid,problemTypeNum,problem,df_problem_all):
        A=df_problem_all.loc[i,'A']
        B=df_problem_all.loc[i,'B']
        C=df_problem_all.loc[i,'C']
        D=df_problem_all.loc[i,'D']
        m.func_choice(A,B,C,D)
    
    def MultipleChoice_ABCD(m,problem_index,problemid,problemTypeNum,problem,df_problem_all):
        A=df_problem_all.loc[i,'A']
        B=df_problem_all.loc[i,'B']
        C=df_problem_all.loc[i,'C']
        D=df_problem_all.loc[i,'D']
        m.func_choice(A,B,C,D)
    
    def Judge_AB(m,problem_index,problemid,problemTypeNum,problem,df_problem_all):
        A=df_problem_all.loc[i,'A']
        B=df_problem_all.loc[i,'B']
        m.func_choice(A,B)
    
    def FillBlanks_None(m,problem_index,problemid,problemTypeNum,problem,df_problem_all):
        pass
    
    def CodeProblem_None(m,problem_index,problemid,problemTypeNum,problem,df_problem_all):
        pass
    
    
    #随机选取5道题
        #生成5个随机数
    #row_len=df_problem_all.shape[0]
    #lista=random.sample(range(0,row_len),5)
    #lista=sorted(lista)
    
    lista=[0,1,2,3,4]
    type_dict=ProblemType_dict#前面用函数生成了题型数字与题型名称的字典，这里赋给type_dict
    #type_dict={1:'SingleChoice',2:'Judge',3:'MultipleChoice',4:'FillBlanks',5:'CodeProblem'}
    func_choice_dict={1:'SingleChoice_ABCD',2:'Judge_AB',3:'MultipleChoice_ABCD',4:'FillBlanks_None',5:'CodeProblem_None'}
    
    listb=[]
    list_problemid=[]
    for i in lista:
        problem_index=lista.index(i)#problem_index的含义是，此题是五道题目中的第几题
        problemTypeNum=df_problem_all.loc[i,'type']#取出type的数字
        problemType=type_dict[problemTypeNum]#将表示type的数字与type的名字对应
        problemid=df_problem_all.loc[i,'problemid']#取出对应题号
        problem=df_problem_all.loc[i,'problem']#取出对应题目
        m=eval(problemType)(problemid,problemTypeNum,problem)#创建m为对象
        eval(func_choice_dict[problemTypeNum])(m,problem_index,problemid,problemTypeNum,problem,df_problem_all)#给m对象，加上选项
        listb.append(m)
        list_problemid.append(problemid)
    
    problem1=listb[0]
    problem2=listb[1]
    problem3=listb[2]
    problem4=listb[3]
    problem5=listb[4]

    list_problemChosen=[problem1,problem2,problem3,problem4,problem5]
    return list_problemChosen,list_problemid


#寻找答案
def answerJudge(answer_input_list):
    #前端的答案用一个list传，[problem1的答案，problem2的答案，……]
    answer_input_list=['A','C','D','null','A']
    
    #从excel中取出存储的答案
    df_answer=pd.read_excel('excel_all.xlsx',sheet_name='Answer')
    answer_problemid=df_answer['problemid']
    
    #取出每一道题在excel中存的答案
    answer_chosen_list=[]#构建answer的列表，列表元素依次为，[{prblem1的题目id：problem1的答案}，……]
    for item in list_problemChosen:
        for j in answer_problemid:
            #item_problemid=item.problemid
            if item.problemid==j:
                indexlist_answer=df_answer.loc[df_answer.problemid==j].index.tolist()#获取该答案所在的行,返回一个列表
                index_answer=indexlist_answer[0]
                answer_chosen=df_answer.loc[index_answer,'answer']
                answer_chosen_dict={j:answer_chosen}
                answer_chosen_list.append(answer_chosen_dict)
    #print(answer_list)
    
    
    
    #对每一道题，根据题目类型判断题目对错
    #定义每一种题型的判断对错函数
    #RW表示right,wrong
    #Ture为对，False为错
    def SingleChoice_RW(answer_input,answer_chosen):
        if answer_input==answer_chosen:
            result=True
        else:
            result=False
        return result
    
    def MultipleChoice_RW(answer_input,answer_chosen):
        #先对传进来的str进行排序，比如把“BCA”排序成“ABC"
        listd=list(answer_input)
        listd=sorted(listd)
        answer_input=''.join(listd)
        if answer_input==answer_chosen:
            result=True
        else:
            result=False
        return result
    
    def Judge_RW(answer_input,answer_chosen):
        if answer_input==answer_chosen:
            result=True
        else:
            result=False
        return result
    
    def FillBlanks_RW(answer_input,answer_chosen):
        if answer_input==answer_chosen:
            result=True
        else:
            result=False
        return result
    
    def CodeProblem_RW(answer_input,answer_chosen):
        result=None
        return result
    
    
    
    #目前有前端传过来的'answer_input_list'，从excel中提取的‘answer_chosen_list’,还有problem的list'list_problemChosen'
    func_answer_dict={1:'SingleChoice_RW',2:'Judge_RW',3:'MultipleChoice_RW',4:'FillBlanks_RW',5:'CodeProblem_RW'}
    
    result_list=[]
    #对每一个problem，根据题目类型，调用函数，进行对错判断
    for i in range(0,5):
        
        ob=list_problemChosen[i]#从problem_list中选取problem
        problemid=ob.problemid#取出该problem的problemid
    
        answer_input=answer_input_list[i]#取出当前problem的answer_input
        answer_chosen=answer_chosen_list[i].get(problemid)#取出当前problem的answer_store
    
        problemTypeNum=ob.problemTypeNum#取出该problem的typeNum
        result=eval(func_answer_dict[problemTypeNum])(answer_input,answer_chosen)#根据TypeNum调用判断对错函数
    
        result_dict={problemid:result}
        result_list.append(result_dict)
    
    #print(result_list)
