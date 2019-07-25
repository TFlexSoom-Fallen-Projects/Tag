from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((input("IP Address??\n"), int(input("PORT?\n"))))

var = s.recv(1024)
s.close()
print(var)