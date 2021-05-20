# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:01:43 2021

@author: BK
"""

#퍼셉트론
#가중치와 편향도입
import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2])     #입력
    w = np.array([0.5,0.5]) #가중
    b = -0.7    #편향
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


def NAND(x1, x2):
    x = np.array([x1,x2])     #입력
    w = np.array([-0.5,-0.5]) #가중
    b = 0.7    #편향
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
    
def OR(x1, x2):
    x = np.array([x1,x2])     #입력
    w = np.array([0.5,0.5]) #가중
    b = -0.2    #편향
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

#A, B, C_in, C_out(Carry), Sum
def Full_Adder(A, B, C):
    Sum = XOR(XOR(A, B), C) #Sum = (A xor B) xor C
    Carry = OR(AND(XOR(A, B), C), AND(A, B)) #C_out(carry) = ((A xor B) and C_in) or (A and B)
    return "Full_Adder Input({0}, {1}, {2}) →→ Carry : Sum = {3} : {4}".format(str(A), str(B), str(C), str(Carry), str(Sum))

# 모든 결과 출력
print((Full_Adder(0, 0, 0)))
print((Full_Adder(0, 1, 0)))
print((Full_Adder(1, 0, 0)))
print((Full_Adder(1, 0, 1)))
print((Full_Adder(1, 1, 0)))
print((Full_Adder(0, 1, 1)))
print((Full_Adder(1, 1, 1)))

