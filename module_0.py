#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,101)
    
    while number != predict:
        count+=1
        
        if number > predict + 90: 
            predict += 90
        elif number < predict - 90: 
            predict -= 90
            
        elif number > predict + 80: 
            predict += 80
        elif number < predict - 80: 
            predict -= 80

        elif number > predict + 70: 
            predict += 70
        elif number < predict - 70: 
            predict -= 70

        elif number > predict + 60: 
            predict += 60
        elif number < predict - 60: 
            predict -= 60

        elif number > predict + 50: 
            predict += 50
        elif number < predict - 50: 
            predict -= 50
        
        elif number > predict + 40: 
            predict += 40
        elif number < predict - 40: 
            predict -= 40
            
        elif number > predict + 30: 
            predict += 30
        elif number < predict - 30: 
            predict -= 30

        elif number > predict + 20: 
            predict += 20
        elif number < predict - 20: 
            predict -= 20
     
        elif number > predict + 10: 
            predict += 10
        elif number < predict - 10: 
            predict -= 10

        elif number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
            
    return count # выход из цикла, если угадали


print(game_core_v3(int(input())),'attempts to guess')


# In[ ]:




