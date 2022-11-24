import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import qrCode


def select_file():
    filetypes = (
        ('Minden fájl', '*.*'),
        ('Szöveg fájl', '*.txt'),
        ('Kép fájl', '*.png')
    )

    filename = askopenfilename(
        title='Válassz egy fájlt',
        initialdir='/',
        filetypes=filetypes)

    if filename == "":
        if ntry_fileName["text"] == "":
            messagebox.showerror(title="Hiba", message="Válassz fájlt!")
        return

    ntry_fileName.config(state='normal')
    ntry_fileName.delete(0, END)
    ntry_fileName.insert(0, filename)
    ntry_fileName.config(state='disable')
    fileType(filename)


def fileType(path):
    qrCode.path = path
    if path.endswith('.txt'):
        btn_decoder.config(state='disable')
        btn_encoder.config(state='normal')
    elif path.endswith('.png'):
        btn_encoder.config(state='disable')
        btn_decoder.config(state='normal')
    else:
        btn_encoder.config(state='disable')
        btn_decoder.config(state='disable')
        messagebox.showerror(title="Hiba", message="Nem megfelelő fájlformátum!")


def encodeFile():
    try:
        newFilePath = qrCode.encoder()
        messagebox.showinfo(title="Siker", message=f"Elkészült a QR-kód!\n{newFilePath}")
    except:
        messagebox.showerror(title="Hiba", message="Nem sikerült elkészíteni a QR-kódot!")


def decodeFile():
    try:
        newFilePath = qrCode.decoder()
        messagebox.showinfo(title="Siker", message=f"Elkészült a szöveges fájl!\n{newFilePath}")
    except:
        messagebox.showerror(title="Hiba", message="Nem sikerült elkészíteni a szöveges fájlt!")


# Ablak beállítása
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
lbl_fileNameLabel = Label(
    text='Fájl neve:',
    width=15
)

ntry_fileName = Entry(
    width=30,
    state='disable'
)

btn_setFile = Button(
    text='Fájl választása',
    width=15,
    command=select_file
)

# 2. sor
frm_coders = Frame(
    master=window,
)

btn_encoder = tk.Button(
    master=frm_coders,
    text='Encoder',
    state="disable",
    width=30,
    command=encodeFile
)

btn_decoder = tk.Button(
    master=frm_coders,
    text='Decoder',
    state="disable",
    width=30,
    command=decodeFile
)

lbl_Title.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

lbl_emptySpace.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

lbl_fileNameLabel.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
ntry_fileName.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
btn_setFile.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

frm_coders.grid(row=3, column=0, padx=5, pady=5, columnspan=3)
btn_encoder.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
btn_decoder.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

window.mainloop()
