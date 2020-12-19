import numpy as np



def bern_sim(n, p):
    if p>1 or p <0 or not isinstance(n,int):
        return -1
    vic = 0
    form = 0
    for i in range(n):
        form += p**(int(i)+1) * (1-p)**(n-int(i)+1)
    return form*n

print(bern_sim(100,0.9))
