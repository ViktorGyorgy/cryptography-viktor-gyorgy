import re

#clever regex trick: https://iluxonchik.github.io/regular-expression-check-if-number-is-prime/
#not that performant tho
def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

num = 0
for i in range(pow(2, 16), pow(2, 17)):
  
  if isprime(i) and i % 4 == 3:
    print(i)
    num += 1
    if num >= 2:
      exit(0)
    