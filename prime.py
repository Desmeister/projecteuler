# -*- coding: utf-8 -*-
"""
ProjectEuler Prime Number Functions
Contains all helper functions related to primes and factorization
@author: dsisson
"""

import math

def gen_primes():
     """
     Generator for primes using the Sieve of Eratosthenes
     """
     D = {}
     q = 2
     while True:
          if q not in D:
               yield q
               D[q * q] = [q]
          else:
               for p in D[q]:
                    D.setdefault(p+q, []).append(p)
               del D[q]
          q+=1
          
def factorize(n, primes):
     """
     Calculates the factors of n given a list of primes
     
     primes - a list of primes up to n
     n - the number to factorize
     
     factors - a list representing powers of primes in the factored form
     """
     
     factors = [0]*len(primes)
     while n>1:
          for i, p in enumerate(primes):
               if((n%p)!=0):
                    continue
               n = n/p
               factors[i] += 1
     return factors

def isPrime(number, primes):
     """
     Checks if a number is prime, without giving a factorization
     
     number - the target number
     primes - a list of primes, the largest of which must be >= sqrt(n)
     """
     
     limit = int(math.sqrt(number))
     if(primes[-1]<limit):
          print("Primes up to sqrt(number) are required.")
          return False
     for prime in primes:
          if(prime>limit):
               break
          if(number%prime==0):
               return False
     return True

def primeFactors(number, primes):
     """
     Returns the prime factors of a number, but not their powers
     """
     
     factors = []
     for prime in primes:
          if(prime>number):
               break
          if(number%prime==0):
               factors.append(prime)
     return factors