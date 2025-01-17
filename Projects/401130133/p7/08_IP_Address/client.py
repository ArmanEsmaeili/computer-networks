import socket

# دامنه‌ای که می‌خواهیم درخواست کنیم
domain_name = input("Enter domain name (e.g., google.com): ")

# ایجاد سوکت UDP برای ارتباط با سرور
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# آدرس سرور DNS
DNS_SERVER_ADDRESS = ('localhost', 53)

# ارسال درخواست به سرور DNS
client_socket.sendto(domain_name.encode('utf-8'), DNS_SERVER_ADDRESS)

# دریافت پاسخ از سرور DNS
data, server_address = client_socket.recvfrom(512)

# نمایش IP دریافت شده
print(f"The IP address for {domain_name} is: {data.decode('utf-8')}")

# بستن سوکت
client_socket.close()
