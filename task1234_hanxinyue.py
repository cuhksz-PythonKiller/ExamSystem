#task1 @panpan
import pandas as pd
#定义函数，获取题目类型的数字与名字之间的对应关系，返回一个字典
def getProblemType_dict():
    df_ProblemType=pd.read_excel('excel_all.xlsx',sheet_name='ProblemType')
    ProblemType_dict={}
    for i in range(0,len(df_ProblemType)):
        TypeNum=df_ProblemType.loc[i,'TypeNum']
        TypeName=df_ProblemType.loc[i,'TypeName']
        ProblemType_dict[TypeNum]=TypeName
    return ProblemType_dict

ProblemType_dict=getProblemType_dict()#潘潘的task4用到了task1的字典，需要赋值
getProblemType_dict()#欣玥的task4没用到task1的字典，直接调用函数生成字典


#task2 @panpan
#判断用户选择的是何种题型
#创建一个字典，将用户选择的题库与excel中的sheet_name 对应
problem_set_dict={
    'Basic python':'BasicPython','loop&logic':'LoopAndLogic', 
    'Function':'Function','Virtualization':'Virtualization',
    'Nump& Pandas&others':'NumpAndPandas'
}
problem_set='loop&logic'#这是从前端传回来的数据，用户选择何种题库
sheet_choose=problem_set_dict[problem_set]
#提取该题库对应的sheet
df_problem_all=pd.read_excel('excel_all.xlsx',sheet_name=sheet_choose)


#task3 @panpan,xinyue
#创建5种题型的类
class SingleChoice:#单选题
    def __init__(self,problemid,problemTypeNum,problem):
        self.problemid=problemid
        self.problemTypeNum=problemTypeNum
        self.problem=problem
    
    def func_choice(self,A,B,C,D):
        self.A=A
        self.B=B
        self.C=C
        self.D=D

    def __str__(self):#打印print(对象)
        return "题号：%d 题型：单选题 题目：%s A.%s B.%s C.%s D.%s" % (self.problemid,self.problem,self.A,self.B,self.C,self.D)

class MultipleChoice:#多选题
    def __init__(self,problemid,problemTypeNum,problem):
        self.problemid=problemid
        self.problemTypeNum=problemTypeNum
        self.problem=problem

    def func_choice(self,A,B,C,D):
        self.A=A
        self.B=B
        self.C=C
        self.D=D

    def __str__(self):
        return "题号：%d 题型：多选题 题目：%s A.%s B.%s C.%s D.%s" % (self.problemid,self.problem,self.A,self.B,self.C,self.D)   

class Judge:#判断题
    def __init__(self,problemid,problemTypeNum,problem):
        self.problemid=problemid
        self.problemTypeNum=problemTypeNum
        self.problem=problem

    def func_choice(self,A,B):
        self.A=A
        self.B=B

    def __str__(self):
        return "题号：%d 题型：判断题 题目：%s A.%s B.%s" % (self.problemid,self.problem,self.A,self.B)    

class FillBlanks:#填空题
    def __init__(self,problemid,problemTypeNum,problem):
        self.problemid=problemid
        self.problemTypeNum=problemTypeNum
        self.problem=problem
    
    def __str__(self):
        return "题号：%d 题型：填空题 题目：%s" % (self.problemid,self.problem)

class CodeProblem:#代码作答
    def __init__(self,problemid,problemTypeNum,problem):
        self.problemid=problemid
        self.problemTypeNum=problemTypeNum
        self.problem=problem

    def __str__(self):
        return "题号：%d 题型：填空题 题目：%s" % (self.problemid,self.problem)


#task4 @xinyue
#遍历题库df，判断type并以对象形式返回
#方法一：不随机，只读前5道题(不考虑填空和代码作答)
list_problem=[]
for i in range(0,len(df_problem_all)):
    problemid=df_problem_all.loc[i,'problemid']
    type=df_problem_all.loc[i,'type']
    problem=df_problem_all.loc[i,'problem']
    A=df_problem_all.loc[i,'A']
    B=df_problem_all.loc[i,'B']
    C=df_problem_all.loc[i,'C']
    D=df_problem_all.loc[i,'D']
    if type==1:
        problemi=SingleChoice(problemid,type,problem)
        problemi.func_choice(A,B,C,D)
        list_problem.append(problemi)
        
    elif type==2:
        problemi=Judge(problemid,type,problem)
        problemi.func_choice(A,B)
        list_problem.append(problemi)
        
    elif type==3:
        problemi=MultipleChoice(problemid,type,problem)
        problemi.func_choice(A,B,C,D)
        list_problem.append(problemi)
        
    elif type==4:
        problemi=FillBlanks(problemid,type,problem)
        list_problem.append(problemi)
    
    elif type==5:
        problemi=CodeProblem(problemid,type,problem)
        list_problem.append(problemi)

list_problem

#方法二：随机5道题
import random
lista=list(range(0,len(df_problem_all)))#随机在[0,1,2,3,4,5,6](0到题库df的最大index)中抽取5个数(抽取5个index)
listb=sorted(random.sample(lista,5))#并按从小到大排列

list_problem=[]
for i in listb:
    problemid=df_problem_all.loc[i,'problemid']
    type=df_problem_all.loc[i,'type']
    problem=df_problem_all.loc[i,'problem']
    A=df_problem_all.loc[i,'A']
    B=df_problem_all.loc[i,'B']
    C=df_problem_all.loc[i,'C']
    D=df_problem_all.loc[i,'D']
    if type==1:
        problemi=SingleChoice(problemid,type,problem)
        problemi.func_choice(A,B,C,D)
        list_problem.append(problemi)
        
    elif type==2:
        problemi=Judge(problemid,type,problem)
        problemi.func_choice(A,B)
        list_problem.append(problemi)
        
    elif type==3:
        problemi=MultipleChoice(problemid,type,problem)
        problemi.func_choice(A,B,C,D)
        list_problem.append(problemi)
        
    elif type==4:
        problemi=FillBlanks(problemid,type,problem)
        list_problem.append(problemi)
    
    elif type==5:
        problemi=CodeProblem(problemid,type,problem)
        list_problem.append(problemi)

list_problem