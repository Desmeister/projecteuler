# -*- coding: utf-8 -*-
"""
Pandigital and other digit-related helper functions
@author: dsisson
"""

def pandigital(number, n):
     """
     Determines if a number of length "n" is 1 to n pandigital.
     """
     
     if(n>9):
          print("Numbers longer than 9 digits cannot be pandigital.")
          return False
     digits = [int(d) for d in str(number)]
     if(len(digits)<n or len(digits)>n):
          return False
     count = [0]*n
     for i in range(len(digits)):
          if(digits[i]>n or digits[i]==0):
               return False
          count[digits[i]-1] += 1
     for k in range(n):
          if count[k]!=1:
               return False
     return True

def makePandig(digits):
     """
     Recursively creates a list of all n-digit pandigital numbers, in ascending
     order
     
     digits - Number of digits in the pandigitals
     """
     
     if(len(digits)==2):
          return [digits[0]+digits[1],digits[1]+digits[0]]
     elif(len(digits)<2):
          print("Requires at least 2 digits.")
          return digits
     else:
          panList = []
          for i in range(len(digits)):
               oneOut = list(digits)
               del oneOut[i]
               subList = makePandig(oneOut)
               for number in subList:
                    number = digits[i] + number
                    panList.append(number)
          return panList

def nConcat(base, n):
     """
     Concatenates multiples of a number together
     
     base - the number we are multiplying
     n - the largest multiple to concatenate
     
     out - a string of the concatenation
     """
     out = ""
     for i in range(1,n+1):
          out = out+str(base*i)
     return int(out)

def isUnique(number, n):
     """
     Determines if a number has n unique digits
     """
     
     digits = [int(d) for d in str(number)]
     if(len(digits)<n-1):
          return False
     if(len(digits)==n-1):
          digits.insert(0,0)
     for i in range(len(digits)):
          for j in range(i+1,len(digits)):
               if(digits[i]==digits[j]):
                    return False
     return True

def uniqueMult(num):
     """
     Gives all 3-digit multiples of a number that possess unique digits
     """
     
     out = [str(x*num) for x in range(1,int(1000/num)+1)]
     i = 0
     while(i < len(out)):
          if(int(out[i])<10):
               out[i] = '00' + out[i]
          elif(int(out[i])<100):
               out[i] = '0' + out[i]
          if(isUnique(out[i],3)==False):
               del out[i]
          else:
               i += 1
     return out

def equalDigits(n1, n2):
     """
     Checks if numbers n1 and n2 have the same digits, a.k.a are anagrams
     """
     
     d1 = [int(d) for d in str(n1)]
     d2 = [int(d) for d in str(n2)]
     if(len(d1)!=len(d2)):
          return False
     length = len(d1)
     count1 = [0]*10
     count2 = [0]*10
     for i in range(length):
          count1[d1[i]] += 1
          count2[d2[i]] += 1
     for i in range(10):
          if(count1[i]!=count2[i]):
               return False
     return True