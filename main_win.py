import tkinter as tk
from tkinter import Button
from sezar import SEZAR
from vijiner import Viginer

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        self.v_main_frame = tk.Frame(root)
        self.v_main_frame.pack(pady=20)

        self.sezar_btn = Button(self.v_main_frame, text='Sezar', command=self.sezar)
        self.sezar_btn.pack(pady=10)

        self.viji_btn = Button(self.v_main_frame, text='Vijiner', command=self.vijiner)
        self.viji_btn.pack(pady=10)

    def sezar(self):
        self.szr = SEZAR()
        self.szr.show()

    def vijiner(self):
        self.vnr = Viginer()
        self.vnr.show()
