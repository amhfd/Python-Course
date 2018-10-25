#!/usr/bin/env python
# coding: utf-8

# In[2]:


gov = ['Irbid', 'Ajloun', 'Jerash', 'Mafraq', 'Balqa', 'Madaba', 'Amman', 'Zarqa', 'Karak', 'Tafila', 'Maan','Aaqba']
print ("states that starts with the letter ‘A’")
for i in gov:
    if i.startswith("A") :
        print (i)
print ("states that has 5 letters only")        
for i in gov:
    if  len(i) == 5:
        print (i)

