import socket
from _thread import *
import sys
from Player import Player
import pickle

from props import Ball

points_1 = 0
points_2 = 0
server = "127.0.0.1"
port = 5555
f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

f.bind((server, port))

f.listen(2)
print("Waiting for connection, Server started")


players = [Player(20, 20), Player(560, 350)]
ball = Ball(300, 300, 5, velocity=(3, 0))


def threaded_client(conn, player):
    global ball
    conn.send(pickle.dumps([players[player], ball]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            ball.move(players)

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = [players[0], ball]
                else:
                    reply = [players[1], ball]

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
