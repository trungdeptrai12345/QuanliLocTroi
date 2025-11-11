import tkinter as tk
from tkinter import ttk, messagebox

from common.insertdanhmuc import insert_danhmuc
from common.detele_danhmuc import delete_danhmuc
from common.updata_danhmuc import update_danhmuc
from common.get_danhmuc import get_all_danhmuc

def lam_moi():
    tree.delete(*tree.get_children())
    for row in get_all_danhmuc():
        tree.insert('', 'end', values=row)
    entry_id.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)

def them():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Bạn phải nhập tên danh mục!")
        return
    insert_danhmuc(ten, mota)
    lam_moi()

def sua():
    select = tree.selection()
    if not select:
        messagebox.showwarning("Chọn dòng!", "Chọn danh mục để sửa")
        return
    madm = tree.item(select[0])['values'][0]
    ten = entry_ten.get()
    mota = entry_mota.get()
    update_danhmuc(madm, ten, mota)
    lam_moi()

def xoa():
    select = tree.selection()
    if not select:
        messagebox.showwarning("Chọn dòng!", "Chọn danh mục để xóa")
        return
    madm = tree.item(select[0])['values'][0]
    delete_danhmuc(madm)
    lam_moi()

def tree_click(event):
    select = tree.selection()
    if select:
        val = tree.item(select[0])['values']
        entry_id.delete(0, tk.END)
        entry_id.insert(0, val[0])
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, val[1])
        entry_mota.delete(0, tk.END)
        entry_mota.insert(0, val[2])

root = tk.Tk()
root.title("Quản Lý Danh mục Sản phẩm")
root.geometry("750x350")

frame_top = tk.LabelFrame(root, text="Thông tin danh mục")
frame_top.pack(fill="x", padx=8, pady=4)

tk.Label(frame_top, text="Mã DM:").grid(row=0, column=0, padx=4, pady=2)
entry_id = tk.Entry(frame_top, width=10)
entry_id.grid(row=0, column=1, padx=2, pady=2)
entry_id.config(state='disabled')

tk.Label(frame_top, text="Tên danh mục:").grid(row=0, column=2, padx=4, pady=2)
entry_ten = tk.Entry(frame_top, width=25)
entry_ten.grid(row=0, column=3, padx=2, pady=2)

tk.Label(frame_top, text="Mô tả:").grid(row=1, column=0, padx=4, pady=2)
entry_mota = tk.Entry(frame_top, width=54)
entry_mota.grid(row=1, column=1, columnspan=3, padx=2, pady=2, sticky='w')

frame_btn = tk.Frame(root)
frame_btn.pack(fill="x", padx=8, pady=4)

btn_them = tk.Button(frame_btn, text="➕ Thêm", width=9, command=them)
btn_them.pack(side='left', padx=4)
btn_sua = tk.Button(frame_btn, text="✏️ Sửa", width=9, command=sua)
btn_sua.pack(side='left', padx=4)
btn_xoa = tk.Button(frame_btn, text="🗑 Xóa", width=9, command=xoa)
btn_xoa.pack(side='left', padx=4)
btn_lammo = tk.Button(frame_btn, text="🗂 Làm mới", width=9, command=lam_moi)
btn_lammo.pack(side='left', padx=4)

cols = ('Mã DM', 'Tên danh mục', 'Mô tả')
tree = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=150 if col != 'Mô tả' else 300)
tree.pack(fill="both", expand=True, padx=8, pady=4)
tree.bind("<<TreeviewSelect>>", tree_click)

lam_moi()
root.mainloop()
