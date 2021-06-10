
import tkinter
from tkinter import*


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

    entry=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="SteelBlue1", fg="Black")
    entry.place(x=105,y=160)
    etiqueta=tkinter.Label(ventana,text="Ingrese su nombre Completo:",
                           font=("Times New Roman",14),
                           bg="SteelBlue3", fg="Black").place(x=85,y=130)
    entry=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="SteelBlue1", fg="Black")
    entry.place(x=105,y=220)
    etiqueta=tkinter.Label(ventana,text="Ingrese su nombre de Usuario:",
                           font=("Times New Roman",14),
                           bg="SteelBlue3", fg="Black").place(x=85,y=190)
    entry=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="SteelBlue1", fg="Black")
    entry.place(x=105,y=280)
    etiqueta=tkinter.Label(ventana,text="Ingrese su Contraseña:",
                           font=("Times New Roman",14),
                           bg="SteelBlue3", fg="Black").place(x=111,y=250)
    
    boton=tkinter.Button(ventana,text="Continuar",font=("Times New Roman",14),
                         bg="DeepSkyBlue4", fg="Black")
    boton.place(x=160,y=320)
    
    

menu()
