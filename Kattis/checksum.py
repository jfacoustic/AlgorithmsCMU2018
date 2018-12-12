#!/usr/bin/env python3

# Joshua Mathews
# Theory of Algorithms 

# This solves Luhn's Checksum:
# https://open.kattis.com/problems/luhnchecksum
# It's a 1.7 difficulty problem.
# Much easier to analyze than the Mandelbrot problem.


T = int(input())

def CheckSum(n):
    N = []

    for i in range(len(n)):

        if (i+1) % 2 == 0:
            a = n[i] * 2

            if a > 9:
                d1 = a % 10
                d2 = (a - d1) / 10
                N.append(int(d1 + d2))
            else:
                N.append(a)

        else:
            N.append(n[i])

    s = 0
    for i in N:
        s += i

    if s % 10 == 0:
        return True
    else:
        return False


for _ in range(T):

    n = [int(s) for s in list(input())][::-1]

    if CheckSum(n) == True:
        print("Pass")
    else:
        print("Fail")
