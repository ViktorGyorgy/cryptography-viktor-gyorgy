import random

x = [i for i in range(1, 54)]
random.shuffle(x)
#-53 a fekete joker
x.insert(random.randint(0, len(x)), -53)
print(x)