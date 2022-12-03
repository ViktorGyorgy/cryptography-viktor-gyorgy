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
    return

  arr1 = seed[0:last]
  arr2 = seed[last:(len(seed) - 1)]

  seed.clear()
  seed.extend(arr2)
  seed.extend(arr1)
  seed.append(last)

def createKey(seed : list[int]):
  #first step: search for white joker
  moveJokers(seed)
  swapCardsBehindAndAfterJokers(seed)
  # print(seed)
  swapWithN(seed)
  return 0

createKey([50, 45, 13, 11, 25, 23, 30, 39, 29, 34, 4, 46, 9, 16, 43, 7, 33, 38, 6, -53, 20, 18, 47, 41, 51, 35, 19, 12, 27, 22, 53, 52, 24, 42, 17, 21, 37, 32, 2, 48, 36, 15, 40, 44, 26, 3, 31, 14, 5, 10, 28, 8, 49, 1])