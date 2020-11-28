# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:33:10 2020

@author: Administrator
"""
import random
dict1={'Tên':'','Tuổi':''}
chu = ['a','b','c','d','e','f','g','h','i','j','k','l',
       'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
tuoi = random.randint(1,101)
x = random.randint(1,10)  
ten=''
for i in range(0,x):
     i = random.randint(0,len(chu))
     ten=ten+chu[i]
dict1['Tên']=ten
dict1['Tuổi']=tuoi
print(dict1)


    
    
     