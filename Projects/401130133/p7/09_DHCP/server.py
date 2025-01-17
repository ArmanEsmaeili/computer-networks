import socket
import random
import time
import threading

# تنظیمات سرور DHCP
DHCP_SERVER_ADDRESS = ('localhost', 67)
DHCP_CLIENT_PORT = 68
DHCP_POOL = ['192.168.1.' + str(i) for i in range(100, 200)]  # Pool از 100 تا 199
leased_ips = set()  # مجموعه ای از IPهای اختصاص داده شده

# ایجاد سوکت برای سرور DHCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(DHCP_SERVER_ADDRESS)
print("DHCP Server is running on port 67...")

def handle_client(client_address, data):
    """ پردازش درخواستهای DORA از سوی کلاینت """

    # مرحله 1: Discovery
    print(f"Received DHCP Discovery from {client_address}")
    
    # انتخاب یک IP از Pool که هنوز به کسی اختصاص داده نشده است
    available_ip = None
    for ip in DHCP_POOL:
        if ip not in leased_ips:
            available_ip = ip
            break
    
    if available_ip is None:
        print("No available IP addresses")
        return
    
    # مرحله 2: Offer
    offer_message = f"DHCPOFFER {available_ip}"
    server_socket.sendto(offer_message.encode('utf-8'), client_address)
    print(f"Sent DHCPOFFER to {client_address} with IP {available_ip}")

    # مرحله 3: Request
    data, client_address = server_socket.recvfrom(1024)
    request_message = data.decode('utf-8')
    if "DHCPREQUEST" in request_message:
        print(f"Received DHCPREQUEST from {client_address}")
        
        # مرحله 4: Acknowledge
        leased_ips.add(available_ip)  # ثبت IP به عنوان اختصاص داده شده
        ack_message = f"DHCACK {available_ip}"
        server_socket.sendto(ack_message.encode('utf-8'), client_address)
        print(f"Sent DHCACK to {client_address} with IP {available_ip}")

# هر بار که یک درخواست دریافت می‌شود، یک نخ جدید ایجاد می‌کنیم تا درخواست را پردازش کند
def start_server():
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received request from {client_address}")
        threading.Thread(target=handle_client, args=(client_address, data)).start()

# اجرای سرور DHCP
start_server()
