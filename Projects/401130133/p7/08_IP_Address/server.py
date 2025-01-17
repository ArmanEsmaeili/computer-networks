import socket

# جدول DNS برای سایت‌های معروف
dns_table = {
    'google.com': '142.250.72.14',
    'yahoo.com': '98.137.11.163',
    'facebook.com': '157.240.22.35',
    'github.com': '140.82.121.3',
    'twitter.com': '104.244.42.65',
    'amazon.com': '205.251.242.103',
    'bing.com': '40.77.226.26',
    'wikipedia.org': '208.80.154.224',
    'stackoverflow.com': '151.101.65.69',
    'reddit.com': '151.101.1.140'
}

# پورت و آدرس سرور DNS
DNS_SERVER_ADDRESS = ('localhost', 53)

# ایجاد سوکت برای سرور
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(DNS_SERVER_ADDRESS)
print("DNS Server is running on port 53...")

while True:
    # دریافت درخواست از کلاینت
    data, client_address = server_socket.recvfrom(512)
    print(f"Received request from {client_address}")

    # استخراج دامنه از درخواست (در اینجا ساده‌سازی شده است)
    domain_name = data.decode('utf-8').strip()

    # بررسی اینکه آیا دامنه در جدول DNS وجود دارد یا خیر
    ip_address = dns_table.get(domain_name, "Not Found")

    # ارسال پاسخ به کلاینت
    server_socket.sendto(ip_address.encode('utf-8'), client_address)
