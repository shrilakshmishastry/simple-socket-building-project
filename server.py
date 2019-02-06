import socket
s = socket.socket()
print(dir(s))
port = 1234

s.bind(('',port))
print("socket binded %s" %(port))

s.listen(5)
print("socket is listening")

while True:
    c,addr = s.accept()
    print("Got connected",addr)
    c.sendall('Thank you'.encode('utf-8'))
    c.close()
