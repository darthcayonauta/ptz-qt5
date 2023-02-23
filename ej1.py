#import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import sys
from time import sleep
from onvif import ONVIFCamera
import zeep
from claseMov import *

#from claseMov import *
#vamos a agregar los componentes de los movimientos

IP = '192.168.78.90'
USER = 'admin'
PASS = 'Admin321'

ob = MoverCam(IP,USER,PASS)

def arriba():  
    ob.moves(1)

def abajo():
    ob.moves(2)
    
def izquierda():
    ob.moves(3)

def derecha():
    #print("muestra funcion")
    ob.moves(4)

def zoomIn():
    ob.moves(5)

def zoomOut():
    ob.moves(6)

def onClossing():
    root.quit()
    cap.release()
    print("camara desconectada")
    root.destroy()

def callback():
    ret,frame = cap.read()

    if ret:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img.thumbnail((704,576))
        tkimage= ImageTk.PhotoImage(img)
        label.configure(image=tkimage)
        label.image=tkimage
        root.after(1,callback)
    else:
        onClossing()

url = f"rtsp://{USER}:{PASS}@{IP}:554/h264/ch1/sub/av_stream"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Cámara Inicializada")
else:
    sys.exit("Cámara Desconectada")

root = Tk()
#root.protocol("WM_DELETE_WINDOW",onClossing())
root.title("Moviendo camaras")
label = Label(root)
label.grid(row=0)

#botones
b1 = Button(root,text="UP",width=5,height=2,command=lambda:arriba())
b2 = Button(root,text="DOWN",width=5,height=2,command=lambda:abajo())
b3 = Button(root,text="LEFT",width=5,height=2,command=lambda:izquierda())
b4 = Button(root,text="RIGHT",width=5,height=2,command=lambda:derecha())
b5 = Button(root,text="ZOOM IN",width=10,height=2,command=lambda:zoomIn())
b6 = Button(root,text="ZOOM OUT",width=10,height=2,command=lambda:zoomOut())

b1.grid(row=1,column=2,padx=5, pady=5)
b3.grid(row=2,column=1,padx=5, pady=5) #left
b4.grid(row=2,column=3,padx=5, pady=5) #right
b2.grid(row=3,column=2,padx=5, pady=5)
b5.grid(row=5,column=1,padx=5, pady=5)
b6.grid(row=5,column=3,padx=5, pady=5)

root.after(1,callback)
root.mainloop()

