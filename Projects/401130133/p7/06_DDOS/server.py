import socket
import threading
import time

MAX_REQUESTS = 10  # حداکثر تعداد درخواست مجاز در بازه زمانی
TIME_WINDOW = 5  # بازه زمانی (ثانیه)
blocked_clients = set()  # لیست سیاه کلاینت‌ها

# دیکشنری برای نگهداری تعداد درخواست‌ها از هر کلاینت
request_count = {}

def handle_client(conn, addr):
    """پردازش درخواست‌های کلاینت"""
    global request_count, blocked_clients

    ip = addr[0]  # آدرس IP کلاینت

    if ip in blocked_clients:
        print(f"Blocked client {ip} tried to connect.")
        conn.close()
        return

    start_time = time.time()
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            # ثبت درخواست کلاینت
            if ip not in request_count:
                request_count[ip] = 0
            request_count[ip] += 1

            # بررسی تعداد درخواست‌ها در بازه زمانی
            if time.time() - start_time > TIME_WINDOW:
                if request_count[ip] > MAX_REQUESTS:
                    print(f"Blocking client {ip} for sending too many requests.")
                    blocked_clients.add(ip)
                    conn.close()
                    break
                # ریست کردن شمارشگر پس از بازه زمانی
                request_count[ip] = 0
                start_time = time.time()

            print(f"Received from {addr}: {data}")
            conn.send(f"Received: {data}".encode())

        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            break

    conn.close()

def run_server(host='127.0.0.1', port=12345):
    """اجرای سرور"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    run_server()
