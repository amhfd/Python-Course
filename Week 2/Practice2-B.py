#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Currency convergion function 
def covert() :
    fr = int(input("Choose currency to convert from \n"+"1. USD \n"+"2. JOD \n"+"3. TRY \n"))
    while fr >5 or fr <= 0 :
         print ("Invalid entry")
         fr = int(input("Choose currency to convert from \n"+"1. USD \n"+"2. JOD \n"+"3. TRY \n"))
    to = int(input("Choose currency to convert to \n"+"1. USD \n"+"2. JOD \n"+"3. TRY \n"))
    while to >5 or to <= 0 :
        print ("Invalid entry")
        to = int(input("Choose currency to convert to \n"+"1. USD \n"+"2. JOD \n"+"3. TRY \n"))
    value = int(input("Enter the currency amount:"))
    listUSD = [1,.709,.564]
    listJOD = [1.41,1,.7096]
    listTRY = [.177,.126,1]
    listA = [listUSD,listJOD,listTRY]
    print(value*listA[fr-1][to-1])


# In[14]:


covert()


# In[ ]:




