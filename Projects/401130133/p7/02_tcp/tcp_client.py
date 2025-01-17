import socket

def run_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        # گرفتن دستور از کاربر
        command = input("Enter command (type 'exit' to quit): ")
        client_socket.send(command.encode())

        if command.lower() == 'exit':
            print("Closing connection...")
            break

        # دریافت خروجی از سرور
        result = client_socket.recv(4096).decode()
        print(f"Result:\n{result}")

    client_socket.close()

if __name__ == "__main__":
    run_client()
