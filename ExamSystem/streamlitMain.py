# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:08:23 2022

@author: Lenovo1
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import PercentFormatter
import numpy as np
import logging
#from task12345 import list_problemChosen

#from proble import * #引用模块中的函数
import backFunc as back
from code.showAnswerResult import match_answer

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='C:/Users/HP/Documents/Python/streamlit+backFunc(1)/ExamSystem.log', level=logging.INFO, format=LOG_FORMAT)


#global list_problemChosen
#########################################################
#定义多页面函数
class MultiPages:
    def __init__(self):
        self.titles_list = []
        self.func_dict = {}

    def add_TitleAndFunc(self, title, func):
        if title not in self.titles_list:
            self.titles_list.append(title)
            self.func_dict[title] = func
#如果选择了‘basic python选项’，函数内的title则为‘basic python’
    def run(self):
        title = st.sidebar.radio(
            'Go To',
            self.titles_list,
            format_func=lambda title: str(title))#str函数可能是多余的
        func_dict=self.func_dict
        func_name=func_dict.get(title)
        eval(func_name)()
##############################################################
        
global setChosen#setChosen表示当前选择的题库

setChosen='BasicPython'
#定义页面       
#定义页面1-登录页面

#########################################################更新(xhp
def logo_detect(Username, password):
    user_table = pd.read_excel('user_all.xlsx',sheet_name='Users')
    temp_table = pd.read_excel('user_temp.xlsx',sheet_name='Temp')
    all_username = list(user_table['name'])
    if Username in all_username:
        if password == str(user_table.loc[all_username.index(Username), 'password']):
            st.success('login successfully')
            temp_table.loc[0, 'name'] = Username
            user_table.loc[all_username.index(Username), 'Login'] = 2
            temp_table.to_excel('user_temp.xlsx', index=False,sheet_name='Temp')
            user_table.to_excel('user_all.xlsx', index=False,sheet_name='Users')#改变user——all用户log状态
        else:
            st.error('password error')
    else:
        st.error('The Username does not exist')

def page_login():
    st.title('Page Login')
    input_Username=st.text_input('Username',max_chars=20).strip()
    input_password = st.text_input('Password', type='password',max_chars=20).strip()
    if st.button('sign in'):
        logo_detect(input_Username,input_password)
        logging.info(f'user [{input_Username}] login')

##############################################################更新(xhp


#定义页面2-题库答题页面：#从外部传入一个setChosen函数
def page_problem(setChosen):
    
    #定义各类题型的题目展示函数
    #problem为一个object
    #定义单选题的题目展示函数
    def SingleChoice_show(problemObject,key_type,setChosen,i):
        str_i=str(i)
        key_str=setChosen+key_type+str_i
        problem_show=problemObject.problem#problem_show为要展示的题目
        logging.info(f'[SingleChoice]: {problemObject.problem}')
        # (f'question[{fillBlanks.problemid}]: {fillBlanks.problem}.')
        choice_default='Please choose your answer'
        choice_A='A. '+str(problemObject.A)
        choice_B='B. '+str(problemObject.B)
        choice_C='C. '+str(problemObject.C)
        choice_D='D. '+str(problemObject.D)
        st.text(problem_show)
        choice_list=[choice_default,choice_A,choice_B,choice_C,choice_D]
        answer_chosen=st.radio('Single Choice',choice_list,key=key_str)
        
        #获取用户选择的答案
        answer_result='null'
        if answer_chosen==choice_default:
            answer_result='null'
        elif answer_chosen==choice_A:
            answer_result='A'
        elif answer_chosen==choice_B:
            answer_result='B'
        elif answer_chosen==choice_C:
            answer_result='C'
        elif answer_chosen==choice_D:
            answer_result='D'
        
        return answer_result
    #定义判断题的题目展示函数
    def Judge_show(problemObject,key_type,setChosen,i):
        str_i=str(i)
        key_str=setChosen+key_type+str_i
        problem_show=problemObject.problem#problem_show为要展示的题目
        logging.info(f'[Judge]: {problem_show}')
        choice_default='Please choose your answer'
        choice_A='A. '+str(problemObject.A)
        choice_B='B. '+str(problemObject.B)
        st.text(problem_show)
        choice_list=[choice_default,choice_A,choice_B]
        answer_chosen=st.radio('Judge',choice_list,key=key_str)
        
        #获取用户选择的答案
        answer_result='null'
        if answer_chosen==choice_default:
            answer_result='null'
        elif answer_chosen==choice_A:
            answer_result='A'
        elif answer_chosen==choice_B:
            answer_result='B'
    
        return answer_result
    
    
    #定义多选题的展示函数
    def MultipleChoice_show(problemObject,key_type,setChosen,i):
        str_i=str(i)
        key_str=setChosen+key_type+str_i
        problem_show=problemObject.problem#problem_show为要展示的题目
        logging.info(f'[MultipleChoice]: {problem_show}')
        choice_A='A. '+str(problemObject.A)
        choice_B='B. '+str(problemObject.B)
        choice_C='C. '+str(problemObject.C)
        choice_D='D. '+str(problemObject.D)
        st.text(problem_show)
        choice_list=[choice_A,choice_B,choice_C,choice_D]
        answer_chosen=st.multiselect('Multiple Choice',choice_list,key=key_str)
        
        #获取用户选择的答案
        answer_result=''
        answer_result_list=[]
        for i in answer_chosen:
            i_list=list(i)
            answer_result_list.append(i[0])
            
        answer_result_list=sorted(answer_result_list)
        answer_result=''.join(answer_result_list)
        return answer_result
    
    #定义填空题的展示函数
    def FillBlanks_show(problemObject,key_type,setChosen,i):
        str_i=str(i)
        key_str=setChosen+key_type+str_i
        problem_show=problemObject.problem#problem_show为要展示的题目
        logging.info(f'[FillBlanks]: {problem_show}')
        st.text(problem_show)    
        answer_chosen=st.text_input('Fill Blanks', value="",key=key_str)
        
        #获取用户选择的答案
        answer_result='null'
        answer_result=answer_chosen
        return answer_result
    
    #主函数：题目展示的主函数
    #st.title('Page Problem')
    answer_result_list={}
    title_str=str(setChosen)
    st.title(title_str)
    type_dict={1:'SingleChoice',2:'Judge',3:'MultipleChoice',4:'FillBlanks',5:'CodeProblem'}
    list_problemChosen,list_problemid= back.problemChoose(setChosen)
    for i in range(0,5):
        j=i+1
        str_subheader='Question'+str(j)    
        st.subheader(str_subheader)
        
        problemObject=list_problemChosen[i]
        if problemObject.problemTypeNum==1:
            answer_result=SingleChoice_show(problemObject,'SingleChoice',setChosen,i)
            answer_result_list[list_problemid[i]]=answer_result
        elif problemObject.problemTypeNum==2:
            answer_result=Judge_show(problemObject,'Judge',setChosen,i)
            answer_result_list[list_problemid[i]]=answer_result
        elif problemObject.problemTypeNum==3:
            answer_result=MultipleChoice_show(problemObject,'MultipleChoice',setChosen,i)
            answer_result_list[list_problemid[i]]=answer_result
        elif problemObject.problemTypeNum==4:
            answer_result=FillBlanks_show(problemObject,'FillBlanks',setChosen,i)
            answer_result_list[list_problemid[i]]=answer_result
    st.text(answer_result_list)

    def write_user_result(right, wrong):
        df_user_all = pd.read_excel('user_all.xlsx', sheet_name='Users')
        df_user_now = pd.read_excel('user_temp.xlsx', sheet_name='Temp')
        user_name = df_user_now.loc[0, 'name']
        all_username = list(df_user_all['name'])
        index_num = all_username.index(user_name)

        comma = ','
        df_user_all.loc[index_num, 'right'] =str(df_user_all.loc[index_num, 'right'])+ comma + str(right).strip('{}').replace(' ','')
        df_user_all.loc[index_num, 'wrong'] =str(df_user_all.loc[index_num, 'wrong'])+ comma + str(wrong).strip('{}').replace(' ','')
        df_user_all.loc[index_num, 'right']= df_user_all.loc[index_num, 'right'].strip('nan,')
        df_user_all.loc[index_num, 'wrong']= df_user_all.loc[index_num, 'wrong'].strip('nan,')
        df_user_all.to_excel('user_all.xlsx',sheet_name='Users')

    #定义提交函数  
    def submitFunc(answer_result_list):
        
        df_user_all=pd.read_excel('user_all.xlsx',sheet_name='Users')
        df_user_now=pd.read_excel('user_temp.xlsx',sheet_name='Temp')
        user_name=df_user_now.loc[0,'name']
        right,wrong = match_answer(user_name,answer_result_list)

        indexlist_user=df_user_all.loc[df_user_all.name==user_name].index.tolist()#获取该user所在的行,返回一个列表
        index_user=indexlist_user[0]
        df_user_all.loc[index_user,setChosen]=3
        df_user_all.to_excel('user_all.xlsx',sheet_name='Users',index=False)
        st.write(str(right))
        write_user_result(right, wrong)


    if st.button('Submit'):
        submitFunc(answer_result_list)


#定义页面3-提示用户已登录，请选择题库进行作答页面：
def page_already_login():
    st.title('Page Already Login')
    pass

#定义页面4：提示用户未登录，请进行登录页面：
def page_not_login():
    st.title('Page Not Login')
    pass

#定义页面5：提示用户，该题库已作答
def page_already_answer():
    st.title('Page Already Answer')
    pass

#定义页面6：分析报告页面
def page_analyze():
    st.title('Page Analyze')
    temp_table = pd.read_excel('user_temp.xlsx', sheet_name='Temp')
    username = list(temp_table['name'])[0]
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 用来正常显示中文标签
    st.write("根据答题结果分析报告如下：")


    def draw_columnars(list1, list2, type_list, colors, title):
        data = [list1, list2]
        x = range(len(list1))
        width = 0.35
        fig = plt.figure()
        # 将bottom_y元素都初始化为0
        bottom_y = np.zeros(len(type_list))
        data = np.array(data)
        # 按列计算计算每组柱子的总和，为计算百分比做准备
        sums = np.sum(data, axis=0)
        for i, color in zip(data, colors):
            # 计算每个柱子的高度，即百分比
            y = i / sums
            pl = plt.bar(x, y, width, bottom=bottom_y, color=color)
            plt.bar_label(pl, label_type="center", color="k")
            # 计算bottom参数的位置
            bottom_y = y + bottom_y
        # 生成legend
        legend_labels = ["正确", "错误"]
        patches = [mpatches.Patch(color=colors[h], label="{:s}".format(legend_labels[h])) for h in
                   range(len(legend_labels))]
        ax = plt.gca()
        ax.legend(handles=patches, ncol=1, bbox_to_anchor=(1, 1), borderaxespad=2)
        plt.xticks(x, type_list)
        # 纵轴设置为百分比
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.title(title, fontdict={'size': 15})
        return fig

    def draw_columnar1(right_list, wrong_list):
        type_list = ['BasicPython', 'LoopAndLogic', 'Function', 'Virtualization', 'NumpAndPandas']
        list1 = [0, 0, 0, 0, 0]
        list2 = [0, 0, 0, 0, 0]
        for i in right_list:
            temp = i.split(':')
            list1[int(temp[0][0:1]) - 1] += 1
        for i in wrong_list:
            temp = i.split(':')
            list2[int(temp[0][0:1]) - 1] += 1
        colors = ['#FFE4C4', '#B0C4DE']
        title = "各题型情况分析"
        fig = draw_columnars(list1, list2, type_list, colors, title)
        st.pyplot(fig)
        max_value = max(list1)
        temp = []
        for i in range(len(list1)):
            if list1[i] == max_value: temp.append(type_list[i])
        print(temp)
        st.subheader("您擅长的题型是:" + "、".join(temp))

    def draw_columnar2(right_list, wrong_list):
        type_list = ['单选题', '判断题', '多选题', '填空题']
        list1 = [0, 0, 0, 0]
        list2 = [0, 0, 0, 0]
        for i in right_list:
            temp = i.split(':')
            list1[int(temp[1]) - 1] += 1
        for i in wrong_list:
            temp = i.split(':')
            list2[int(temp[1]) - 1] += 1
        colors = ['#AFEEEE', '#F08080']
        title = "各题型情况分析"
        fig = draw_columnars(list1, list2, type_list, colors, title)
        st.pyplot(fig)
        max_value = max(list1)
        temp = []
        for i in range(len(list1)):
            if list1[i] == max_value: temp.append(type_list[i])
        print(temp)
        st.subheader("您擅长的题型是:" + "、".join(temp))

    def read_excel(username):
        user_table = pd.read_excel('user_all.xlsx', sheet_name='Users')
        all_username = list(user_table['name'])
        right_str = user_table.loc[all_username.index(username), 'right']
        wrong_str = user_table.loc[all_username.index(username), 'wrong']
        right_list = right_str.split(',')
        wrong_list = wrong_str.split(',')
        draw_columnar1(right_list, wrong_list)
        draw_columnar2(right_list, wrong_list)
        draw_pie(right_list, wrong_list)

    def draw_pie(right_list, wrong_list):
        labels = ["正确", "错误"]
        colors = ["#40E0D0", "#3CB371"]
        sizes = [len(right_list), len(wrong_list)]
        fig = plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.2f%%',
                startangle=90, colors=colors, textprops={'color': "white",
                                                         "fontsize": "16"})  # '%1.1f'：指小数点后保留一位有效数值；'%1.2f%%'保留两位小数点，增加百分号（%）;startangle=90则从y轴正方向画起
        plt.axis('equal')  # 该行代码使饼图长宽相等
        plt.title('答题总情况占比', fontdict={'size': 15})
        plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)  # 添加图例
        st.pyplot(fig)

    read_excel(username)



#####################################################################定义页面7：用户退出登录页面：
def page_logout():
    user_table = pd.read_excel('user_all.xlsx', sheet_name='Users')
    temp_table = pd.read_excel('user_temp.xlsx', sheet_name='Temp')
    Username=list(temp_table['name'])[0]
    all_username = list(user_table['name'])
    st.title('Page Log Out')
    if st.button('log out'):
        user_table.loc[all_username.index(Username), 'Login'] = 1
        user_table.to_excel('user_all.xlsx',sheet_name='Users')


#############################################################################更新（xhp
#定义页面8：用户登录后的login界面
def page_Welcome():
    temp_table = pd.read_excel('user_temp.xlsx',sheet_name='Temp')
    username=str(temp_table.loc[0,'name'])
    st.title(username)
    st.title("Welcome to Python World ")

#################################################################
#定义不同题库的答题页面函数

def page_problem_BasicPython():
    setChosen='BasicPython'
    page_problem(setChosen)
    pass

def page_problem_LoopAndLogic():
    setChosen='LoopAndLogic'
    page_problem(setChosen)
    pass

def page_problem_Function():
    setChosen='Function'
    page_problem(setChosen)
    pass

def page_problem_Virtualization():
    setChosen='Virtualization'
    page_problem(setChosen)
    pass

def page_problem_NumpAndPandas():
    setChosen='NumpAndPandas'
    page_problem(setChosen)
    pass










############################################################
#定义函数：生成pagestate_dict的函数

def create_pagestate_dict():
    state_dict={}
    df_user_all=pd.read_excel('user_all.xlsx',sheet_name='Users')
    df_user_now=pd.read_excel('user_temp.xlsx',sheet_name='Temp')
    key_list=[
        'Login',
        'BasicPython',
        'LoopAndLogic',
        'Function',
        'Virtualization',
        'NumpAndPandas',
        'Analysis',
        'LogOut'
    ]
    user_name=df_user_now.loc[0,'name']
    indexlist_user=df_user_all.loc[df_user_all.name==user_name].index.tolist()#获取该user所在的行,返回一个列表
    index_user=indexlist_user[0]
    for key_name in key_list:
        state_dict[key_name]=df_user_all.loc[index_user,key_name]
    pagestate_dict=state_dict
    return pagestate_dict


#定义函数：页面选择函数
def pageChooseFunc():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='ExamSystem.log', level=logging.INFO, format=LOG_FORMAT)
    global pagestate_dict
    #pagestate_dict={
    #    'Login':1,
    #    'BasicPython':2,
    #    'LoopAndLogic':2,
    #    'Function':2,
    #    'Virtualization':2,
    #   'NumpAndPandas':2,
    #    'Analysis':2,
    #    'LogOut':2
    #    }
    pagestate_dict = create_pagestate_dict()
    
    ###############################################
    #定义页面选择函数
    #对于登录界面，定义页面选择函数
    def login_page(loginState):
        if loginState==1:
            func='page_login'
        elif loginState== 2:
             func = 'page_Welcome'
        return func
    
    #对于BasicPython题库界面，定义页面选择函数：
    def BasicPython_page(Logo_state,BasicPythonState):
        if Logo_state==1:
            func='page_not_login'
        elif BasicPythonState==2:
            func='page_problem_BasicPython'
            #setChosen='BasicPython'
        elif BasicPythonState==3:
            func='page_already_answer'
        return func
    
    #对于LoopAndLogic题库界面，定义页面选择函数：
    def LoopAndLogic_page(Logo_state,LoopAndLogicState):
        if Logo_state==1:
            func='page_not_login'
        elif LoopAndLogicState==2:
            func='page_problem_LoopAndLogic'
            #setChosen='LoopAndLogic'
        elif LoopAndLogicState==3:
            func='page_already_answer'
        return func
    
    def Function_page(Logo_state,FunctionState):
        if Logo_state==1:
            func='page_not_login'
        elif FunctionState==2:
            func='page_problem_Function'
            #setChosen='Function'
        elif FunctionState==3:
            func='page_already_answer'
        return func
    
    def Virtualization_page(Logo_state,VirtualizationState):
        if Logo_state==1:
            func='page_not_login'
        elif VirtualizationState==2:
            func='page_problem_Virtualization'
            #setChosen='Virtualization'
        elif VirtualizationState==3:
            func='page_already_answer'
        return func
    
    def NumpAndPandas_page(Logo_state,NumpAndPandasState):
        if Logo_state==1:
            func='page_not_login'
        elif NumpAndPandasState==2:
            func='page_problem_NumpAndPandas'
            #setChosen='NumpAndPandas'
        elif NumpAndPandasState==3:
             func='page_already_answer'
        return func
    
    def Analysis_page(Logo_state,AnalysisState):
        if Logo_state==1:
            func='page_not_login'
        elif AnalysisState==2:
            func='page_analyze'
        return func
    #####################################这里修改logout和login都有一个参数控制
    def LogOut_page(loginState):
        if loginState==1:
            func='page_not_login'
        elif loginState==2:
            func='page_logout'
        return func
    
    ##############################################
    
    #定义一个字典，保存各界面的func
    pagefunc_dict={}

    def ChooseFunc_login(pagefunc_dict):
        interface='Login'#interface为界面的名称
        login_func=login_page(pagestate_dict[interface])
        pagefunc_dict[interface]=login_func
        return pagefunc_dict

    def ChooseFunc_BasicPython(pagefunc_dict):
        interface = 'BasicPython'  # interface为界面的名称
        BasicPython_func = BasicPython_page(pagestate_dict['Login'],pagestate_dict[interface])
        pagefunc_dict['BasicPython'] = BasicPython_func
        return pagefunc_dict

    def ChooseFunc_LoopAndLogic(pagefunc_dict):
        interface = 'LoopAndLogic'  # interface为界面的名称
        LoopAndLogic_func = LoopAndLogic_page(pagestate_dict['Login'],pagestate_dict[interface])
        pagefunc_dict['LoopAndLogic'] = LoopAndLogic_func
        return pagefunc_dict

    def ChooseFunc_Function(pagefunc_dict):
        interface = 'Function'  # interface为界面的名称
        Function_func = Function_page(pagestate_dict['Login'],pagestate_dict[interface])
        pagefunc_dict['Function'] = Function_func
        return pagefunc_dict

    def ChooseFunc_Virtualization(pagefunc_dict):
        interface = 'Virtualization'  # interface为界面的名称
        Virtualization_func = Virtualization_page(pagestate_dict['Login'],pagestate_dict[interface])
        pagefunc_dict['Virtualization'] = Virtualization_func
        return pagefunc_dict

    def ChooseFunc_NumpAndPandas(pagefunc_dict):
        interface = 'NumpAndPandas'  # interface为界面的名称
        NumpAndPandas_func = NumpAndPandas_page(pagestate_dict['Login'],pagestate_dict[interface])
        pagefunc_dict['NumpAndPandas'] = NumpAndPandas_func
        return pagefunc_dict

    def ChooseFunc_Analysis(pagefunc_dict):
        interface = 'Analysis'  # interface为界面的名称
        Analysis_func = Analysis_page(pagestate_dict['Login'],pagestate_dict[interface])
        pagefunc_dict['Analysis'] = Analysis_func
        return pagefunc_dict
    
    def ChooseFunc_LogOut(pagefunc_dict):
        interface='LogOut'#interface为界面的名称
        LogOut_func=LogOut_page(pagestate_dict['Login'])
        pagefunc_dict['LogOut']=LogOut_func
        return pagefunc_dict
    
    pagefunc_dict=ChooseFunc_login(pagefunc_dict)
    pagefunc_dict=ChooseFunc_BasicPython(pagefunc_dict)
    pagefunc_dict=ChooseFunc_LoopAndLogic(pagefunc_dict)
    pagefunc_dict=ChooseFunc_Function(pagefunc_dict)
    pagefunc_dict=ChooseFunc_Virtualization(pagefunc_dict)
    pagefunc_dict=ChooseFunc_NumpAndPandas(pagefunc_dict)
    pagefunc_dict=ChooseFunc_Analysis(pagefunc_dict)
    pagefunc_dict=ChooseFunc_LogOut(pagefunc_dict)
    
    return pagefunc_dict

 #########################################################################   
#streamlit运行的主函数
pagefunc_dict=pageChooseFunc() 
system=MultiPages()

def add_page(title_name):
    func_name=pagefunc_dict[title_name]
    system.add_TitleAndFunc(title_name,func_name)
    
add_page('Login')
add_page('BasicPython')
add_page('LoopAndLogic')
add_page('Function')
add_page('Virtualization')
add_page('NumpAndPandas')
add_page('Analysis')
add_page('LogOut')

system.run()   
    
    
    