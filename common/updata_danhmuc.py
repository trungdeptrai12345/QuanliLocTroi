from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def update_danhmuc(id, ten_moi, mota_moi):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "UPDATE danhmuc SET ten = %s, mota = %s WHERE id = %s"
        cursor.execute(sql, (ten_moi, mota_moi, id))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Đã cập nhật danh mục có ID = {id}")
        else:
            print(f"Không tìm thấy danh mục có ID = {id}")

    except Error as e:
        print("Lỗi khi cập nhật danh mục:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
