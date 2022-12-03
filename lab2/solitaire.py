def moveJokers(seed : list[int]):
  feherIndex = seed.index(53)
  index1 = (feherIndex + 1) % len(seed)
  seed[feherIndex] = seed[index1]
  seed[(feherIndex + 1) % len(seed)] = 53

  feketeIndex = seed.index(-53)
  index1 = (feketeIndex + 1) % len(seed)
  index2 = (feketeIndex + 2) % len(seed)
  seed[feketeIndex] = seed[index1]
  seed[index1] = seed[index2]
  seed[index2] = -53

def swapCardsBehindAndAfterJokers(seed : list[int]):
  #whte joker, black joker indexes
  wIndex = seed.index(53)
  bIndex = seed.index(-53)
  i1 = min(wIndex, bIndex)
  i2 = max(wIndex, bIndex)

  arr1 = seed[0:i1]
  arr2 = seed[i1: i2+1]
  arr3 = seed[i2+1: len(seed)]

  seed.clear()
  seed.extend(arr3)
  seed.extend(arr2)
  seed.extend(arr1)

def swapWithN(seed : list[int]):
  last = abs(seed[len(seed) - 1])
  if(last == 53):
    print("nothing is happening")
    return

def createKey(seed : list[int]):
  #first step: search for white joker
  moveJokers(seed)
  swapCardsBehindAndAfterJokers(seed)
  print(seed)
  swapWithN(seed)
  return 0

createKey([32, 14, 10, 45, 6, 44, 49, 8, 11, 33, 12, 23, 9, 35, -53, 20, 30, 16, 24, 7, 52, 38, 29, 1, 17, 4, 3, 40, 18, 41, 26, 34, 43, 25, 42, 51, 48, 21, 47, 27, 50, 22, 5, 31, 39, 36, 46, 28, 37, 13, 2, 15, 19, 53])