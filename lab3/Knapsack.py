import random
import math
from datetime import datetime

n = 8
w = []
q = 0
r = 1

b = []

def generateKeys():
  global q
  global w
  global r
  random.seed(datetime.now())
  x = random.randint(2, 10)
  w.append(x)
  total = x
  for i in range(n-1):
    x = random.randint(total + 1, 2 * total)
    w.append(x)
    total += x

  q = random.randint(total + 1, 2 * total)
  r = q
  while math.gcd(r, q) != 1:
    r = random.randint(2, q - 1)

  for x in w:
    b.append(r * x % q)
  
