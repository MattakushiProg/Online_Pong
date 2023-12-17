import socket
from _thread import *
import sys
from Player import Player
import pickle

server = "127.0.0.1"
port = 5555


f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

f.bind((server, port))
    
f.listen(2)
print('Waiting for connection, Server started')


players = [Player(0, 0), Player(100, 100)]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                    
                print("Received : ", data)
                print("Sending : ", reply)
                
            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = f.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn, currentPlayer)) 
    currentPlayer += 1