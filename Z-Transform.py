import numpy as np
j=0
#Fool proof input
while (j<1):
    h = int(input('Please enter the highest k value '))
    l = int(input('Please enter the lowest k value '))
    if (h > l):
        j=j+1
    else:
        continue
R=h-l
j=0
x = np.ones(R)
print("Please enter the function values for all values of k from lowest to highest = ")
print('[',end='')
while (j<R-1):
    x[j] = int(input())
    print(', ',end='') 
x[j] = int(input(end=''))
print(']')
i=l


while(i<h):
    print('%f * z^-%f + '%(x[i-l],i))
    i=i+1

    
