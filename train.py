#untuk memanggil data dari directory
import os
from os import listdir
from numpy import asarray, expand_dims
from keras.models import load_model
import numpy as np
import pickle
import random

# Library Image Processing
from PIL import Image
import cv2

# GUI
import tkinter as tk

def rekamWajah():
    kRandom = random.randint(0, 999999)
    faceDir = 'Assets/data/'
    camera = cv2.VideoCapture(1)
    codec = cv2.VideoWriter_fourcc(	'M', 'J', 'P', 'G'	)
    camera.set(6, codec)
    camera.set(5, 60)
    camera.set(3, 1280)
    camera.set(4, 720)

    cascade = cv2.CascadeClassifier('Assets/model/cascade/haarcascade_frontalface_default.xml')
    while(1):
        retV, gambar = camera.read()
        abuabu = cv2.cvtColor(gambar, cv2.COLOR_BGR2BGRA)
        wajah = cascade.detectMultiScale(abuabu, 1.1, 4)
        for (x,y,w,h) in wajah:
            jumlah = 0
            gambar = cv2.rectangle(gambar, (x,y), (x+w, y+h), (107, 235, 52), 2)
            namaFile = str(entry1.get()) + '.' + str(entry2.get()) +'.'+str(kRandom)++'.jpg'
            cv2.imwrite(faceDir +'/'+ namaFile , abuabu[y:y+h, x:x+w])
            cv2.putText(gambar,'Tekan ENTER untuk Ambil Gambar', (360, 640),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow('Mengambil', gambar)
            


        k = cv2.waitKey(1)
        if k == 13: #Tombol Enter untuk ambil gambar
            break


    
    camera.release()
    cv2.destroyAllWindows()


def trainWajah():
    #Training Gambar
    FaceNet = load_model('Assets/model/keras/facenet_keras.h5')     
    cascade = cv2.CascadeClassifier('Assets/model/cascade/haarcascade_frontalface_default.xml')
    # Proses Training
    FaceDir='assets/data/'
    database = {}

    for filename in listdir(FaceDir):
        if filename.endswith('png') or filename.endswith('jpg'):
            path = FaceDir
            gambar = cv2.imread(FaceDir + filename)
        
            wajah = cascade.detectMultiScale(gambar,1.1,4)
        
            if len(wajah)>0:
                x1, y1, width, height = wajah[0]         
            else:
                x1, y1, width, height = 1, 1, 10, 10
                
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            
            gbr = cv2.cvtColor(gambar, cv2.COLOR_RGB2BGR)
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
            
            database[os.path.basename(filename).split('.',1)[0]]=sign

    myfile = open('Assets/train/train.pkl', 'wb')
    pickle.dump(database, myfile)
    myfile.close()
    # print(database)
    print('Train Complete')

trainWajah()