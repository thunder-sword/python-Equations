#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sympy import solve,Symbol 
#解方程组小程序v0.4-thunder-sword
#处理了输出内容，使其整齐化
#因为solve函数返回值有可能为列表，有可能为字典，所以要用isinstance函数判断

print('请输入方程组中所有的变量名：')
bianliang=[]
while true:
    string=input()
    if string=='':
        break
    bianliang.append(string)
    exec("{0}=Symbol('{0}')".format(string))
print('请输入方程组中所有的方程：')
fangcheng=[]
while true:
    string2=input()
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
    #print(string2)
    if string2=='':
        break
    fangcheng.append(eval(string2))

#print(fangcheng)
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