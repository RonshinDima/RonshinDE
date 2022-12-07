import tkinter as tk
from tkinter import *
from tkinter import messagebox 
import json
import requests
def info_git ():
    username = height_tf.get()
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    keys=["company", "created at", "email", "id", "name", "url"]
    with open("file.json", "w", encoding="utf-8") as file:
        for I in user_data.keys():
            if I in keys:
                (json.dump(f"{I} : {user_data[I]}", file, indent=1))
window= Tk()
window.title("ввод данных")
window.geometry("800x600")
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
height_lb = Label(
    frame,
    text="Введите имя репозитория"
)
height_lb.grid(row=3, column=1)
height_tf=Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)
cal_btn=Button(
    frame,
    text='Ввод',
    command=info_git 
)
cal_btn.grid(row=5, column=2)
window.mainloop()
