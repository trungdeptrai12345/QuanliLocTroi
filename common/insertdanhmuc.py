from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten, mota):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten, mota) VALUES (%s, %s)"
        data= (ten, mota)
        cursor.execute(sql, (ten, mota))
        connection.commit()
        print("Đã thêm danh mục thành công!")
    except Error as e:
        print("Lỗi khi insert danh mục:", e)
    finally:
        cursor.close()