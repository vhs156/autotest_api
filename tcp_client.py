import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)

message = "Hello Server"
client_socket.send(message.encode())

response = client_socket.recv(1024)
print(f"Received message: {response.decode()}")
client_socket.close()

