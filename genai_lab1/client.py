import socket

HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# take credentials from user
username = input("Enter username: ")
password = input("Enter password: ")

# send credentials
client_socket.send(username.encode())
client_socket.send(password.encode())

# receive authentication result
response = client_socket.recv(1024).decode()

if response == "AUTH_SUCCESS":
    print("Login successful. You can start chatting.")

    while True:
        message = input("You: ")
        client_socket.send(message.encode())

        if message.lower() == "exit":
            break

        reply = client_socket.recv(1024).decode()
        print("Server:", reply)
else:
    print("Login failed. Connection closed.")

client_socket.close()
