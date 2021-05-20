# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:59:12 2021

@author: BK
"""

#퍼셉트론
#x1w1 + x2w2 - θ > 0 then 1
#x1w1 + x2w2 - θ <= 0 then 0
# def AND(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1*w1 + x2*w2
#     if tmp <= theta:
#         return 0
#     elif tmp > theta:
#         return 1   

# print("x1 x2 θ"    )
# print("0  0 ", AND(0, 0))
# print("1  0 ", AND(1, 0))
# print("0  1 ", AND(0, 1))
# print("1  1 ", AND(1, 1))


#가중치와 편향도입
import numpy as np
# x = np.array([0,1])     #입력
# w = np.array([0.5,0.5]) #가중
# b = -0.7    #편향

# print("x*w=", x*w)
# print("np.sum(x*w)=", np.sum(x*w))
# print("np.sum(x*w)+b=", np.sum(x*w)+b)  #부동소수점 수에 의한 연산 오차

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
    
# print ("AND")
# print("0 0 =", AND(0,0))
# print("1 0 =", AND(1,0))
# print("0 1 =", AND(0,1))
# print("1 1 =", AND(1,1))

# print ("\nNAND")
# print("0 0 =", NAND(0,0))
# print("1 0 =", NAND(1,0))
# print("0 1 =", NAND(0,1))
# print("1 1 =", NAND(1,1))

# print ("\nOR")
# print("0 0 =", OR(0,0))
# print("1 0 =", OR(1,0))
# print("0 1 =", OR(0,1))
# print("1 1 =", OR(1,1))

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# print ("\nXOR")
# print("0 0 =", XOR(0,0))
# print("1 0 =", XOR(1,0))
# print("0 1 =", XOR(0,1))
# print("1 1 =", XOR(1,1))


#A, B, C_in, C_out(Carry), Sum
def Full_Adder(A, B, C_in):
    Sum = XOR(XOR(A, B), C_in) #Sum = (A xor B) xor C
    C_out = OR(AND(XOR(A, B), C_in), AND(A, B)) #C_out(carry) = ((A xor B) and C_in) or (A and B)
    return C_out, Sum