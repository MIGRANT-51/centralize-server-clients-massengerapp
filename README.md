# Chat Application in Python

## Overview
This repository contains a simple chat application implemented in Python using sockets for communication. The application is divided into two parts: `server.py` and `client.py`. The server facilitates communication between multiple clients, allowing them to send and receive messages in a chat-like environment.

## Instructions

### Server (`server.py`)

#### Running the Server:
1. Open a terminal.
2. Navigate to the directory containing `server.py`.
3. Run the server using the command: `python server.py`.

#### Server Configuration:
- The server is set to run on `127.0.0.1` (localhost) and port `5106`. Modify the `HOST` and `PORT` variables in the `server.py` file if needed.

#### Client Connection:
- Clients can connect to the server using the `client.py` script.
- The server supports up to `LISTENER_LIMIT` concurrent connections, set to 5 by default. Modify this value in the `server.py` file if needed.

### Client (`client.py`)

#### Running the Client:
1. Open a new terminal.
2. Navigate to the directory containing `client.py`.
3. Run the client using the command: `python client.py`.

#### Client Configuration:
- The client is configured to connect to the server at `127.0.0.1` and port `5106`. Modify the `HOST` and `PORT` variables in the `client.py` file if needed.

#### Entering the Chat:
- When prompted, enter a username. Ensure the username is not already taken by another client on the server.

#### Chatting:
- Once connected, clients can send messages to the entire chat. Messages are displayed with the format `[username]: message`.

#### Exiting the Client:
- To exit the client, simply close the terminal.

## Important Notes
- The server and clients communicate using UTF-8 encoding.
- Usernames are used for identification in the chat, and each message sent includes the sender's username.

## Error Handling
Both the server and client scripts include basic error handling to address potential issues such as empty messages, disconnections, and failed connections.

## Dependencies
The scripts use Python's built-in `socket` and `threading` modules. No additional dependencies are required.
