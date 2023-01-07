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
  key = 0
  currentSeed = seed.copy()
  for i in range(4):
    newKey, currentSeed  = createOneKey(currentSeed)
    key += newKey

  return key, currentSeed

def createOneKey(seed : list[int]):
  moveJokers(seed)
  swapCardsBehindAndAfterJokers(seed)
  swapWithN(seed)

  first = abs(seed[0])
  if first == 53:
    return createOneKey(seed)

  return seed[first], seed