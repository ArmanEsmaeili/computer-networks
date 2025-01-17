from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    # ایجاد مجوزدهنده برای مدیریت کاربران
    authorizer = DummyAuthorizer()
    
    # اضافه کردن یک کاربر با دسترسی کامل (خواندن و نوشتن)
    authorizer.add_user("user", "12345", ".", perm="elradfmw")

    # ساختن یک هندلر برای مدیریت ارتباطات
    handler = FTPHandler
    handler.authorizer = authorizer

    # ایجاد سرور FTP روی پورت 2121
    server = FTPServer(("0.0.0.0", 2121), handler)
    
    print("FTP server is running on port 2121...")
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()
