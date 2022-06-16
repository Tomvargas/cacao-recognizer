import os
from tkinter import Tk, Button, Entry, PhotoImage, Label, messagebox

def help():
    messagebox.showinfo(title="Ayuda", message="El nombre de usuario debe tener almenos 4 caracteres y la contraseña al menos 6")

def singup():
    username = user.get().strip()
    passwd = pwd.get()

    if len(username) > 3 and len(passwd) > 5:
        
        filepathname = "./users/"+username+".bin"

        pahtfile = os.path.isfile(filepathname)

        if(pahtfile):
            messagebox.showinfo(title="alerta", message="Usuario ya registrado")
        else:
            file = open(filepathname, "wb")
            userdata=username+"\n"+passwd
            data = userdata.encode()   
            file.write(data)
            file.close()
            messagebox.showinfo(title="alerta", message="Registro exitoso")
    else:
        messagebox.showinfo(title="alerta", message="Debe llenar los campos")

def Validate():
    username = user.get().strip()
    passwd = pwd.get()
    data=[]

    if(len(username) > 3):
        if (len(passwd) > 5):
            filename = "./users/"+username+".bin"
            pahtfile = os.path.isfile(filename)

            if pahtfile:
                file = open(filename, "r")

                while True:
                    line = file.readline()
                    if not line:
                        break
                    data.append(line.rstrip())
                
                file.close()

                if username == data[0] and passwd == data[1]:
                    messagebox.showinfo(title="alerta", message="bienvenido "+username)
                    login.destroy()
                    os.system("main.pyw")
                    quit()
                else:
                     messagebox.showinfo(title="alerta", message="Usuario o contraseña incorrecta.")

            else:
                messagebox.showinfo(title="alerta", message="Usuario no registrado")
        else:
            messagebox.showinfo(title="alerta", message="Debe escribir una contraseña valida")
    else:
        messagebox.showinfo(title="alerta", message="Debe escribir un nombre de usuario valido")
       

login = Tk()

login.geometry("300x450")
login.title('LOGIN')
login.iconbitmap('./assets/icon.ico')
login.configure(bg = "#FFFFFF")

bg = PhotoImage(file = "./assets/loginbg.png")

label1 = Label( login, image = bg)
label1.place(x = 0, y = 0)


user = Entry(login, width=30, borderwidth = 0)
user.pack(anchor='center', pady=(115,0))


pwd = Entry(login, show="*", width=30, borderwidth = 0)
pwd.pack(anchor='center', pady=(68,0))

btnin = Button( login, text = "Iniciar sesión",height=2, width=15, fg="#ffffff", bg = "#045F6B", command=Validate, borderwidth = 0)
btnin.pack(anchor='center', pady=(30,0))

btnup = Button( login, text = "Registrarse", width=15,height=2, fg="#045F6B", bg = "#ffffff", command=singup, borderwidth = 0)
btnup.pack(anchor='center', pady=20)

Button( login, text = "Ayuda", fg="#ffffff",bg="#ffa500", width=15, borderwidth = 0, command=help ).pack(anchor='center')

login.resizable(False, False)
login.mainloop()