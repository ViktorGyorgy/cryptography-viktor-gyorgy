import socket
import json
import solitaire, streamCrypto, Knapsack
from _thread import *

HOST = "127.0.0.1"
SERVER_PORT = 8000
MY_PORT = 8001
OTHER_PORT = 8002

ALGORITHMS = {"solitaire":  solitaire.createKey}

file = open("config1.json")
conf = json.load(file)
file.close()

solitaireSeed = conf["initial_seed"]

def client_reader_thread(mys: socket.socket):
  while True:
    data = mys.recv(1024)

    if not data:
      print("BYE")
      break

    # add decryption
    decoded = codeText(data)
    print("Other user: " + decoded.decode('utf-8'))

def server_reader_thread(mys: socket.socket):
  while True:
    data = mys.recv(1024)

    if not data:
      print("BYE")
      break

    # add decryption
    decoded = codeText(data)
    print("Other user: " + decoded.decode('utf-8'))

def codeText(data: bytes):
  return streamCrypto.streamCrypt(data, solitaire.createKey, solitaireSeed)

def main():
  Knapsack.generateKeys()

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, SERVER_PORT))
    print("Connected to server")

    s.sendall("\n".join([str(i) for i in Knapsack.b]).encode())

    print("Public key sent to server, the key is " +  str(Knapsack.b))

    print("Waiting for thepublic key of other client!")

    pubKeys = [int(i) for i in s.recv(2048).decode('utf8').split('\n')]
    print("The pubkeys of the other is " + str(pubKeys))
    Knapsack.b = pubKeys

    #Creating socket to send solitaira seed to other


main()