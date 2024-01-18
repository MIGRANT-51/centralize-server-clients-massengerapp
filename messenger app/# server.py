# server.py

import socket
import threading

HOST = '127.0.0.1'
PORT = 5106
LISTENER_LIMIT = 5
active_clients = []

def listen_for_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                final_msg = f"{username}~{message}"
                send_messages_to_all(final_msg)
            else:
                print(f"Message received from {username} is empty")
                remove_client(username)
                break
        except:
            print(f"Error occurred while receiving message from {username}")
            remove_client(username)
            break

def send_message_to_client(client, message):
    client.sendall(message.encode())

def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

def remove_client(username):
    for user in active_clients:
        if user[0] == username:
            active_clients.remove(user)
            prompt_message = f"SERVER~{username} left the chat"
            send_messages_to_all(prompt_message)
            break

def client_handler(client):
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            if not username:
                print("Client username is empty")
                client.close()
                return
            
            if any(user[0] == username for user in active_clients):
                client.sendall("USERNAME_TAKEN".encode())
            else:
                client.sendall("USERNAME_ACCEPTED".encode())
                active_clients.append((username, client))
                prompt_message = f"SERVER~{username} added to the chat"
                send_messages_to_all(prompt_message)
                threading.Thread(target=listen_for_messages, args=(client, username)).start()
                break
        except:
            print("Error occurred while handling the client connection")
            client.close()
            return

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST}:{PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}: {e}")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]}:{address[1]}")
        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()