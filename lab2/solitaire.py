

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

def createKey(seed : list[int]):
  #first step: search for white joker
  print(seed)
  moveJokers(seed)
  print(seed)
  return 0

createKey([32, 14, 10, 45, 6, 44, 49, 8, 11, 33, 12, 23, 9, 35, -53, 20, 30, 16, 24, 7, 52, 38, 29, 1, 17, 4, 3, 40, 18, 41, 26, 34, 43, 25, 42, 51, 48, 21, 47, 27, 50, 22, 5, 31, 39, 36, 46, 28, 37, 13, 2, 15, 19, 53])