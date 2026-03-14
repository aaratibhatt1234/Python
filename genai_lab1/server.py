import socket

# server configuration
HOST = '127.0.0.1'
PORT = 5000

# hardcoded credentials (for project demo)
VALID_USERNAME = "student"
VALID_PASSWORD = "1234"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started...")
print("Waiting for client connection...")

conn, addr = server_socket.accept()
print("Connected with", addr)

# receive username and password
username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

# authentication check
if username == VALID_USERNAME and password == VALID_PASSWORD:
    conn.send("AUTH_SUCCESS".encode())
    print("Client authenticated successfully")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("Client disconnected")
            break

        print("Client:", data)
        reply = input("Server reply: ")
        conn.send(reply.encode())
else:
    print("Authentication failed")
    conn.send("AUTH_FAILED".encode())
    conn.close()

conn.close()
server_socket.close()

