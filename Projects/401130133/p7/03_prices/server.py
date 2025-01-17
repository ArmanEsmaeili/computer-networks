import socket
import random
import time
import threading

# مقادیر اولیه قیمت ارزها
prices = {
    'USD': 100.0,
    'EUR': 120.0,
    'JPY': 90.0
}

def update_prices():
    """ به‌روزرسانی قیمت ارزها به‌صورت شبیه‌سازی شده """
    while True:
        for currency in prices:
            # ایجاد تغییرات تصادفی در قیمت ارزها
            change = random.uniform(-0.5, 0.5)
            prices[currency] += change
        time.sleep(2)  # هر 2 ثانیه قیمت‌ها به‌روزرسانی می‌شود

def handle_client(conn, addr):
    """ پردازش درخواست‌های کلاینت """
    print(f"Connected by {addr}")
    conn.send("Welcome to the currency price server.\nType 'prices' to get current prices or 'exit' to quit.".encode())

    while True:
        command = conn.recv(1024).decode().strip()
        if not command:
            continue

        if command.lower() == 'exit':
            print(f"Connection closed by {addr}")
            break
        elif command.lower() == 'prices':
            price_info = "\n".join([f"{currency}: {price:.2f}" for currency, price in prices.items()])
            conn.send(price_info.encode())
        else:
            conn.send("Invalid command. Type 'prices' or 'exit'.".encode())

    conn.close()

def run_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    # اجرای به‌روزرسانی قیمت‌ها در یک رشته (Thread) جداگانه
    threading.Thread(target=update_prices, daemon=True).start()

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    run_server()
