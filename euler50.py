# -*- coding: utf-8 -*-
"""
ProjectEuler Python
Selections from Questions 1-50
@author: dsisson
"""

# Imports
import math
import bisect

# Local Imports
from prime import gen_primes, factorize, isPrime, primeFactors
from pandig import pandigital, makePandig, nConcat, uniqueMult, equalDigits
from assorted import rotate, gen_triangle, gen_pentagon, gen_hexagon, gen_dblSqr


def p22():
     """
     Import the file, convert to name scores, find the largest
     """
     
     PATH = "C:\\Users\\dsisson\\Documents\\Python Scripts\\p022_names.txt"
     file = open(PATH,'r')
     names = file.read()
     file.close()
     names = names.split(",")
     names = [i.replace('"', '') for i in names]
     names.sort()
     
     total = 0
     for i in range(len(names)):
          score = 0
          for j in range(len(names[i])):
               score += ord(names[i][j]) - 64
          total += score * (i+1)
     print(total)

def p26():
     """
     Implement the long division algorithm and look for repeated remainders to
     identify cycles
     """
     
     maxLen = 0
     index = 0
     MAX_IDX = 1000
     for i in range(1,MAX_IDX):
          count = 0
          remainders = [0]
          subFrom = 1
          cycleSize = 0
          while(count < MAX_IDX):
               subFrom = subFrom*10
               if(i>subFrom):
                    remainders.append(0)
                    count += 1
               else:
                    rem = subFrom%i
                    for j in range(len(remainders)):
                         if(remainders[j]==rem):
                              cycleSize = len(remainders)-j
                              count = MAX_IDX
                         else:
                              pass
                    remainders.append(rem)
                    subFrom = rem
                    count += 1
          if(cycleSize > maxLen):
               maxLen = cycleSize
               index = i
     print("Cycle of length",maxLen,"from reciprocal of",index)

def p29():
     """
     To factorize (A^B), factorize A then multiply the prime powers by B. Store
     the factorizations and check for uniqueness
     """
     
     primeList = []
     prime = gen_primes()
     p = next(prime)
     while(len(primeList)<100):
          primeList.append(p)
          p = next(prime)
     factorSet = []
     for base in range(2,101):
          for power in range(2,101):
               factors = factorize(base,primeList)
               for i in range(len(factors)):
                    factors[i] *= power
               unique = 1
               for i in range(len(factorSet)):
                    match = 1
                    for j in range(len(factorSet[i])):
                         if factorSet[i][j] != factors[j]:
                              match = 0
                              break
                    if(match):
                         unique = 0
                         break
               if(unique):
                    factorSet.append(factors)
     print(len(factorSet))

def p31():
     """
     Recursively compute the number of ways by introducing coins one at a time
     """
     
     coins = [1,2,5,10,20,50,100,200]
     coinWays = [1] + [0]*200
     for coin in coins:
          for i in range(coin, 201):
               coinWays[i] += coinWays[i-coin]
     print(coinWays[200])

def p32():
     """
     Using a 1-2 digit i and a 2-4 digit j, finds all pandigital products
     """
     
     products = []
     for i in range(1,100):
          for j in range(100,10000):
               prod = i*j
               if(prod>=10000):
                    continue
               if(pandigital(int(str(i)+str(j)+str(prod)))):
                    print(i, "*", j, "=", prod)
                    products.append(prod)
     products = list(set(products))
     print("Sum:",sum(products))
     return

def p33():
     """
     Brute force all two-digit fractions and combinations of digit cancelling
     """
     
     numers = []
     denoms = []
     for i in range(11,100):
          if(i%10==0):
               continue
          for j in range(i+1,100):
               if(j%10==0):
                    continue
               iDig = [int(_) for _ in str(i)]
               jDig = [int(_) for _ in str(j)]
               if(iDig[0]==jDig[0]):
                    if((i/j)==(iDig[1]/jDig[1])):
                         numers.append(i)
                         denoms.append(j)
               if(iDig[0]==jDig[1]):
                    if((i/j)==(iDig[1]/jDig[0])):
                         numers.append(i)
                         denoms.append(j)
               if(iDig[1]==jDig[0]):
                    if((i/j)==(iDig[0]/jDig[1])):
                         numers.append(i)
                         denoms.append(j)
               if(iDig[1]==jDig[1]):
                    if((i/j)==(iDig[0]/jDig[0])):
                         numers.append(i)
                         denoms.append(j)
     numer, denom = 1, 1
     for i in numers:
          numer *= i
     for i in denoms:
          denom *= i
     denom /= math.gcd(numer,denom)
     print(denom)
               
     return

def p35():
     """
     Removes primes with even numbered digits, then check all "rotations" of
     the prime for primality
     """
     
     primes = []
     prime = gen_primes()
     p = next(prime)
     while(p<1000000):
          primes.append(p)
          p = next(prime)
     
     cPrimes = []
     for p in primes:
          strP = str(p)
          oddFlag = True
          for dig in strP:
               if int(dig) in (0,2,4,6,8):
                    oddFlag = False
                    break
          if(oddFlag==False):
               continue
          cFlag = True
          p_2 = p
          for _ in range(len(str(p))):
               p_2 = rotate(p_2)
               if p_2 not in primes:
                    cFlag = False
                    break
          if(cFlag==True):
               cPrimes.append(p)
     cPrimes.append(2)
     print(len(cPrimes))
     print(cPrimes)
     
def p36():
     """
     Casts to a string and runs backwards to check for palindromes
     """
     
     palins = []
     for i in range(1,1000001):
          b2 = str(bin(i)[2:])
          b10 = str(i)
          if(b2[::-1]==b2 and b10[::-1]==b10):
               palins.append(i)
     print(sum(palins))
     return

def p37():
     """
     Keeps testing all primes for truncation until an 11th is found
     """
     
     primes = []
     truncPrimes = []
     prime = gen_primes()
     p = next(prime)
     while(len(truncPrimes)<11):
          primes.append(p)
          p = next(prime)
          if(primes[-1]<10):
               continue
          newPrime = primes[-1]
          truncatable = True
          while(newPrime>10):
               newPrime = str(newPrime)
               newPrime = newPrime[:-1]
               newPrime = int(newPrime)
               if(newPrime in primes):
                    continue
               truncatable = False
          newPrime = primes[-1]
          while(newPrime>10):
               newPrime = str(newPrime)
               newPrime = newPrime[1:]
               newPrime = int(newPrime)
               if(newPrime in primes):
                    continue
               truncatable = False
          if(truncatable==True):
               truncPrimes.append(primes[-1])
     print(truncPrimes)
     print(sum(truncPrimes))
          
     return

def p38():
     """
     Brute force search, using the nConcat and pandigital helper functions
     """
     
     largest = 0
     for i in range(1,9999):
          for j in range(2,6):
               concat = nConcat(i,j)
               if(len(str(concat))==9):
                    if(pandigital(concat, 9)==True):
                         if(concat>largest):
                              largest=concat
               elif(len(str(concat))>9):
                    break
     print(largest)
     return

def p40():
     """
     Just convert each integer to digits and count them until a power of 10
     """
     
     n = 1
     product = 1
     targets = [10**i for i in range(7)]
     for i in range(1,1000000):
          if(n>1000000):
               break
          number = str(i)
          for digit in number:
               if(n in targets):
                    print(n, " ", digit)
                    product *= int(digit)
               n += 1
     print(product)
     return
          
def p41():
     """
     Because of the properties of divisibility by 3, we only need to check up
     to 7 digits. Generate primes and pandigitals up to this range, and search
     """
     
     prime = gen_primes()
     primes = []
     p = 0
     while(p<=int(math.sqrt(7654321))):
          p = next(prime)
          primes.append(p)
     digits = ['1','2']
     largest = 0
     for i in range(3,9):
          pandigits = makePandig(digits)
          for j in range(len(pandigits)):
               pandigits[j] = int(pandigits[j])
               if(isPrime(pandigits[j],primes)==True):
                    largest = pandigits[j]
          digits.append(str(i))
     print(largest)
     return

def p42():
     """
     Read the words, and compare them to generated triangle numbers
     """
     
     PATH = "C:\\Users\\dsisson\\Documents\\Python Scripts\\p042_words.txt"
     file = open(PATH,'r')
     words = file.read()
     file.close()
     words = words.split(",")
     words = [i.replace('"', '') for i in words]
     triangle = [int((i+1)*(i/2)) for i in range(1,30)]
     count = 0
     for word in words:
          wrdSc = 0
          for letter in word:
               wrdSc += (ord(letter)-64)
          if(wrdSc in triangle):
               count += 1
     print(count)
     return
     
def p43():
     """
     Determine each set of 3 digits that satisfies each condition,
     and stitch them together when the digits are unique
     """
     primes = [13,11,7,5,3,2]
     combined = uniqueMult(17)
     for p in primes:
          newCombined = []
          nextPrime = uniqueMult(p)
          for i in nextPrime:
               for j in combined:
                    if(i[1:3]==j[0:2] and (i[0] not in j)):
                         newCombined.append(i[0]+j)
          combined = newCombined
     digits = ['0','1','2','3','4','5','6','7','8','9']
     for d in digits:
          for i in range(len(combined)):
               if(d not in combined[i]):
                    combined[i] = d + combined[i]
                    continue
     #None of them were missing '0', so no problems
     combined = [int(x) for x in combined]
     print(sum(combined))
     return

def p44():
     """
     Continually generate pentagonal numbers. When (p1 - p2) = p3 is found,
     store (p1 + p2) to check if it is pentagonal once the numbers are that size
     """
     
     pentagon = gen_pentagon()
     p = 0
     pentList = []
     unchkSums = []
     found = 0
     while True:
          p = next(pentagon)
          pentList.append(p)
          if(unchkSums):
               if(p >= unchkSums[0]):
                    if(unchkSums[0] in pentList):
                         found = p
                         break
                    else:
                         del unchkSums[0]
          for pent in pentList:
               if(p-pent in pentList):
                    bisect.insort(unchkSums,p+pent)
                    
     for i in range(len(pentList)):
          for j in range(i+1,len(pentList)):
               if(pentList[i]+pentList[j]==found):
                    if((pentList[j]-pentList[i]) in pentList):
                         print(pentList[j]-pentList[i])
     
     return

def p45():
     """
     Search for pentagon-hexagon matches, then compare against triangle
     """
     triangle = gen_triangle()
     t = next(triangle)
     t = next(triangle)
     pentagon = gen_pentagon()
     p = next(pentagon)
     p = next(pentagon)
     hexagon = gen_hexagon()
     h = next(hexagon)
     h = next(hexagon)
     ph = [1]
     tph = [1]
     while(len(tph)<3):
          if(p>h):
               h = next(hexagon)
          elif(p==h):
               ph.append(p)
               while(t<ph[-1]):
                    t = next(triangle)
               if(t==ph[-1]):
                    tph.append(t)
               h = next(hexagon)
          else:
               p = next(pentagon)
     print(tph)
     return

def p46():
     """
     Generate all primes and double dquares up to n, and test all composite n
     """
     
     prime = gen_primes()
     square = gen_dblSqr()
     p = next(prime)
     s = next(square)
     primes = []
     primes.append(p)
     squares = []
     squares.append(s)
     n = 9
     while True:
          while(primes[-1]<n):
               p = next(prime)
               primes.append(p)
          while(squares[-1]<n):
               s = next(square)
               squares.append(s)  
          partition = False
          if(n in primes):
               n+=2
               continue
          for i in primes:
               target = n-i
               idx = bisect.bisect(squares, target)
               if squares[idx-1] == target:
                    partition = True
                    break
          if(partition==False):
               break
          n += 2
          
     print(n)
     return

def p47():
     """
     Keep a running count of the number of factors, wait until 4 in a row with
     4 factors are found
     """
     
     prime = gen_primes()
     primes = [next(prime)]
     i = 2
     count = 0
     while True:
          if(primes[-1]<i):
               primes.append(next(prime))
          if(len(primeFactors(i, primes))==4):
               count += 1
          else:
               count = 0
          if(count==4):
               print(i-3)
               break
          i += 1
     return

def p49():
     """
     Generate all 4 digit primes, and look at pairs (a, a+d) which are anagrams
     to test if (a+2d) also is prime and has the same digits
     """
     
     # Generate 4 digit primes, compare pairs for arithmetic sequences
     prime = gen_primes()
     p = next(prime)
     primes = []
     while(p<1000):
          p = next(prime)
     while(p<10000):
          primes.append(p)
          p = next(prime)
     
     for i in range(len(primes)):
          for j in range(i+1,len(primes)):
               if(equalDigits(primes[i],primes[j])==False):
                    continue
               diff = primes[j] - primes[i]
               for k in range(j+1,len(primes)):
                    if(primes[k]==primes[j]+diff):
                         if(equalDigits(primes[j],primes[k])==True):
                              print(primes[i],primes[j],primes[k])
     return

def p50():
     """
     Test all (start,stop) indices, but do it faster by keeping track of the
     longest sequence so far (lRun), and beginning stop at (start + lRun)
     """
     
     LIMIT = math.pow(10,6)
     prime = gen_primes()
     primes = []
     p = 0
     while(p<=LIMIT):
          p = next(prime)
          primes.append(p)
     lRun= 0
     lSum = 0
     for i in range(len(primes)):
          for j in range(i+lRun,len(primes)):
               newSum = sum(primes[i:j])
               if(newSum>=LIMIT):
                    break
               if(newSum in primes):
                    if((j-i)>lRun):
                         lRun = (j-i)
                         lSum = sum(primes[i:j])
     print(lRun,"primes in a row with sum",lSum)
     return
