import socket
host = '127.0.0.1'
port = 6880
s=socket.socket()
s.connect((host,port))
print('Connected to server')
while True:
    print('''Enter ur choice:
    1.Signup
    2.Login
    3.Logout
    ''')
    choice = input('Enter ur choice:')
    s.sendall(choice.encode())
    if choice == '1':
        username = input('Enter the username:')
        password = input('Enter the password:')
        s.sendall(username.encode())
        s.sendall(password.encode())
        data = s.recv(1024).decode()
        print(data)
    elif choice == '2':
        username_1 = input('Enter the username to login:')
        password_1 = input('Enter the password to login:')
        s.sendall(username_1.encode())
        s.sendall(password_1.encode())
        data = s.recv(1024).decode()
        print(data)
    elif choice == '3':
        msg = s.recv(1024).decode()
        print(msg)
        break
s.close()

