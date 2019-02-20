def progression(l):
    n = len(l)
    if n == 0:
        return False
    if n == 1:
        return True
    l.sort()
    d = l[1] - l[0]
    for i in range(2, n):
        if l[i] - l[i - 1] != d:
            return False
    return True


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


def is_square(positive_int):
    x = positive_int // 2
    seen = {x}
    while x * x != positive_int:
        x = (x + (positive_int // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def primesquare(l):
    is_lastPrime = False
    for i in range(0, len(l)):
        if i == 0:
            if is_prime(l[i]):
                is_lastPrime = True
        else:
            if is_lastPrime:
                if is_square(l[i]):
                    is_lastPrime = False
                else:
                    return False
            else:
                if is_prime(l[i]):
                    is_lastPrime = True
                else:
                    return False
    return True


def matrixflip(l, flip_type):
    k = l
    if flip_type == 'h':
        return [k[0][::-1]] + [k[1][::-1]]
    elif flip_type == 'v':
        return l[::-1]
    else:
        return l



def progression(l):
  if(l==[]):
    return False
  if(len(l)<=2):
    return True
  d=l[1]-l[0]
  for i in range(2,len(l)):
    if(l[i] != l[0]+(i*d)):
      return False
  return True

def prime(n):
  if(n==1):
    return False
  for i in range(2,n//2+1):
    if(n%i==0):
      return False
  return True

import math
def perfect(n):
  a=math.sqrt(n)
  if((a//1) == a):
    return True
  return False

def primesquare(l):
  if(prime(l[0])):
    for i in range(1,len(l)):
      if(i%2 == 1):
        if(not perfect(l[i])):
          return False
      else:
        if(not prime(l[i])):
          return False
  elif(perfect(l[0])):
    for i in range(1,len(l)):
      if(i%2 == 1):
        if(not prime(l[i])):
          return False
      else:
        if(not perfect(l[i])):
          return False
  return True

def matrixflip(m,d):
  from copy import copy, deepcopy
  n=deepcopy(m)
  if(d=='h'):
    for i in range(len(n)):
      for j in range(len(n[i])//2):
        (n[i][j],n[i][len(n[i])-j-1])=(n[i][len(n[i])-j-1],n[i][j])
  elif(d=='v'):
    for i in range(len(n)//2):
      (n[i],n[len(n)-i-1])=(n[len(n)-i-1],n[i])
  return n



