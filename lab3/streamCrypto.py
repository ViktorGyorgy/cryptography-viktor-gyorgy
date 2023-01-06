def streamCrypt(data: bytes, cryptoFunction, initialSeed : any):
  newData = []
  newSeed = initialSeed
  for byte in data:
    key, newSeed = cryptoFunction(newSeed)
    newData.append(byte ^ key)
  return bytes(newData)
