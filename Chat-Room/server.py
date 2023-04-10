import socket
import select
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:

    print("Correct Usage: Script, IP Address, Port")

    exit()

ip_address = str(sys.argv[1])

port = int(sys.argv[2])

server.bind((ip_address, port))

server.listen(100)

list_of_clients = []

def client_thread(conn, addr):

    conn.send("Welcome to SmashedFrenzy16's Chat Room!")

    while True:

        try:

            message = conn.recv(2048)

            if message:

                print(f"{addr[0]}: {message}")

                message_to_send = f"{addr[0]}: {message}"

                broadcast(message_to_send, conn)

            else:

                remove(conn)

        except:

            continue

def broadcast(message, connection):

    for client in list_of_clients:

        if client != connection:

            try:

                client.send(message)

            except:

                client.close()

                remove(client)

def remove(connection):

    if connection in list_of_clients:

        list_of_clients.remove(connection)

while True:

    conn, addr = server.accept()

    list_of_clients.append(conn)

    print(f"{addr[0]} has joined!")

    start_new_thread(client_thread, (conn, addr))

conn.close()
server.close()

                