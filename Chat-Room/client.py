import socket
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:

    print("Correct Usage: Script, IP Address, Port")

    exit()

ip_address = str(sys.argv[1])

port = int(sys.argv[2])

server.connect((ip_address, port))

while True:

    socket_list = [sys.stdin, server]

    read_s, write_s, error_s = select.select(socket_list, [], [])

    for s in read_s:

        if s == server:

            message = s.recv(2048)

            print(message)

        else:

            message = sys.stdin.readline()

            server.send(message)

            sys.stdout.write("You: ")

            sys.stdout.write(message)

            sys.stdout.flush()

server.close()

