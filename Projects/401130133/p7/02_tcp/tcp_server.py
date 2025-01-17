import socket
import subprocess

def run_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        # دریافت دستور از کلاینت
        command = conn.recv(1024).decode()
        if command.lower() == 'exit':
            print("Closing connection...")
            break

        print(f"Received command: {command}")

        # اجرای دستور و گرفتن خروجی
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            result = f"Error: {e.output}"

        # ارسال خروجی به کلاینت
        conn.send(result.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    run_server()
