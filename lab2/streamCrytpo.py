def streamCrypt(data: bytearray, cryptoFunction : function, initialSeed : any):
  newData = bytearray
  newSeed = initialSeed
  for byte in data:
    key, newSeed = cryptoFunction(newSeed)
    newData.append(byte ^ key)
  return newData
