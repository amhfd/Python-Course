#!/usr/bin/env python
# coding: utf-8

# In[18]:


"""
This code Read one name and two numbers, and then print the name with any 
greeting and prints out the addition, subtraction, multiplication,
division, the reminder of division of first number over the other, the 
exponent of first to the other. 
"""
user_input = input("Enter your name: ")
num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
print('Hi Mr/Mrs '+ user_input)
print ("The Sum of "+ num_1 + ' and ' + num_2 + ' is:', int(num_1)+ int(num_2))
print ("The Sub of "+ num_1 + ' and ' + num_2 + ' is:', int(num_1)- int(num_2))
print ("The Mul of "+ num_1 + ' and ' + num_2 + ' is:', int(num_1)* int(num_2))
print ("The Div of "+ num_1 + ' over ' + num_2 + ' is:', int(num_1)/ int(num_2))
print ("The Reminder of "+ num_1 + ' over ' + num_2 + ' is:', int(num_1)% int(num_2))
print ("The Exponent of "+ num_1 + ' to ' + num_2 + ' is:', int(num_1)**int(num_2))


# In[ ]:




