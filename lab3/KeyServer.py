import socket

KnapsackKeys = {}

HOST = 'localhost'
PORT = 8000
n = 8

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Server is running")

    conns = []
    for i in range(2):
        conn, addr = s.accept()
        print("Server got a new client")

        conns.append(conn)
        #get the private key
        PORT += 1

        print("Getting the public key from client " + str(PORT))
        keys = [int(i) for i in conn.recv(2048).decode('utf8').split('\n')]

        KnapsackKeys[PORT] = keys
        print("Knapsakkeys: " + str(KnapsackKeys))
        
        #add new Thread to read from client

    print("Sending keys to the clients")
    conns[0].sendall('\n'.join(str(i) for i in KnapsackKeys[8002]).encode())
    conns[1].sendall('\n'.join(str(i) for i in KnapsackKeys[8001]).encode())

    print("Shutting down, bye!")

        
