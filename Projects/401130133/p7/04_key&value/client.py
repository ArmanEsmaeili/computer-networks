import socket

def run_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket.recv(1024).decode())

    while True:
        command = input("Enter command (SET/GET/DEL/SHOW/EXIT): ")
        client_socket.send(command.encode())

        if command.upper() == 'EXIT':
            print("Closing connection...")
            break

        result = client_socket.recv(4096).decode()
        print(f"Server response:\n{result}")

    client_socket.close()

if __name__ == "__main__":
    run_client()
