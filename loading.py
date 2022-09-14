import os
import tkinter as tk
import time

def mainload():
    splash = tk.Tk()
    splash.resizable(width=False, height=False)
    splash.title('Pendaftaran Absensi Menggunakan Face Recognition')
    splash.iconbitmap('assets/photocameraoutline_80020.ico')

    splash = tk.Canvas(splash, width=600, height=300)
    splash.grid(columnspan=3, rowspan=8)
    splash.configure(bg='#908de0')
    judul = tk.Label(splash, text='SIAP SIAP UNTUK MENGAMBIL GAMBAR', font=('Arial',34), fg='black' ,bg='#908de0')
    note = tk.Label(splash, text='Jika aplikasi seperti membeli berarti aplikasi sedang melakukan train data', font=('Arial',34), fg='black', bg='#908de0')
    note2 = tk.Label(splash, text='Window ini akan tertutup dalam 3 detik', font=('Arial',34), fg='black', bg='#908de0')
    splash.create_window(300, 150, window=judul)
    splash.create_window(300,180, window= note)
    splash.create_window(300,210, window= note)

    splash.mainloop()
    
    splash.after(3000,lambda:splash.destroy())

