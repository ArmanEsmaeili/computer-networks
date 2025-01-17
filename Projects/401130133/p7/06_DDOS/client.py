import socket
import time

def run_client(host='127.0.0.1', port=12345, num_requests=20, delay=0.2):
    """اجرای کلاینت برای ارسال درخواست به سرور"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    for i in range(num_requests):
        message = f"Request {i+1}"
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
        time.sleep(delay)  # تأخیر بین هر درخواست

    client_socket.close()

if __name__ == "__main__":
    # اجرای کلاینت با 20 درخواست و تأخیر 0.2 ثانیه بین هر درخواست
    run_client()
