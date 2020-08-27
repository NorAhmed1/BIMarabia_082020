#!/usr/bin/env python
# coding: utf-8

# In[2]:


# The for loop example
Concrete_Components = ['water', 'sand', 'gravel','cement']
for Component in Concrete_Components:
    print(Component)


# In[6]:


# The While loop example
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")


# In[10]:


# The While loop example 2
Concrete_Components = ['water', 'sand', 'gravel','cement']
Component = 0
while (Component < len(Concrete_Components)):
    print (Concrete_Components[Component])
    Component = Component +1


# In[2]:


# Using else Statement with While Loop
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


# In[6]:


#The Python break and continue Statement  https://realpython.com/python-while-loop/
n = 15
while n > 0:
    n -= 1
    if n == 6:
        break
    print(n)
print('Loop ended.')


# In[7]:


#The Python continue Statement  https://realpython.com/python-while-loop/
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')


# In[10]:


# The  while  else Clause
n = 5
while n > 0:
     n -= 1
     print(n)
else:
     print('Loop done.')


# In[ ]:




