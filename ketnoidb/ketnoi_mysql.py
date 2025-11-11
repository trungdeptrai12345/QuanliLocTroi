import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_nhung_trung',
            port = 3307
        )

        if connection.is_connected():
            print("Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("Lỗi kết nối MySQL:", e)
        return None

# Sử dụng:
conn = connect_mysql()
if conn:
    # Thực hiện các truy vấn dữ liệu tại đây
    # (ví dụ: với db_nhung_trung ở phpMyAdmin trang http://localhost:9000/phpmyadmin)
    conn.close()
