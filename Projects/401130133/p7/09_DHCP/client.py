import socket

# تنظیمات کلاینت DHCP
DHCP_SERVER_ADDRESS = ('localhost', 67)
CLIENT_PORT = 68
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('localhost', CLIENT_PORT))

# مرحله 1: Discovery
discover_message = "DHCPDISCOVER"
client_socket.sendto(discover_message.encode('utf-8'), DHCP_SERVER_ADDRESS)
print("Sent DHCPDISCOVER to server")

# دریافت پاسخ از سرور (Offer)
data, server_address = client_socket.recvfrom(1024)
offer_message = data.decode('utf-8')
print(f"Received DHCPOFFER: {offer_message} from server")

# مرحله 2: Request
request_message = "DHCPREQUEST " + offer_message.split()[1]
client_socket.sendto(request_message.encode('utf-8'), DHCP_SERVER_ADDRESS)
print(f"Sent DHCPREQUEST to server for IP {offer_message.split()[1]}")

# مرحله 3: Acknowledge
data, server_address = client_socket.recvfrom(1024)
ack_message = data.decode('utf-8')
print(f"Received DHCACK: {ack_message} from server")

# بستن سوکت
client_socket.close()
