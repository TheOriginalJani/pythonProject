import tkinter as tk
from tkinter import *

# Ablak beállításai
window = tk.Tk()
window.title('QR code encoder / decoder')
window.resizable(False, False)
icon = PhotoImage(file='./venv/Images/QRcode.png')
window.iconphoto(False, icon)

# UI elemek
lbl_Title = Label(
    text='QR code encoder / decoder',
    font='Helvetica 36 bold'
)

lbl_emptySpace = Label(
    state="disable")

# 1. sor
lbl_actualFileLabel = Label(
    text='Aktuális fájl:',
    width=15
)

lbl_actualFileName = Entry(
    width=30,
    state='disable'
)

btn_setFile = Button(
    text='Fájl választása',
    width=15
)

# 2. sor
frm_coders = Frame(
    master=window,
)

btn_encodeFile = tk.Button(
    master=frm_coders,
    text='Encode',
    state="disable",
    width=30
)

btn_decodeFile = tk.Button(
    master=frm_coders,
    text='Decode',
    state="disable",
    width=30
)

lbl_Title.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

lbl_emptySpace.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

lbl_actualFileLabel.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
lbl_actualFileName.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
btn_setFile.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

frm_coders.grid(row=3, column=0, padx=5, pady=5, columnspan=3)
btn_encodeFile.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
btn_decodeFile.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

window.mainloop()
