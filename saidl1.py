import numpy as np 
import matplotlib.pyplot as plt
c=5*10**(-6)
r=2*10**(3)
urest=0
tref=5*10**(-3)
v=1*10**(-3)
h=1*10**(-6)
w=(45/180)*3.14
w1=(45/180)*3.14
w2=(60/180)*3.14
w3=(30/180)*3.14
u_values=[]
il1=[]
il2=[]
il3=[]
il4=[]
for i in range(100000):
    z=0
    il1.append(z)
    il2.append(z)
    il3.append(z)
    il4.append(z)
    u_values.append(z)
for j in range(4999,74999):
    il1[j]=2*10*(-6)
for j in range(100000):
    il2[j]=1.5*10*(-6)
for j in range(100000):
    il3[j]=5*np.sin(w*i*10**(-3))
for j in range(100000):
    il4[j]=((-2)*np.sin(w1*i*10**(-3))+(3)*np.sin(w2*i*10**(-3))+np.cos(w3*i*10**(-3)))
fl1=plt.plot(il1)
fl2=plt.plot(il2)
fl3=plt.plot(il3)
fl4=plt.plot(il4)
for i in range(99999):
    f=(-u_values[i]+il[i]*r)/(r*c)
    u_values[i+1]=u_values[i] +h*f
    if(u_values[i]>=v):
        tf=i
        break
i=0
while(i<10000):
    
    for i in range(tf+4998,99999):
        f=(-u_values[i]+il[i]*r)/(r*c)
        u_values[i+1]=u_values[i] +h*f
        if(u_values[i]>=v):
            tf=i
            i=0
            break
fig1=plt.plot(u_values)
for i in range(100000):
    u_values.append(z)
for i in range(99999):
    f=(-u_values[i]+il[i]*r)/(r*c)
    u_values[i+1]=u_values[i] +h*f
    if(u_values[i]>=v):
        tf=i
        break
i=0
while(i<10000):
    
    for i in range(tf+4998,99999):
        f=(-u_values[i]+il[i]*r)/(r*c)
        u_values[i+1]=u_values[i] +h*f
        if(u_values[i]>=v):
            tf=i
            i=0
            break
fig2=plt.plot(u_values)
for i in range(100000):
    u_values.append(z)
for i in range(99999):
    f=(-u_values[i]+il[i]*r)/(r*c)
    u_values[i+1]=u_values[i] +h*f
    if(u_values[i]>=v):
        tf=i
        break
i=0
while(i<10000):
    
    for i in range(tf+4998,99999):
        f=(-u_values[i]+il[i]*r)/(r*c)
        u_values[i+1]=u_values[i] +h*f
        if(u_values[i]>=v):
            tf=i
            i=0
            break
fig3=plt.plot(u_values)
for i in range(100000):
    u_values.append(z)
for i in range(99999):
    f=(-u_values[i]+il[i]*r)/(r*c)
    u_values[i+1]=u_values[i] +h*f
    if(u_values[i]>=v):
        tf=i
        break
i=0
while(i<10000):
    
    for i in range(tf+4998,99999):
        f=(-u_values[i]+il[i]*r)/(r*c)
        u_values[i+1]=u_values[i] +h*f
        if(u_values[i]>=v):
            tf=i
            i=0
            break
fig4=plt.plot(u_values)

ci=[]
totcount=[]
for consti in range(100):
    ci.append(consti*10*(-6))
    for i in range(100000):
    u_values.append(z)
    for i in range(99999):
        f=(-u_values[i]+il[i]*r)/(r*c)
        u_values[i+1]=u_values[i] +h*f
        if(u_values[i]>=v):
            tf=i
            break
    i=0
    while(i<10000):
    
        for i in range(tf+4998,99999):
            f=(-u_values[i]+il[i]*r)/(r*c)
            u_values[i+1]=u_values[i] +h*f
            if(u_values[i]>=v):
                tf=i
                i=0
                break
    for i in u_values:
        count=0
        if(u_values[i]>=v):
            count=count+1
        totcount.append(count)
figi=plt.plot(totcount)
plt.show()

    
    








    



