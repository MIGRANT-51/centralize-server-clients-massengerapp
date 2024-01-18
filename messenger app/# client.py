# client.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 5106

# Function to listen for messages from the server and display them
def listen_for_messages_from_server(client):
    while True:
        try:
            # Receive the message from the server
            message = client.recv(2048).decode('utf-8')
            if message:
                # Split the message into username and content using "~" as a separator
                username, content = message.split("~", 1)
                # Display the message with the username and content
                print(f"[{username}]: {content}")
            else:
                # If the message is empty, it indicates the server has closed the connection
                print("Message received from the server is empty")
                # Close the client socket and exit the loop
                client.close()
                break
        except:
            # If an error occurs while receiving the message, it indicates a connection issue
            print("Error occurred while receiving message from the server")
            # Close the client socket and exit the loop
            client.close()
            break

# Function to send messages to the server
def send_message_to_server(client):
    while True:
        try:
            # Get the user input as the message
            message = input("Enter message: ")
            if message:
                # Encode the message and send it to the server
                client.sendall(message.encode())
            else:
                # If the message is empty, notify the user
                print("Message empty")
        except:
            # If an error occurs while sending the message, it indicates a connection issue
            print("Error occurred while sending the message")
            # Close the client socket and exit the loop
            client.close()
            break

# Function to establish communication with the server
def communicate_to_server(client):
    try:
        # Get the user input as the username
        username = input("Enter username: ")
        if username:
            # Encode the username and send it to the server
            client.sendall(username.encode())
        else:
            # If the username is empty, notify the user
            print("Username cannot be empty")
            # Close the client socket and return from the function
            client.close()
            return

        # Receive response from the server indicating if the username is accepted or not
        response = client.recv(1024).decode('utf-8')
        if response == "USERNAME_TAKEN":
            # If the server rejects the username, notify the user and close the connection
            print("Username is already taken. Please choose a different one.")
            client.close()
            return

        # Start a separate thread to listen for messages from the server
        threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()
        # Start sending messages to the server in the main thread
        send_message_to_server(client)
    except:
        # If an error occurs while communicating with the server, it indicates a connection issue
        print("Error occurred while communicating with the server")
        # Close the client socket

def main():
    # Create a new client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect the client to the server
        client.connect((HOST, PORT))
        print("Successfully connected to the server")
    except Exception as e:
        # If unable to connect to the server, notify the user and exit the program
        print(f"Unable to connect to the server {HOST}:{PORT}: {e}")
        return

    # Start communication with the server
    communicate_to_server(client)

if __name__ == '__main__':
    main()