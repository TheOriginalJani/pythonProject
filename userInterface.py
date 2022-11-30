import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import qrCode


# Fájl kiválasztása
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


# Fájl típusának ellenőrzése
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


# Rejtjelező gomb parancsa
def encodeFile():
    try:
        newFilePath = qrCode.encoder()
        messagebox.showinfo(title="Siker", message=f"Elkészült a QR-kód!\n\n{newFilePath}")
    except:
        messagebox.showerror(title="Hiba", message="Nem sikerült elkészíteni a QR-kódot!")


# Megfejtő gomb parancsa
def decodeFile():
    try:
        newFilePath = qrCode.decoder()
        messagebox.showinfo(title="Siker", message=f"Elkészült a szöveges fájl!\n\n{newFilePath}")
    except:
        messagebox.showerror(title="Hiba", message="Nem sikerült elkészíteni a szöveges fájlt!")


# Ablak beállítása
window = tk.Tk()
window.title('QR code encoder / decoder')
window.resizable(False, False)
window.configure(bg='#4B0082')
icon = PhotoImage(file='./venv/Images/QRcode.png')
window.iconphoto(False, icon)

# UI elemek

# 0. sor
lbl_emptySpaceUp = Label(
    state="disable",
    font='Helvetica 20 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

# 1. sor
lbl_Title = Label(
    text='QR-kód rejtjelező és megfejtő',
    font='Helvetica 36 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

# 2. sor
lbl_emptySpaceDown = Label(
    state="disable",
    font='Helvetica 20 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

# 3. sor
lbl_fileNameLabel = Label(
    text='Fájl neve:',
    width=15,
    font='Helvetica 20 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

ntry_fileName = Entry(
    width=30,
    state='disable',
    font='Helvetica 20 bold',
    disabledbackground='#4B0082',
    disabledforeground='#00FF7F'
)

btn_setFile = Button(
    text='Fájl választása',
    width=15,
    command=select_file,
    font='Helvetica 20 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

# 4. sor
frm_coders = Frame(
    master=window,
    bg='#4B0082',
)

btn_encoder = tk.Button(
    master=frm_coders,
    text='Rejtjelez',
    state="disable",
    width=30,
    command=encodeFile,
    font='Helvetica 20 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

btn_decoder = tk.Button(
    master=frm_coders,
    text='Megfejt',
    state="disable",
    width=30,
    command=decodeFile,
    font='Helvetica 20 bold',
    bg='#4B0082',
    fg='#00FF7F'
)

lbl_emptySpaceUp.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)
lbl_Title.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)
lbl_emptySpaceDown.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

lbl_fileNameLabel.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
ntry_fileName.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
btn_setFile.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

frm_coders.grid(row=4, column=0, padx=5, pady=5, columnspan=3)
btn_encoder.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
btn_decoder.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

window.mainloop()
