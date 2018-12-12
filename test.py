#!/usr/bin/env python3
import secrets, random
import numpy as np
import matplotlib.pyplot as plt


# This compares random() to secret() where 
# secret() is cryptographically secure.
def randomTest():
    x = []
    y = []
    c = 0
    for i in range(10000):
        x.append(random.randint(0,9))
        #print(str(i) + " " + str(len(x)))
    for i in range(10):
        #print(str(i) + " " + str(x.count(i)))
        y.append(x.count(i))
        c += x.count(i)
    #print(c)
    #print(len(x))
    return(y)

def secretsTest():
    x = []
    y = np.empty([], dtype=int)
    c = 0
    for i in range(10000):
        x.append(secrets.randbelow(10))
    for i in range(10):
     #   print(str(i) + " " + str(x.count(i)))
        np.append(y, x.count(i))
        c += x.count(i)
    #print(c)
    return(y)

tot = [0] * 10
for i in range(1000):
    x = randomTest()
    #print(x)
    for j in range(10):
        tot[j] += x[j]
for i in range(10):
    print(tot[i] / 1000.)


print("\n")
secretsTest()


    
