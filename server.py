# Tristan Hilbert
# Simple Port Script
#
#
# Port -> 7019

import socket
ipv4_address = '192.168.0.111'
port = 7019

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ipv4_address, port))
sock.settimeout(20)
print("Started Connection!")
while True:
    try:
        sock.listen(0)
        conn, addr = sock.accept()
        conn.settimeout(10)
        try:
            var = conn.recv(1024)
            a = "der"
            while a != "":
                print(var)
                a = conn.send(input("> ").encode())
                var = conn.recv(1024)
            conn.close()
        except socket.timeout:
            conn.close()
    except socket.timeout:
        a = input("Continue Checking?")
        if a == '1':
            continue
        else:
            sock.close()
            break


