#got thes numbers from online sources
p = 65539
q = 65543
n = p * q

def createKey(seed: int):
  z = 0
  x = pow(seed, 2) % n
  for i in range(8):
    x = pow(x, 2) % n
    z *= 2
    z += x % 2
  return z, x