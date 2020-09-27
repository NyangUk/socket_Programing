import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = input("-> ")
    
    while message != 'q':
        s.send(message.encode())
        r_data = s.recv(1024)
        data = r_data.decode()
        print("Received from server: " + data)
        message = input("-> ")
    s.close()
    
Main()



