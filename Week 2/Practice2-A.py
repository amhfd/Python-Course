#!/usr/bin/env python
# coding: utf-8

# In[25]:


#print prime numbers function
def primes(max):    
    min=2
    count= 1
    while(count<=(max)):
      for c in range(2, min):
        if min % c==0:
          break
      else:
        print (min)
        count +=1
      min=min+1
    
    
    


# In[27]:


primes(11)


