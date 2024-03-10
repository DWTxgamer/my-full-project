import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received message from {username}: {message}")
            broadcast_message = f"{username}: {message}"
            broadcast(broadcast_message, client_socket)
        except:
            break

    print(f"{username} Left")
    client_sockets.remove(client_socket)
    usernames.remove(username)
    broadcast_message = f"{username} left the chat"
    broadcast(broadcast_message, client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in client_sockets:
        try:
            if client != sender_socket:
                client.send(message.encode())
        except:
            continue

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.23.1', 1234))
    server.listen(5)

    print("Server is listening on port 1234...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        username = client_socket.recv(1024).decode()
        usernames.append(username)
        client_sockets.append(client_socket)

        print(f"{username} joined the chat")
        broadcast_message = f"{username} joined the chat"
        broadcast(broadcast_message, client_socket)

        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()

if __name__ == "__main__":
    client_sockets = []
    usernames = []
    start_server()
