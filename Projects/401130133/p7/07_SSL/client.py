import socket
import ssl

# ایجاد سوکت برای ارتباط با سرور
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# اتصال به سرور ایمن
secure_socket = ssl.wrap_socket(client_socket, keyfile=None, certfile=None, server_side=False, server_hostname="localhost")
secure_socket.connect(('localhost', 12345))

# دریافت پیغام خوش‌آمدگویی
data = secure_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

# ارسال پیغام
message = input("Enter your message: ")
secure_socket.send(message.encode('utf-8'))

# بستن ارتباط
secure_socket.close()
