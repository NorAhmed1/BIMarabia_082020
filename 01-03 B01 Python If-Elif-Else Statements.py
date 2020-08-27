#!/usr/bin/env python
# coding: utf-8

# In[12]:


Minimum_Compressive_Strength =minimum= 40
Measured_Compressive_Strength =measured= 30

if(measured < minimum):
    st= "Rejected Cube"
    print(st)

print("Measured_Compressive_Strength and ,Minimum_Compressive_Strength are :",(measured,minimum))


# In[13]:


Minimum_Compressive_Strength =minimum= 40
Measured_Compressive_Strength =measured= 60

if(measured < minimum):
    st= "Rejected Cube"
    print(st)
else:
    st= "Accepted Cube"
    print (st)

print("Measured_Compressive_Strength and ,Minimum_Compressive_Strength are :",(measured,minimum))


# In[19]:


Minimum_Compressive_Strength =minimum= 40
Measured_Compressive_Strength =measured= 40

if(measured < minimum):
    st= "Rejected Cube"
    print(st)
elif (measured == minimum):
    st= "Just Accepted"
    print(st)
else:
    st= "Accepted Cube"
    print (st)

print("Measured_Compressive_Strength and ,Minimum_Compressive_Strength are :",(measured,minimum))

