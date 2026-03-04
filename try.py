import tkinter as tk
from tkinter import messagebox
# إنشاء نافذة اللعبة
root = tk.Tk()
root.title("🎬 اختر مقعدك في السينما")
root.geometry("500x650")
root.config(bg="#2c2c2c")
# =========================
# متغيرات تتبع الاختيار
# =========================
selected_oneD = None
selected_twoD = None
# =========================
# القسم الأول: أحادي البعد
# =========================
oneD = ["VIP1", "VIP2", "VIP3", "VIP4"]
oneD_buttons = {}
def oneD_selected(index):
   global selected_oneD
   if selected_oneD is not None:
       messagebox.showwarning("تنبيه", "🚫 يمكنك اختيار مقعد واحد فقط من القسم الأول")
       return
   seat = oneD[index]
   oneD_buttons[index].config(bg="green", fg="white")
   selected_oneD = seat
   update_selection_label()
   message = f"""✨ تم اختيار المقعد: {seat}
📌 موقعه في المصفوفة:
VIPsection[{index}]"""
   messagebox.showinfo("مصفوفة أحادية البعد", message)
label1 = tk.Label(root, text="🎟 القسم الأول:",
                 font=("Arial", 14, "bold"),
                 fg="yellow", bg="#2c2c2c")
label1.pack(pady=10)
frame1 = tk.Frame(root, bg="#2c2c2c")
frame1.pack()
for i in range(len(oneD)):
   btn = tk.Button(frame1,
                   text=oneD[i],
                   width=7,
                   height=2,
                   font=("Arial", 12, "bold"),
                   bg="#c41c1c",
                   fg="white",
                   command=lambda index=i: oneD_selected(index))
   btn.grid(row=0, column=i, padx=8, pady=8)
   oneD_buttons[i] = btn
# =========================
# فاصل
# =========================
separator = tk.Label(root, text="-"*50, bg="#2c2c2c", fg="gray")
separator.pack(pady=10)
# =========================
# القسم الثاني: ثنائي البعد
# =========================
cinema = [
   ["A1", "A2", "A3", "A4"],
   ["B1", "B2", "B3", "B4"],
   ["C1", "C2", "C3", "C4"],
   ["D1", "D2", "D3", "D4"]
]
buttons = {}
def seat_selected(row, col):
   global selected_twoD
   if selected_twoD is not None:
       messagebox.showwarning("تنبيه", "🚫 يمكنك اختيار مقعد واحد فقط من القسم الثاني")
       return
   seat = cinema[row][col]
   buttons[(row, col)].config(bg="green", fg="white")
   selected_twoD = seat
   update_selection_label()
   message = f"""✨ تم اختيار المقعد: {seat}
📌 موقعه في المصفوفة:
cinema[{row}][{col}]"""
   messagebox.showinfo("مصفوفة ثنائية البعد", message)
label2 = tk.Label(root, text="🎬 القسم الثاني:",
                 font=("Arial", 14, "bold"),
                 fg="lightblue", bg="#2c2c2c")
label2.pack(pady=10)
frame2 = tk.Frame(root, bg="#2c2c2c")
frame2.pack()
for i in range(len(cinema)):
   for j in range(len(cinema[i])):
       btn = tk.Button(frame2,
                       text=cinema[i][j],
                       width=6,
                       height=2,
                       font=("Arial", 11, "bold"),
                       bg="#c41c1c",
                       fg="white",
                       command=lambda r=i, c=j: seat_selected(r, c))
       btn.grid(row=i, column=j, padx=8, pady=8)
       buttons[(i, j)] = btn
# =========================
# عرض الاختيارات
# =========================
selection_label = tk.Label(root,
                          text="لم يتم اختيار مقاعد بعد",
                          font=("Arial", 12, "bold"),
                          fg="white",
                          bg="#2c2c2c")
selection_label.pack(pady=15)
def update_selection_label():
   text = f"🎟 VIP: {selected_oneD if selected_oneD else '-'}   |   🎬 قاعة: {selected_twoD if selected_twoD else '-'}"
   selection_label.config(text=text)
root.mainloop()