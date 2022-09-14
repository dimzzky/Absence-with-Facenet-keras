import tkinter as tk
import os

def ScanFace():
    os.system('python TakeImage.py')

def Absen():
	os.system('python Absensi.py')

def Quit():
    root.destroy()

def readme():
    os.system("start \"msedge\" \"readme.html\"")



root = tk.Tk()
root.resizable(width=False, height=False)
root.title('Absensi Menggunakan Face Recognition')
root.iconbitmap('assets/photocameraoutline_80020.ico')
# mengatur canvas (window tkinter)
canvas = tk.Canvas(root, width=400, height=500)
canvas.grid(columnspan=3, rowspan=6)
canvas.configure(bg='#e8e8a0')
#JUDUL
judul = tk.Label(root, text='SMART ABSENSI', font=('Arial',34), fg='Black' ,bg='#e8e8a0')
canvas.create_window(200, 50, window=judul)

note1 = tk.Label(root, text='SILAHKAN PILIH MENU DIBAWAH', font=('Arial',15),fg='Black',bg='#e8e8a0')
canvas.create_window(200, 180, window=note1)

note3 = tk.Label(root, text = 'Pilih DAFTAR jika merasa belum mendaftar', font=('Arial',12), fg='Black' ,bg='#e8e8a0')
canvas.create_window(200, 220, window=note3)

note4 = tk.Label(root, text = 'Jika sudah terdaftar silahkan pilih ABSENSI', font=('Arial',12), fg='Black' ,bg='#e8e8a0')
canvas.create_window(200, 250, window=note4)


Label = tk.Label(root, text = 'SELAMAT DATANG!!', font=('Arial',15), fg='Black' ,bg='#e8e8a0')
canvas.create_window(200, 120, window=Label)

# tombol untuk rekam data wajah
Rekam_text = tk.StringVar()
Rekam_btn = tk.Button(root, textvariable=Rekam_text, font='Roboto', bg='#20bebe', fg='white', height=2, width=15, command=lambda:(Quit(),ScanFace()))
Rekam_text.set('DAFTAR')
canvas.create_window(200, 300, window=Rekam_btn)

Rekam_text2 = tk.StringVar()
Rekam_btn2 = tk.Button(root, textvariable=Rekam_text2, font='roboto',bg='#20bebe', fg='white', height=2, width=15, command=Absen)
Rekam_text2.set('ABSENSI')
canvas.create_window(200, 360, window=Rekam_btn2)

help_text = tk.StringVar()
help_btn = tk.Button(root,textvariable=help_text, font='roboto', bg='white', fg='black', height=1, width=10, command=readme)
help_text.set('TUTORIAL')
canvas.create_window(85,450, window=help_btn)

keluar_text = tk.StringVar()
keluar_btn = tk.Button(root, textvariable=keluar_text, font='roboto',bg='RED', fg='white', height=1, width=10, command=Quit)
keluar_text.set('KELUAR')
canvas.create_window(320, 450, window=keluar_btn) 




root.mainloop()