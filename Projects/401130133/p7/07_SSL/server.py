import socket
import ssl

# ایجاد یک سوکت ساده
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# تنظیم پورت و آدرس
server_socket.bind(('localhost', 12345))

# گوش دادن به درخواست‌های ورودی
server_socket.listen(5)
print("Server is listening for connections...")

# ایجاد سرور امن با SSL
server_socket = ssl.wrap_socket(server_socket, keyfile="server-key.pem", certfile="server-cert.pem", server_side=True)

while True:
    # پذیرش ارتباط
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")

    # دریافت و ارسال داده‌ها
    client_socket.send(b"Welcome to the secure chat room!")
    data = client_socket.recv(1024)
    print(f"Received message: {data.decode('utf-8')}")

    # بستن ارتباط
    client_socket.close()
