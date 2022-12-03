import json
import streamCrypto
import solitaire

f = open("config.json")
config = json.load(f)
f.close()

text = "helloVilag"
enc = streamCrypto.streamCrypt(bytes(text, 'utf-8'), solitaire.createKey, config["initial_seed"])
print(enc)
dec = streamCrypto.streamCrypt(enc, solitaire.createKey, config["initial_seed"])
print(dec.decode("utf-8"))