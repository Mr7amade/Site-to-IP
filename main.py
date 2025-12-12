import socket

#port = socket.getservbyname(input("http/https/ftp/telnet:"))

#print(port)

service = socket.gethostbyname(input("Site:"))

print(service)
