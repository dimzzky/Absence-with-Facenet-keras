#untuk memanggil data dari directory
import os
import numpy as np
import pickle
from os import listdir
from numpy import asarray, expand_dims
from keras.models import load_model
from datetime import datetime


# Library Image Processing
from PIL import Image
import cv2


# Absensi
def markAttendance(identity):
        with open('Attendance.csv', 'r+') as f:
            namesDatalist = f.readlines()
            namelist = []
            for line in namesDatalist:
                entry = line.split(',')
            if identity not in namelist:
                dtString = datetime.now()
                Time = dtString.strftime('%X')
                f.writelines(f'\n{identity},{Time}')
                namelist.append(entry[0])


def Absence():
    # Import Model
    cascade = cv2.CascadeClassifier('Assets/model/cascade/haarcascade_frontalface_default.xml')
    FaceNet = load_model('Assets/model/keras/facenet_keras.h5')

    # Membuka Lokal Database
    myfile = open("Assets/train/train.pkl", "rb")
    database = pickle.load(myfile)
    myfile.close()

    # Membuat kamera
    cam = cv2.VideoCapture(1)
    codec = cv2.VideoWriter_fourcc(	'M', 'J', 'P', 'G'	)
    cam.set(6, codec)
    cam.set(5, 60)
    cam.set(3, 1280)
    cam.set(4, 720)

    while(1):
        _, gambar = cam.read()

        wajah = cascade.detectMultiScale(gambar,1.1,4)

        if len(wajah)>0:
            x1, y1, width, height = wajah[0]
        else:
            x1, y1, width, height = 1, 1, 10, 10
        
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height

        gbr = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
        gbr = Image.fromarray(gbr)                  # konversi dari OpenCV ke PIL
        gbr_array = asarray(gbr)

        face = gbr_array[y1:y2, x1:x2] 

        face = Image.fromarray(face)                       
        face = face.resize((160,160))
        face = asarray(face)

        face = face.astype('float32')
        mean, std = face.mean(), face.std()
        face = (face - mean) / std

        face = expand_dims(face, axis=0)
        sign = FaceNet.predict(face)

        min_dist=100
        identity=' '
        for name, value in database.items() :
            dist = np.linalg.norm(value-sign) 
            if dist < min_dist:
                min_dist = dist
                identity = name
        
        if min_dist > 0.4: 
            cv2.putText(gambar,identity, (x1,y1 - 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
            cv2.rectangle(gambar,(x1,y1),(x2,y2), (0,255,0), 1)
        else:
            cv2.putText(gambar,'tidak dikenal', (100,100),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
            # cv2.rectangle(gambar,(x1,y1),(x2,y2), (0,255,0), 1)
            
        cv2.putText(gambar,'Tekan Enter untuk Absensi / Tekan Esc untuk keluar dari kamera', (100, 640),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)   
        cv2.imshow('Absensi',gambar)

        

        k = cv2.waitKey(1) 
        if k == 13: # jika menekan tombol enter akan mengambil absensi
            markAttendance(identity)
        elif k == 27:  # jika menekan tombol esc akan berhenti
            break

        
    cv2.destroyAllWindows()
    cam.release()

Absence()