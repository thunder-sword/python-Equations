#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sympy import solve,Symbol 
#解方程组小程序v2.0-thunder-sword
#添加了自动分析变量的代码，现在输入只需要输入方程组便可以得到结果


bianliang=[]
print('请输入方程组中所有的方程：')
fangcheng=[]
while True:
    string2=input()
    if string2=='':
        break
    #自动读入分析变量名
    temp_bianliang=''
    flag_1 = False
    for i in range(len(string2)):
        if flag_1==False and string2[i].isalpha():
            temp_bianliang+=string2[i]
            flag_1=True
        elif flag_1:
            if string2[i].isalnum():
                temp_bianliang += string2[i]
            else:
                if temp_bianliang not in bianliang:
                    bianliang.append(temp_bianliang)
                temp_bianliang=''
                flag_1=False
    if flag_1:
        if temp_bianliang not in bianliang:
            bianliang.append(temp_bianliang)
        temp_bianliang = ''
        flag_1 = False
    #将bianliang元组中的所有变量初始化
    for eachbianliang in bianliang:
        exec("{0}=Symbol('{0}')".format(eachbianliang))
    #处理等于号，使第一个等号变为减号，等号右边被括号括住被减
    ind = string2.find('=')
    if ind!=-1:
        string2=string2[:ind]+'-('+string2[ind+1:]+')'
    #如果方程式中的变量前面是数字，手动添加乘号*
    for i in bianliang:
        ind2=string2.find(i.strip())
        while ind2!=-1:
            if ind2!=-1 and ind2!=0 and string2[ind2-1].isdigit():
                string2=string2[:ind2]+'*'+string2[ind2:]
            ind2=string2.find(i.strip(),ind2+1)
    #将^号切换为**，以便指数运算
    string2=string2.replace('^','**')
    fangcheng.append(eval(string2))

ans_solve=solve(fangcheng, bianliang)
if isinstance(ans_solve,list):
    print(bianliang,'=',ans_solve,end='\n\n')
    for i in range(len(bianliang)):
        print(bianliang[i],':',end=' ')
        for j in range(len(ans_solve)):
            if j!=0:
                print(',',end='')
            print(ans_solve[j][i],end='')
        print()
elif isinstance(ans_solve,dict):
    for k,v in ans_solve.items():
        print(k,':',v)
