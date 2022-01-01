#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star,");
print("         How I wonder what you areI");
print("               Up above the world so high");
print("               Like a diamond in the sky.");
print("Twinkle, twinkle, little star,");
print("         How I wonder what you areI");


# In[2]:


import sys
print("Python version");
print(sys.version);
print("Version info");
print(sys.version_info);


# In[4]:


from datetime import date
today = date.today();
print("Today date is", today);


# In[6]:


from math import pi
r = float(input("Input the radius of the circle"));
print("The area of the circle radius" + str(r) + " is" + str(pi*r**2));


# In[8]:


fname = input("Input your First name");
lname = input("Input your last name");
print("Hi " + lname + " " + fname);


# In[11]:


num1 = int(input("Input first number"));
num2 = int(input("Input second number"));
a = num1 + num2
print("Sum is:", a);


# In[ ]:




