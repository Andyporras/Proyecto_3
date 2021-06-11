
import tkinter
from tkinter import*
from tkinter import messagebox


def menu():
    ventana=Tk()
    ventana.geometry("400x400")
    ventana.title("Menú Inicio")
    ventana.config(bg="SteelBlue3", cursor="hand2")

    tkinter.Label(ventana, text="۝   CONTROL DE ACCESO   ۝",
                  font=("Times New Roman", 18),bg="RoyalBlue2" ,
                  fg="Black").pack(fill=tkinter.X)
    etiqueta=tkinter.Label(ventana,
                           text="¡Bienvenido al juego!\n Por favor llenar los campos requeridos\nPara empezar a jugar",
                           font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=45,y=32)
    tkinter.Label(ventana, text="- - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -" ,
                  font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=10,y=100)

    entry1=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="SteelBlue1", fg="Black")
    entry1.place(x=105,y=160)
    etiqueta=tkinter.Label(ventana,text="Ingrese su nombre Completo:",
                           font=("Times New Roman",14),
                           bg="SteelBlue3", fg="Black").place(x=85,y=130)
    entry2=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="SteelBlue1", fg="Black")
    entry2.place(x=105,y=220)
    etiqueta=tkinter.Label(ventana,text="Ingrese su nombre de Usuario:",
                           font=("Times New Roman",14),
                           bg="SteelBlue3", fg="Black").place(x=85,y=190)
    entry3=tkinter.Entry(ventana,text="",show="*",
                        font=("Times New Roman",14),
                        bg="SteelBlue1", fg="Black")
    entry3.place(x=105,y=280)
    etiqueta=tkinter.Label(ventana,text="Ingrese su Contraseña:",
                           font=("Times New Roman",14),
                           bg="SteelBlue3", fg="Black").place(x=111,y=250)
    def controlDeAcceso():
        nombre=entry1.get()
        usuario=entry2.get()
        contraseña=entry3.get()
        archivo=open("acceso.txt")
        datos=archivo.readlines()
        if(nombre+"\n")in datos:
            indice=datos.index(nombre+"\n")
            if(usuario+"\n")== datos[indice+1]:
                if(contraseña+"\n")==datos[indice+2]:
                    ventana.destroy()
                else:
                    messagebox.showerror("error","Contraseña incorrecta") 
            else:
                 messagebox.showerror("error","Usuario incorrecto")
        else:
             messagebox.showerror("error","Nombre incorrect0")
            
    
    boton=tkinter.Button(ventana,text="Continuar",font=("Times New Roman",14),
                         bg="DeepSkyBlue4", fg="Black",command=controlDeAcceso)
    boton.place(x=160,y=320)
    
    

menu()
