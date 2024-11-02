import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox

class Viginer:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Viginer Cipher")
        self.v_main_frame = Frame(self.window)
        self.v_main_frame.pack(padx=10, pady=10)

        self.txt_eny = Label(self.v_main_frame, text="Text kiriting:")
        self.txt_eny.grid(row=0, column=0)
        self.text_enter = Entry(self.v_main_frame, width=30)
        self.text_enter.grid(row=0, column=1)

        self.key_lab = Label(self.v_main_frame, text="Key kiriting:")
        self.key_lab.grid(row=1, column=0)
        self.key_line = Entry(self.v_main_frame, width=30)
        self.key_line.grid(row=1, column=1)

        self.btn_shifr = Button(self.v_main_frame, text="Shifrlash", command=self.shifrlash)
        self.btn_shifr.grid(row=2, column=0, pady=10)
        self.btn_deshifr = Button(self.v_main_frame, text="Deshifrlash", command=self.deshifrlash)
        self.btn_deshifr.grid(row=2, column=1, pady=10)

        self.shifr_lab = Label(self.v_main_frame, text="Shifrlangan:")
        self.shifr_lab.grid(row=3, column=0)
        self.shifr_line = Entry(self.v_main_frame, width=30)
        self.shifr_line.grid(row=3, column=1)

        self.deshifr_lab = Label(self.v_main_frame, text="Deshifrlangan:")
        self.deshifr_lab.grid(row=4, column=0)
        self.deshifr_line = Entry(self.v_main_frame, width=30)
        self.deshifr_line.grid(row=4, column=1)

    def shifrlash(self):
        text = self.text_enter.get()
        key = self.key_line.get()
        if len(key) > len(text):
            messagebox.showinfo("Info", "Key textdan uzun bulishi mumkinmas")
            return
        e_text = ""
        key = (key * (len(text) // len(key) + 1))[:len(text)]
        for i in range(len(text)):
            x = (ord(text[i]) + ord(key[i])) % 256
            e_text += chr(x)
        self.shifr_line.delete(0, tk.END)
        self.shifr_line.insert(0, e_text)

    def deshifrlash(self):
        text = self.text_enter.get()
        key = self.key_line.get()
        if len(key) > len(text):
            messagebox.showinfo("Info", "Key textdan uzun bulishi mumkinmas")
            return
        e_text = ""
        key = (key * (len(text) // len(key) + 1))[:len(text)]
        for i in range(len(text)):
            x = (ord(text[i]) + ord(key[i])) % 256
            e_text += chr(x)
        de_text = ""
        key = (key * (len(e_text) // len(key) + 1))[:len(e_text)]
        for i in range(len(e_text)):
            y = (ord(e_text[i]) - ord(key[i])) % 256
            de_text += chr(y)
        self.deshifr_line.delete(0, tk.END)
        self.deshifr_line.insert(0, de_text)

    def show(self):
        self.window.deiconify()
