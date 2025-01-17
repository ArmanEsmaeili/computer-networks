import socket
import threading

def handle_client(conn, addr):
    """پردازش درخواست‌های کلاینت"""
    print(f"Connected by {addr}")
    conn.send("Connection established. Port is open.".encode())
    conn.close()

def run_server(host='127.0.0.1', ports=[12345, 12346, 12347]):
    """سرور که به پورت‌های مختلف گوش می‌دهد"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, 0))  # گوش دادن به هر پورت آزاد

    for port in ports:
        try:
            server_socket.bind((host, port))
            server_socket.listen(5)
            print(f"Server listening on port {port}...")
            
            while True:
                conn, addr = server_socket.accept()
                threading.Thread(target=handle_client, args=(conn, addr)).start()
                
        except Exception as e:
            print(f"Could not open port {port}: {e}")

if __name__ == "__main__":
    # سرور را برای پورت‌های مختلف راه‌اندازی می‌کند
    run_server()
