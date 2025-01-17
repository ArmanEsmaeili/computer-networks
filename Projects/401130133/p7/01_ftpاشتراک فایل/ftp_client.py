from ftplib import FTP

def upload_file():
    # اتصال به سرور FTP
    ftp = FTP()
    ftp.connect("127.0.0.1", 2121)
    ftp.login("user", "12345")

    # باز کردن فایل برای آپلود
    filename = "test.txt"
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename}", file)

    print(f"{filename} uploaded successfully.")
    ftp.quit()

def download_file():
    # اتصال به سرور FTP
    ftp = FTP()
    ftp.connect("127.0.0.1", 2121)
    ftp.login("user", "12345")

    # دانلود فایل
    filename = "test.txt"
    with open(f"downloaded_{filename}", "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)

    print(f"{filename} downloaded successfully.")
    ftp.quit()

if __name__ == "__main__":
    # آپلود فایل
    upload_file()

    # دانلود فایل
    download_file()
