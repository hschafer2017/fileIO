import socket
IP = '0.0.0.0'
PORT = 1125
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048

listening_socket = socket.socket()
listening_socket.bind((IP,PORT))

listening_socket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'd like to connect")

while True:    
    (client_socket, client_ip_and_port) = listening_socket.accept()
    (client_ip, client_port) = client_ip_and_port
        
    initial_response = "Connection available\n".encode()
    client_socket.send(initial_response)
    print(initial_response)
        
    while True:   
        client_message = client_socket.recv(BUFFER_SIZE).decode()
        echo_response = ("You said: " + client_message).encode()
        print(echo_response)
        client_socket.send(echo_response)
        if client_message == "Exit\n":
            print(client_message)
            client_socket.close()
            break

