# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:50:19 2021

@author: BK
"""

class Main:
    def __init__(self, name):
        self.name = name
        print("Init!")
        
    def hello(self):
        print("hello" , self.name , "!")
        
    def goodby(self):
        print("Good by" , self.name , "!")
        
m = Main("홍길동")
m.hello()
m.goodby()