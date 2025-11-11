from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def get_all_danhmuc():
    try:
        connection = connect_mysql()
        if connection is None:
            return []

        cursor = connection.cursor()
        sql = "SELECT id, ten, mota FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except Error as e:
        print("Lỗi khi lấy danh sách danh mục:", e)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

# Ví dụ in ra danh sách:
ds = get_all_danhmuc()
for id, ten, mota in ds:
    print(f"ID: {id} | Tên: {ten} | Mô tả: {mota}")
