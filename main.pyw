from tkinter import Tk, Button, PhotoImage, Label, messagebox, Toplevel
import cv2
from PIL import Image, ImageTk
import imutils
import os
from serial import Serial

try:
    arduino = Serial("COM6", 9600)
except:
    print("No arduino connect")

def LogOut():
    global cap
    cap.release()
    window.destroy()
    os.system("login.pyw")

def alerts():
    alrt = Toplevel(window)
    alrt.title("Recomendaciones")
    alrt.geometry("861x600")
    alrt.iconbitmap('./assets/icon.ico')
    
    Label( alrt, image = bg2).place(x = 0, y = 0)
    #Label(alrt, text="RECOMENDACIONES PARA TENER UN BUEN CULTIVO").pack()
    
    #num+=1
    #window.after(1000, getBad)

def stream():
    global cap
    #si usa camara integrada use 0
    #si no tiene camara y conecta una use 0
    #si tiene camara integrada y va a usar camara usb ingrese 1
    cap = cv2.VideoCapture(2,cv2.CAP_DSHOW)
    iniciar()

def iniciar():
    global cap
    global cacaoCascade
    global cacao2Cascade
    global numb
    global nbuenos
    global nmalos
    global arduino

    ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=500)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)

        obj = cacao2Cascade.detectMultiScale(frame,
        scaleFactor = 2,
        minNeighbors = 50,
        minSize=(90,20))

        cv2.rectangle(frame, (350,0),(348,400),(255,0,0),2)

        cv2.rectangle(frame, (280,0),(270,400),(0,0,255),2)
     
        color = frame2[180, 180]
        #print(type(color[0]))

        for (x,y,w,h) in obj:
            cv2.circle(frame, (x+120,y+80), 2, (255, 0, 0), 2)

            if(x+w == 349):
                numb+=1

            if(x+120 > 269 and x+120 < 281):
                for a in color:
                    for b in color:
                        for z in color:
                            a, b, z = int(a), int(b), int(z)
                            if (
                                (a>=353 and a<=343 and b>=58 and b<=37 and z>=27 and z<=40) or
                                (a>=344 and a<=347 and b>=26 and b<=65 and z>=49 and z<=97) or 
                                (a>=11 and a<=30 and b>=40 and b<=71 and z>=93 and z<=98) or 
                                (a>=21 and a<=26 and b>=54 and b<=65 and z>=50 and z<=76)
                            ):
                                #print(a,"-",b,"-",z)
                                nbuenos+=1
                                arduino.write(b'3')


                            elif(
                                (a>=21 and a<=32 and b>=19 and b<=55 and z>=27 and z<=35) or 
                                (a>=38 and a<=46 and b>=11 and b<=20 and z>=69 and z<=85) or
                                (a>=38 and a<=46 and b>=11 and b<=20 and z>=69 and z<=85)
                            ):
                                nmalos+=1
                                #print(a,"-",b,"-",z) 
                                arduino.write(b'3')          

            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,'Cacao',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
            
        cv2.putText(frame,str(numb),(420,350),1,4,(0,0,0),2,cv2.LINE_AA)

        bad.configure(text=nmalos) 
        good.configure(text=nbuenos) 

        img = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=img)
        camtag.configure(image=image) 
        camtag.image = image
        camtag.after(10, iniciar)

def on_of_platform():
    
    global arduino

    global value

    if value==1:
        value=0
        print("stop platforrm")
        btnlplay.configure(image=playbtn)
        #write in serial monitor
        arduino.write(b'0')
        
    elif(value==0):
        value=1
        print("play platform")
        btnlplay.configure(image=pausebtn)
        #write in serial monitor
        arduino.write(b'1')
        


def inf():
    txt="author: Tomás Vargas/nYou can find repository on/nhttps://github.com/tomvargas/cacao-recognizer"    
    messagebox.showinfo(title="Información", message=txt)


cap = None
cacaoCascade = cv2.CascadeClassifier('./traindata/cascade.xml')
cacao2Cascade = cv2.CascadeClassifier('./traindata/cascade3.xml')
value = 0
num = 1
numb, nbuenos, nmalos = 0, 0, 0

window = Tk()


window.geometry("737x524")
window.title('estado del cacao')
window.iconbitmap('./assets/icon.ico')
window.configure(bg = "#FFFFFF")

bg = PhotoImage(file = "./assets/bg.png")
bg2 = PhotoImage(file = "./assets/information.png")
info = PhotoImage(file = "./assets/info.png")
playbtn = PhotoImage(file = "./assets/playbtn.png")
pausebtn = PhotoImage(file="./assets/pausebtn.png")
alert = PhotoImage(file = "./assets/alert.png")
logout = PhotoImage(file = "./assets/logout.png")

label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

camtag = Label(window)
camtag.place(x = 20, y = 102)


Button(window, image=logout, bg="#ffffff", borderwidth= 0, command = LogOut).place(x=556, y=19)
btnlInfo = Button( window, image = info, bg = "#ffffff", borderwidth = 0, command=inf)
btnlInfo.place(x = 676, y = 19)

alertbtn = Button(window, image = alert, bg = "#ffffff", borderwidth = 0, command=alerts)
alertbtn.place(x=616, y=21)

btnlplay = Button( window, image = playbtn, bg = "#ffffff", borderwidth = 0, command=on_of_platform)
btnlplay.place(x = 541.91, y = 103.37)

title = Label(window, text="GRUPO 2", bg = "#ffffff", font=("Arial", 25, "bold"))
title.place(x= 36, y=19)


good = Label(window, text="0", bg = "#ffffff", fg="#045F6B", font=("Arial", 30, "bold"))
good.place(x= 570, y=285)

bad = Label(window, text="0", bg = "#ffffff", fg="#045F6B", font=("Arial", 30, "bold"))
bad.place(x= 570, y=428)
#getBad()

# video en tiempo real
stream()

window.resizable(False, False)
window.mainloop()
