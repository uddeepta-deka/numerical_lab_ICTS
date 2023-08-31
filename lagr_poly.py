#!/usr/bin/env python
# coding: utf-8

# In[1]:


#this program finds the lagrange's nth order polynomial
def lagrange(xlist,ylist,x):
    Ln=[]
    P=0.0
    n=len(xlist)-1             #n is the order of polynomial, i.e. (total number of terms-1)
    for k in range (n+1):      #kth lagrange multiplier (n of such in total)
        a=1.0
        for i in range (n+1):  
            if (i!=k):
                a=a*(x-xlist[i])/(xlist[k]-xlist[i])
        Ln.append(a)
    for i in range (n+1):
        P=P+(ylist[i]*Ln[i])
    return P

#def f(x):
#    y=[]
#    for i in range (len(x)):
#        y.append(1.0/x[i])
#    return y

#x=([2.0,2.75,4.0])
#y=f(x)
#z=lagrange(x,y,4)
#print (z)





