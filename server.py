import socket
host = '127.0.0.1'
port = 6880
data = []
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
conn,addr = s.accept()
choice = conn.recv(1024).decode()
while True:
    if choice == '1':
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()
        data.append(username)
        data.append(password)
        reply = 'Signup sucessfully'
        conn.sendall(reply.encode())
    elif choice == '2':
        user_1 = conn.recv(1024).decode()
        password_1 = conn.recv(1024).decode()
        if user_1 == data[0] and password_1 == data[1]:
            reply = 'Login Successful'
        else:
            reply = 'login failed'
        conn.sendall(reply.encode())
    elif choice == '3':
        reply = 'Logout Successfully'
        conn.sendall(reply.encode())
        break
    choice = conn.recv(1024).decode()
conn.close()
