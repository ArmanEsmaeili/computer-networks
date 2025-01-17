import socket

# تنظیمات کلاینت
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# اتصال به سرور
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

print("Connected to the server!")

# دریافت پیام از سرور (تخته بازی و نوبت بازیکن)
while True:
    data = client_socket.recv(1024).decode()
    print(data)
    if "Game Over" in data:
        break

    # ارسال حرکت (فرمت row,col)
    move = input("Enter your move (row,col): ")
    client_socket.send(move.encode())

# بستن اتصال
client_socket.close()
