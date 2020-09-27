import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.bind((host, port))
s.listen(1)
print ("Waiting for c client's Connection \n =>", end=' ')
c, addr = s.accept()

print ("Connection from: " + str(c) + str(addr))

while True:
    r_data = c.recv(1024)
    if not r_data:
        break
    print ("\nFrom connected user: " + r_data.decode())
    data = r_data.decode().upper()
    # data = data.upper()
    print("Sending: " + data)
    c.send(data.encode())
c.close()
    



