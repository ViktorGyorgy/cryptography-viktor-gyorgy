import socket
import json
import blumblumShub
import streamCrypto
import solitaire
from _thread import *

HOST = "127.0.0.1"
PORT = 4000

ALGORITHMS = {"blumBlumShub": blumblumShub.createKey, "solitaire": solitaire.createKey}

file = open("config2.json")
conf = json.load(file)
file.close()

def client_reader_thread(mys: socket.socket):
  while True:
    data = mys.recv(1024)

    if not data:
      print("BYE")
      break

    # add decryption
    decoded = codeText(data)
    print("Other user:" + decoded.decode('utf-8'))

def server_reader_thread(mys: socket.socket):
  while True:
    data = mys.recv(1024)

    if not data:
      print("BYE")
      break

    # add decryption
    decoded = codeText(data)
    print("Other user:" + decoded.decode('utf-8'))

def codeText(data: bytes):
  return streamCrypto.streamCrypt(data, ALGORITHMS[conf["algorithm"]], conf["initial_seed"])


def main():
  mode = ""
  while mode != 'S' and mode != 'C':
    mode = input("Do you want to be (S)erver or (C)lient?\n")
    mode = mode.upper()

  if(mode == 'S'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      
      start_new_thread(server_reader_thread, (conn, ))

      while True:
        text = input("Write something!\n")
        data = codeText(text.encode('utf-8'))
        conn.sendall(data)

  else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      start_new_thread(client_reader_thread, (s, ))

      while True:
        text = input("Write something!\n")
        data = codeText(text.encode('utf-8'))
        s.sendall(data)

main()