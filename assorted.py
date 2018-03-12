# -*- coding: utf-8 -*-
"""
Assorted Helper Functions
@author: dsisson
"""

def rotate(n):
     """
     Takes the last digit of a number and moves it to the front
     """
     
     if(n<10):
          return n
     n = str(n)
     n = n[-1] + n[:-1]
     n = int(n)
     return n

def gen_triangle():
     """
     Generator for triangular numbers
     """
     
     n = 1
     while True:
          yield int((n)*(n+1)/2)
          n += 1

def gen_pentagon():
     """
     Generator for pentagonal numbers
     """
     n = 1
     while True:
          yield int((n)*((3*n)-1)/2)
          n += 1
          
def gen_hexagon():
     """
     Generator for hexagonal numbers
     """
     n = 1
     while True:
          yield int((n)*((2*n)-1))
          n += 1

def gen_dblSqr():
     """
     Generator for double the squares of positive integers
     """
     
     n = 1
     while True:
          yield 2*n*n
          n += 1