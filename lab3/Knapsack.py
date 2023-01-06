import random
import math
from datetime import datetime
import utils

n = 8
w = []
q = 0
r = 1
s = 0

b = []

def generateKeys():
  global q
  global w
  global r
  global b
  global s
  random.seed(str(datetime.now()))
  x = random.randint(2, 10)
  w = []
  b = []
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

  s = utils.modinv(r, q)

def encodeByte(byte):
  bits = utils.byte_to_bits(byte)
  return sum([x * y for x, y in zip(bits, b)])

def decodeByte(bytes):
  c = int.from_bytes(bytes, "little")
  c2 = 1


byte = bytes("h", 'utf8')[0]
e = encodeByte(byte)
d = decodeByte(int.to_bytes(e, e.bit_length(), "little"))
print(d)
