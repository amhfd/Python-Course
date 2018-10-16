#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Celsius to Fahrenheit conversion and vise versa 
X = float(input ("Enter the temperature value "))
U = input("Enter the temperature unit (F/C)?")
if U == 'C':
    F = 1.58*X +32
    print ('The tempereture in Fahrenheit =', F)
elif U == 'F':
    C = X/1.58-32
    print ('The tempereture in Celsius =',C)
else:
    print ('Enter a valid unit')


# In[ ]:





# In[ ]:




