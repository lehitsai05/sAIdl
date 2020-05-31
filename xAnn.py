import numpy as np
bit1=[1,1,0,0]
bit2=[1,0,1,0]
weights1=[[20,20],[-20,-20]]
weights2=[20,20]
bias1=[-30,10]
bias2=-10
x=input("enter 0/1 : ")
h1=[]
for j in range(2):
    a1=[]
    for i in range(4):
        o=0
        o+=bit1[i]*weights1[j][0]+bit2[i]*weights1[j][1]
        o+=bias1[j]
        if(o>0):
            a=1
        else:
            a=0
        a1.append(a)
    h1.append(a1)
print(h1)
a2=[]
for i in range(4):
    o=0
    o+=h1[0][i]*weights2[0] +h1[1][i]*weights2[1]
    o+=bias2
    print(o)
    if(o>0):
            a=1
    else:
            a=0
    a2.append(a)
a3=[]
for i in a2:
    j=-20*int(x)+ 20*i
    if(int(j)==0):
        i=0
    else:
        i=1
    a3.append(i)
print(a3)



