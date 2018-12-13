#!/usr/bin/env python3
import secrets, random
import numpy as np
import matplotlib.pyplot as plt


# This compares random() to secret() where
# secret() is cryptographically secure.
def randomTest(n):
    x = np.empty([n])
    y = np.empty([10])
    index = []
    for i in range(10):
        index.append(i)
    print(index)
    for i in range(n):
        x[i] = random.randint(0,9)
    unique, counts = np.unique(x, return_counts=True)
    dist = dict(zip(unique, counts))
    count = 0
    for i in range(10):
        y[i] = dist[i]
        count += y[i]
    print(y)
    print(count/10)
    plt.bar(index,y)
    plt.show()

def secretsTest(n):
    x = np.empty([n])
    y = np.empty([10])
    index = []
    for i in range(10):
        index.append(i)
    print(index)

    for i in range(n):
        x[i] = secrets.randbelow(10)
    unique, counts = np.unique(x, return_counts=True)
    dist = dict(zip(unique,counts))

    count = 0
    for i in range(10):
        y[i] = dist[i]
        count += y[i]
    print(y)
    print(count/10.)
    plt.bar(index,y)
    plt.show()

randomTest(100)
secretsTest(100)
