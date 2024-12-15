import tkinter as tk
from tkinter import messagebox
import pyttsx3
import sys

# تهيئة مكتبة تحويل النص إلى كلام
engine = pyttsx3.init()

# دالة تشغيل النص إلى كلام
def text_to_speech():
    text = entry.get()
    if text.strip():  # التأكد من وجود نص
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("warning", "Enter your text")

# دالة الخروج من البرنامج
def exit_program():
    root.destroy()
    sys.exit()

# دالة مسح النص في مربع الإدخال
def clear_entry():
    entry.delete(0, tk.END)

# إنشاء نافذة GUI
root = tk.Tk()
root.title("Text to Speech GUI")
root.geometry("400x500")  # حجم النافذة
root.resizable(True, True)  # منع تغيير حجم النافذة

# إضافة مربع النص
entry_label = tk.Label(root, text=" Enter Your Text :", font=("Arial", 12))
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

# إضافة الأزرار بجانب بعض باستخدام Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", font=("Arial", 12), bg="white", fg="black", width=10, command=text_to_speech)
play_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg="red", fg="black", width=10, command=exit_program)
exit_button.grid(row=0, column=1, padx=10)

set_button = tk.Button(button_frame, text="Set", font=("Arial", 12), bg="white", fg="black", width=10, command=clear_entry)
set_button.grid(row=0, column=2, padx=20)

# تشغيل النافذة
root.mainloop()