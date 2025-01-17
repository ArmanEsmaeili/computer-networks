import socket

def scan_ports(host, ports):
    """اسکن پورت‌های مختلف سرور"""
    open_ports = []
    
    for port in ports:
        try:
            # تلاش برای اتصال به هر پورت
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # زمان تایم‌اوت برای اتصال 1 ثانیه
            result = sock.connect_ex((host, port))  # بررسی اتصال به پورت
            
            if result == 0:
                print(f"Port {port} is open.")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error connecting to port {port}: {e}")
    
    return open_ports

def run_client(host='127.0.0.1', ports=[12345, 12346, 12347]):
    """اجرای اسکن پورت‌ها توسط کلاینت"""
    open_ports = scan_ports(host, ports)
    
    if open_ports:
        print("\nOpen ports found:", open_ports)
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    # اسکن پورت‌های مشخص شده
    run_client()
