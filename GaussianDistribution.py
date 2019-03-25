import numpy as np

T=100
N = 10000
m = 10000
s = 1000
w=0
j=0
q = np.ones(T)

while (j<T):
    i = 0
    a = 0
   
    x = np.ones(N)

    while (i<N):
        y = np.random.normal(loc = m,scale = s, size = 1)
        x[i] = y
        if ((x[i]<m-3*s)or(x[i]>m+3*s)):
            x[i]=0
            a=a+1
            i=i+1
        else:
            i=i+1
                   
    p=a/N*100
    q[j]=p
    w= w + q[j]
    j=j+1
    
e=w/T
print(e)
    

    


