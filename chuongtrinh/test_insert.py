from common.insertdanhmuc import insert_danhmuc
while True:
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vào mô tả")
    insert_danhmuc(ten,mota)
    con=input("Tiếp tục y , THOÁT THÌ NHẤN BẤT KỲ")
    if con!="y":
        break