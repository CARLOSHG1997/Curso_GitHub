#!/usr/bin/env python
# coding: utf-8

# Resolver EDO 
# y´=x/(x+2)*y 

# In[12]:


np.zeros(4)


# In[17]:


np.ones((3,3))


# In[19]:


x = np.linspace(0,3.5,50)
y = np.zeros(x.shape)


# In[22]:


L=['a','b','c','d']
for i in range(0,len(L)):
    print(i,L[i])


# In[26]:


for i,val in enumerate(L):
    print(i,val)


# In[29]:


arr=np.linspace(0,1,5)
new_arr=np.zeros(arr.shape)
print(f'Array sin modificaciones{new_arr}')
for i, val in enumerate(arr):
    new_arr[i]=val*2
    print(f'Valor del array en posicion {i},{new_arr}')
print(f'Array modificado{new_arr}')
    


# In[32]:


import numpy as np
from scipy.integrate import quad

a=0
b=3

x1=1
def p(x):
    return -x/(x+2)
I,err=quad(p,a,x1)
print(f'El valor de la integral es{I:1.2f}')
y1 = b*np.exp(-I)

print(f'El avlor de la ecuación diferencial es {y1:1.2f}')


# In[42]:


a=0
b=3

x =np.linspace(0,3.5)
y=np.zeros(x.shape)
def p(x):
    return -x/(x+2)
for i,val in enumerate(x):
    I,__=quad(p,a,val)
    y[i]=b*np.exp(-I)
    
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.plot(x,y)


# In[60]:


derivada=np.gradient(y,x,edge_order=2)

plt.plot(x,derivada,'ro--',label='numerico')
plt.plot(x,x/(x+2)*y,'b',label='analitico')
plt.legend()


# In[ ]:




