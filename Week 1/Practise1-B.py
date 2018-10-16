#!/usr/bin/env python
# coding: utf-8

# In[19]:


#This code is for a piecewise function 
Num = int(input("Enter your number "))
if Num < (-100): 
    Num = -Num
elif Num >= -100 and Num <= (-25):
    Num = Num**4
elif Num > -25 and Num <= 0:
    Num = 3 * Num**2 - 1
elif Num > 0 and Num <= 100:
    Num = (22/7)/2*Num+3
else: 
    Num = Num 
print (Num)
# The suitable data type for F(x) is float. because some of the defined functions contains fractions.


# In[ ]:





# In[ ]:




