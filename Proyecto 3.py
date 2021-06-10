
import tkinter
from tkinter import*


def menu():
    ventana=Tk()
    ventana.geometry("400x400")
    entry=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="white", fg="Black")
    entry.pack()
    etiqueta=tkinter.Label(ventana,text="Ingrese su nombre Completo",
                           font=("Times New Roman",14),
                           bg="white", fg="Black").pack()
    entry=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="white", fg="Black")
    entry.pack()
    etiqueta=tkinter.Label(ventana,text="Ingrese su nombre de usuario",
                           font=("Times New Roman",14),
                           bg="white", fg="Black").pack()
    entry=tkinter.Entry(ventana,text="",
                        font=("Times New Roman",14),
                        bg="white", fg="Black")
    entry.pack()
    etiqueta=tkinter.Label(ventana,text="Ingrese su contraseña",
                           font=("Times New Roman",14),
                           bg="white", fg="Black").pack()
    
    boton=tkinter.Button(ventana,text="Continuar",font=("Times New Roman",14),
                         bg="white", fg="Black")
    boton.pack()
    
    

menu()
