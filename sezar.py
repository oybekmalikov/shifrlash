import tkinter as tk
from tkinter import Frame, Label, Entry, Button

class SEZAR:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Sezar Shifrlash")
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
        etext = ''
        try:
            key = int(self.key_line.get())
        except ValueError:
            self.key_line.config(bg='red')
            return
        self.key_line.config(bg='white')
        for char in text:
            etext += chr((ord(char) + key) % 256)
        self.shifr_line.delete(0, tk.END)
        self.shifr_line.insert(0, etext)

    def deshifrlash(self):
        text = self.text_enter.get()
        etext = ''
        try:
            key = int(self.key_line.get())
        except ValueError:
            self.key_line.config(bg='red')
            return
        self.key_line.config(bg='white')
        for char in text:
            etext += chr((ord(char) + key) % 256)
        de_text = ""
        for char in etext:
            de_text += chr((ord(char) - key) % 256)
        self.deshifr_line.delete(0, tk.END)
        self.deshifr_line.insert(0, de_text)

    def show(self):
        self.window.deiconify()
