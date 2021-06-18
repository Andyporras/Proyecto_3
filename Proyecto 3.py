
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from random import choice
import random

"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""
class Archivos:
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def __init__(self):
        self.Acceso=open("acceso.txt")
        self.Luchadores=open("Luchadores.txt")
        self.DatoLuchadores=self.Luchadores.readlines()
        self.Torneos=open("Torneos.txt")
        self.DatoTorneos=self.Torneos.readlines()
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def datosAcceso(self):
        return self.Acceso.readlines()
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def BuscarIndiceLuchadores(self,buscar):
        datos=self.DatoLuchadores
        return datos.index(buscar)
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def BuscarDatosLuchadores(self,buscar):
        for linea in self.DatoLuchadores:
            if(linea == buscar):
                return False
            else:
                continue
        return True
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def EliminarLuchador(self,eliminar,indice):
        datos=a.DatoLuchadores
        cont=0
        
        while len(datos)>=indice:
            if(datos[indice]==eliminar):
                while cont!=15:
                    datos.pop(indice-3)
                    cont+=1
                return Convertir_A_String(datos)
            else:
                indice+=15
#---------------------------------------------------------------------------------------------------        
"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""             
def Convertir_A_String(lista):
    if isinstance(lista, list):#El parámetro de entrada debe de ser una lista(restricción).
        string = ""
        for linea in lista:
            string += linea
        return string
    else:#Se imprime el error en el caso de que el parámetro de entrada no cumple con las restriciones predeterminadas.
        #print("Error: No se puede convertir a string, debido a que el tipo de dato de entrada no es una lista.")
        None

"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""            
#PUNTO C#-----------------------------------------------------------------------------
class DefiniciónDeLosPersonajes:
    def __init__(self):
        
        self.Tipo=[]
        self.Sexo=[]
        self.Hombre=[]
        self.AlterEgo=[]
        self.velocidad=[]
        self.Fuerza=[]
        self.Inteligencia=[]
        self.DefensaPersonal=[]
        self.Magia=[]
        self.Telepatia=[]
        self.Estrategia=[]
        self.Volar=[]
        self.Elasticidad=[]
        self.Regeneracion=[]

        A=Archivos()
        Personajes=A.DatoLuchadores
        cont=0
        for linea in Personajes:
            #print(linea)
            #print(cont)
            if(cont==0):
                self.Tipo+=[linea[5:-1]]
                cont+=1
            elif(cont==1):
                self.Sexo+=[linea[5:-1]]
                cont+=1
            elif(cont==2):
                self.Hombre=[linea[16:-1]]
                cont+=1
            elif(cont==3):
                self.AlterEgo+=[linea[23:-1]]
                cont+=1
            elif(cont==4):
                self.velocidad+=[linea[10:-1]]
                cont+=1
            elif(cont==5):
                self.Fuerza+=[linea[7:-1]]
                cont+=1
            elif(cont==6):
                self.Inteligencia+=[linea[13:-1]]
                cont+=1
            elif(cont==7):
                self.DefensaPersonal+=[linea[18:-1]]
                cont+=1
            elif(cont==8):
                self.Magia+=[linea[7:-1]]
                cont+=1
            elif(cont==9):
                self.Telepatia+=[linea[10:-1]]
                cont+=1
            elif(cont==10):
                self.Estrategia+=[linea[11:-1]]
                cont+=1
            elif(cont==11):
                self.Volar+=[linea[6:-1]]
                cont+=1
            elif(cont==12):
                self.Elasticidad+=[linea[6:-1]]
                cont+=1
            elif(cont==13):
                self.Regeneracion+=[linea[13:-1]]
                cont+=1
            else:
                cont=0
                
#---------------------------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """          
    def verAlterEgo(self):
        return self.AlterEgo

#---------------------------------------------------------------------------------------------------
"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""
#PUNTO D#----------------------------------------------------------------------------------------
class DefiniciónDelTorneo:#Punto d
    def __init__(self,nombre,fecha,lugar,numero,luchas):
        self.NombreDelTorneo=nombre
        self.Fecha=fecha
        self.LugarDelTorneo=lugar
        self.NumeroDeLuchas=numero
        self.Luchas=luchas
        self.BandoGanador=[]
#---------------------------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def Mostrar(self):
        print(self.NombreDelTorneo)
        print(self.Fecha)
        print(self.LugarDelTorneo)
        print(self.NumeroDeLuchas)
        print(self.Luchas)
        

#---------------------------------------------------------------------------------------------------              
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def agregarPersonajes(self):
        return 


#---------------------------------------------------------------------------------------------------
"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""
#PUNTO E#-------------------------------------------------------------------------------------------
class DefiniciónDeLasLuchas: #Punto e
    def __init__(self,luchador1,luchador2,Round1,Round2,Round3,ganador):
        
        self.alterEgoDePrimerLuchador =luchador1
        self.alterEgoDelSegundoLuchador=luchador2
        self.Ganador1erRound=Round1
        self.Ganador2doRound=Round2
        self.Ganador3erRound=Round3
        self.GanadorDeLaLucha=ganador

#---------------------------------------------------------------------------------------------------    
"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""      
class GranTorino(Archivos):
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def menu(self):
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
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
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
                        
                        M.menuInicial()
                    else:
                        messagebox.showerror("error","Contraseña incorrecta")
                else:
                     messagebox.showerror("error","Usuario incorrecto")
                     
            else:
                 messagebox.showerror("error","Nombre incorrecto")
                 
                
        
        boton=tkinter.Button(ventana,text="Continuar",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black",command=controlDeAcceso)
        boton.place(x=160,y=320)
#-----------------------------------------------------------------------------------------------
#Ventana del menu principal/Inicial
"""
Nombre:
Entrada:
Salida:
Restriccion:
Objetivo:
"""
class MenuPrincipal:
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def __init__(self):
        self.Torneos=[]
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def mostrarTorneos(self):
        for dato in self.Torneos:
            dato.Mostrar()
#---------------------------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def menuPersonaje(self):
        vtnPersonaje=Tk()
        vtnPersonaje.geometry("400x450")
        vtnPersonaje.title("Menú Personajes")
        vtnPersonaje.config(bg="SteelBlue3", cursor="hand2")

        tkinter.Label(vtnPersonaje, text="۝   CREACIÓN DE PERSONAJE   ۝",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)
        etiqueta=tkinter.Label(vtnPersonaje,
                               text="Crea tu Personaje",
                               font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=130,y=32)

        etiqueta=tkinter.Label(vtnPersonaje, text="Selecciona un Tipo:",
                               font=("Times New Roman",14),bg="SteelBlue3",
                               fg="Black").place(x=130,y=70)
        comboHV=ttk.Combobox(vtnPersonaje, values=("Héroe", "Villano"))
        comboHV.place(x=135,y=100)
        #
        etiqueta=tkinter.Label(vtnPersonaje, text="Selecciona el Sexo:",
                               font=("Times New Roman",14),bg="SteelBlue3",
                               fg="Black").place(x=130,y=130)
        comboHV2=ttk.Combobox(vtnPersonaje, values=("Mujer", "Hombre","No determinado"))
        comboHV2.place(x=135,y=160)
        #
        etiqueta=tkinter.Label(vtnPersonaje,text="Escriba el nombre del Personaje:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=90,y=190)
        entry4=tkinter.Entry(vtnPersonaje,text="",
                            font=("Times New Roman",14),
                            bg="SteelBlue1", fg="Black")
        entry4.place(x=120,y=220)
        #
        etiqueta=tkinter.Label(vtnPersonaje,text="Escriba el alter ego de su Personaje:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=80,y=250)
        alterEgo=tkinter.Entry(vtnPersonaje,text="",
                            font=("Times New Roman",14),
                            bg="SteelBlue1", fg="Black")
        alterEgo.place(x=120,y=280)
        #
        boton=tkinter.Button(vtnPersonaje,text="Eliminar Personaje Existente",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black",command= eliminarPersonaje).place(x=10,y=400)

        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def validarPersonaje():
            a=Archivos()
            
            if(a.BuscarDatosLuchadores("Nombre de su alter ego:"+alterEgo.get()+"\n")):

                return menuPersonaje2(comboHV.get(),comboHV2.get(),entry4.get(),alterEgo.get())

                
            else:
                messagebox.showerror("Error","El alter ego de su personaje ya existe")
                    
        
        boton=tkinter.Button(vtnPersonaje,text="Continuar\nCreacion",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black", command=validarPersonaje)
        boton.place(x=160,y=320)
#---------------------------------------------------------------------------------------------------
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def menuPersonaje2(tipo,sexo,nombre,alterEgo):
            vtnPersonaje.destroy()
            vtnPersonaje2=Tk()
            vtnPersonaje2.geometry("500x600")
            vtnPersonaje2.title("Menú Personajes")
            vtnPersonaje2.config(bg="SteelBlue3", cursor="hand2")

            tkinter.Label(vtnPersonaje2, text="۝    CREACIÓN DE PERSONAJE    ۝",
                          font=("Times New Roman", 18),bg="RoyalBlue2" ,
                          fg="Black").pack(fill=tkinter.X)
            etiqueta=tkinter.Label(vtnPersonaje2,
                                   text="Crea tu Personaje",
                                   font=("Times New Roman",14),bg="SteelBlue3", fg="blue4").place(x=190,y=32)
            etiqueta=tkinter.Label(vtnPersonaje2,
                                   text="Escribe el numero de la cantidad de habilidades\nque le quieres agregar a tu personaje\nEl total de estas debe ser igual a -100-",
                                   font=("Times New Roman",13),bg="SteelBlue3", fg="blue4").place(x=80,y=60)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Velocidad",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=50,y=130)
            entry5=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry5.place(x=10,y=160)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Fuerza",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=55,y=200)
            entry6=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry6.place(x=10,y=230)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Inteligencia",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=55,y=270)
            entry7=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry7.place(x=10,y=300)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Defensa Personal",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=40,y=350)
            entry8=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry8.place(x=10,y=380)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Magia",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=55,y=420)
            entry9=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry9.place(x=10,y=450)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Telepatía",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=250,y=130)
            entry10=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry10.place(x=200,y=160)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Estrategia",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=250,y=200)
            entry11=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry11.place(x=200,y=230)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Volar",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=250,y=270)
            entry12=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry12.place(x=200,y=300)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Volar",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=250,y=350)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Elasticidad",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=250,y=350)
            entry14=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry14.place(x=200,y=380)
            #
            etiqueta=tkinter.Label(vtnPersonaje2,text="Regeneración",
                               font=("Times New Roman",12),
                               bg="SteelBlue3", fg="Black").place(x=250,y=420)
            entry15=tkinter.Entry(vtnPersonaje2,text="",
                                    font=("Times New Roman",12),
                                    bg="SteelBlue1", fg="Black")
            entry15.place(x=200,y=450)
            
            """
            Nombre:
            Entrada:
            Salida:
            Restriccion:
            Objetivo:
            """
            def validarPoderes():
                suma=0
                suma+=int(entry5.get())
                suma+=(int(entry6.get()))+(int(entry7.get()))+(int(entry8.get()))+(int(entry9.get()))
                suma+=int(entry10.get())
                suma+=int(entry11.get())
                suma+=int(entry12.get())
                suma+=int(entry14.get())
                suma+=int(entry15.get())
                if(suma==100):
                    archivo=open("Luchadores.txt","a")
                    
                    archivo.write("Tipo:"+tipo+"\n")
                    archivo.write("Sexo:"+sexo+"\n")
                    archivo.write("Nombre Completo:"+nombre+"\n")
                    archivo.write("Nombre de su alter ego:"+alterEgo+"\n")
                    archivo.write("velocidad:"+entry5.get()+"\n")
                    archivo.write("Fuerza:"+entry6.get()+"\n")
                    archivo.write("Inteligencia:"+entry7.get()+"\n")                    
                    archivo.write("Defensa Personal: "+entry8.get()+"\n")
                    archivo.write("Magia: "+entry9.get()+"\n")
                    archivo.write("Telepatía:"+entry10.get()+"\n")
                    archivo.write("Estrategia:"+entry11.get()+"\n")
                    archivo.write("Volar:"+entry12.get()+"\n")
                    archivo.write("Elasticidad:"+entry14.get()+"\n")
                    archivo.write("Regeneracion:"+entry15.get()+"\n")
                    archivo.write("--------------------------------------------------"+"\n")
                    archivo.close()
                    vtnPersonaje2.destroy()
                    
                    M.menuInicial()

                    
                else:
                    messagebox.showerror("Error","La suma de las habilidades no suma 100")
            
            boton=tkinter.Button(vtnPersonaje2,text="Crear Personaje",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=validarPoderes)
            boton.place(x=350,y=550)

#---------------------------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def eliminarPersonaje(self):
        vtnEliminarP=Tk()
        vtnEliminarP.geometry("400x400")
        vtnEliminarP.title("Eliminar Personaje")
        vtnEliminarP.config(bg="SteelBlue3", cursor="hand2")

        tkinter.Label(vtnEliminarP, text="۝   ELIMINAR PERSONAJE   ۝",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)
        etiqueta=tkinter.Label(vtnEliminarP,
                                text="¿Deseas eliminar un personaje?\n Por favor llenar los campos requeridos\nPara eliminar el personaje",
                                font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=45,y=32)
        tkinter.Label(vtnEliminarP, text="- - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -" ,
                      font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=10,y=100)

        etiqueta=tkinter.Label(vtnEliminarP,text="Escriba el arte ego del personaje que desea Eliminar:",
                                   font=("Times New Roman",14),
                                   bg="SteelBlue3", fg="Black").place(x=5,y=200)
        eliminarP=tkinter.Entry(vtnEliminarP,text="",
                               font=("Times New Roman",14),
                               bg="SteelBlue1", fg="Red")
        eliminarP.place(x=110,y=230)
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def Eliminar():
            if(a.BuscarDatosLuchadores("Nombre de su alter ego:"+eliminarP.get()+"\n"))==False:
               indice=a.BuscarIndiceLuchadores("Nombre de su alter ego:"+eliminarP.get()+"\n")
               eliminado=a.EliminarLuchador("Nombre de su alter ego:"+eliminarP.get()+"\n",indice)
               Archivo=open("Luchadores.txt","w")
               Archivo.write(eliminado)
               Archivo.close()
               messagebox.showinfo("Eliminado","Luchador eliminado")
               vtnEliminarP.destroy()
               M.menuInicial()
               

        botonE=tkinter.Button(vtnEliminarP,text="Eliminar Personaje",font=("Times New Roman",14),
                                     bg="DeepSkyBlue4", fg="red",command=Eliminar)#,command=eliminarPersonajetxt())
        botonE.place(x=120,y=275)
#---------------------------------------------------------------------------------------------------

    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def menuInicial(self):
        ventanaIni=Tk()
        ventanaIni.geometry("400x450")
        ventanaIni.title("Menú Principal")
        ventanaIni.config(bg="SteelBlue3", cursor="hand2")

        tkinter.Label(ventanaIni, text="۝    MENÚ PRINCIPAL    ۝",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)
        etiqueta=tkinter.Label(ventanaIni,
                               text="¡Bienvenido al juego!\n Elija una de las siguientes opciones\n¡Que te Diviertas!",
                               font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=55,y=32)
        tkinter.Label(ventanaIni, text="- - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -" ,
                      font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=10,y=100)

#---------------------------------------------------------------------------------------------------
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def Crear():
    
            
            M.menuPersonaje()
            ventanaIni.destroy()
            
                       
        btn1=tkinter.Button(ventanaIni,text=" Crear y Borrar\n  Personaje  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=Crear)
        btn1.place(x=50,y=150)
        #
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def Torneo():

            M.ventanaTorneo()
            ventanaIni.destroy()
            
        
        btn2=tkinter.Button(ventanaIni,text=" Crear y Borrar\n     Torneo   ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=Torneo)
        btn2.place(x=230,y=150)
        #
        btn3=tkinter.Button(ventanaIni,text="   Estadisticas  \n    De Las Luchas  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black")
        btn3.place(x=130,y=235)
        #
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def jugarTorneo5():
            M.jugarTorneo()
        btnJugarT=tkinter.Button(ventanaIni,text=" JUGAR TORNEO  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black", command=jugarTorneo5).place(x=125,y=320)
        #
        btnSalir=tkinter.Button(ventanaIni,text="   SALIR  \n    DEL JUEGO  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=ventanaIni.destroy).place(x=135,y=380)
        #Decoración
        tkinter.Label(ventanaIni, text="۝",
                      font=("Times New Roman", 18),bg="SteelBlue3" ,
                      fg="Black").place(x=1,y=420)
        tkinter.Label(ventanaIni, text="۝",
                      font=("Times New Roman", 18),bg="SteelBlue3" ,
                      fg="Black").place(x=370,y=420)

#---------------------------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def ventanaTorneo(self):
        ventanaTorneo=Tk()
        ventanaTorneo.geometry("450x530")
        ventanaTorneo.title("Menú Torneos")
        ventanaTorneo.config(bg="SteelBlue3", cursor="hand2")

        tkinter.Label(ventanaTorneo, text="۩        MENÚ DE TORNEOS        ۩",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)
        etiqueta=tkinter.Label(ventanaTorneo, text="¡Crea tu torneo ahora!",
                               font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=140,y=40)
        
        etiqueta=tkinter.Label(ventanaTorneo,text="Escriba el nombre del torneo:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=115,y=70)
        entry16=tkinter.Entry(ventanaTorneo,text="",
                            font=("Times New Roman",14),
                            bg="SteelBlue1", fg="Black")
        entry16.place(x=135,y=95)
        #
        etiqueta=tkinter.Label(ventanaTorneo,text="Ingrese la fecha del torneo:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=135,y=120)
        entry17=tkinter.Entry(ventanaTorneo,text="",
                            font=("Times New Roman",14),
                            bg="SteelBlue1", fg="Black")
        entry17.place(x=135,y=145)
        #
        etiqueta=tkinter.Label(ventanaTorneo,text="Selecciona el Lugar del Torneo:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=110,y=170)
        comboLugar=ttk.Combobox(ventanaTorneo, values=("La ciudad Oscura", "Limon","La Selva","---","..."))
        comboLugar.place(x=150,y=200)
        #
        etiqueta=tkinter.Label(ventanaTorneo,text="Selecciona el numero de Luchas:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=120,y=230)
        comboNumLuchas=ttk.Combobox(ventanaTorneo, values=("1", "2","3","4","5"))
        comboNumLuchas.place(x=150,y=260)
        #
        etiqueta=tkinter.Label(ventanaTorneo,text="Selecciona el modo de Lucha:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=5,y=290)
#---------------------------------------------------------------------------------------------------
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def manual():
            
            if(comboNumLuchas.get()!="")and comboLugar.get()!="" and entry17.get()!="" and entry16.get()!="":
                numero=comboNumLuchas.get()
                if(numero=="1") or numero=="2" or numero=="3" or numero=="4" or numero=="5":
                    
                    M.vManual(entry16.get(),entry17.get(),comboLugar.get(),numero)
                    ventanaTorneo.destroy()
                else:
                    messagebox.showerror("Error","El numero de lucha debe ser entre 1 y 5")

            else:
                messagebox.showerror("Error","Debe llenar los espacios solicitados")
            
            
        boton=tkinter.Button(ventanaTorneo,text="MANUAL",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black",command=manual)
        boton.place(x=10,y=320)
        #
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def JugvsIA7():
            if(comboNumLuchas.get()!="")and comboLugar.get()!="" and entry17.get()!="" and entry16.get()!="":
                numero=comboNumLuchas.get()
                if(numero=="1") or numero=="2" or numero=="3" or numero=="4" or numero=="5":
                    
                    M.JugvsIA(entry16.get(),entry17.get(),comboLugar.get(),int(numero))
                    ventanaTorneo.destroy()
                else:
                    messagebox.showerror("Error","El numero de lucha debe ser entre 1 y 5")

            else:
                messagebox.showerror("Error","Debe llenar los espacios solicitado")
            
        boton=tkinter.Button(ventanaTorneo,text="PERSONA VS PROGRAMA",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black", command=JugvsIA7)
        boton.place(x=10,y=355)
        #
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def IA_aux():
            if(comboNumLuchas.get()!="")and comboLugar.get()!="" and entry17.get()!="" and entry16.get()!="":
                numero=comboNumLuchas.get()
                if(numero=="1") or numero=="2" or numero=="3" or numero=="4" or numero=="5":
                    
                    M.IA(entry16.get(),entry17.get(),comboLugar.get(),int(numero))
                    ventanaTorneo.destroy()
                else:
                    messagebox.showerror("Error","El numero de lucha debe ser entre 1 y 5")

            else:
                messagebox.showerror("Error","Debe llenar los espacios solicitado")
            
        boton=tkinter.Button(ventanaTorneo,text="PROGRAMA VS PROGRAMA",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black", command= IA_aux)
        boton.place(x=10,y=390)
        #
        tkinter.Label(ventanaTorneo, text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" ,
                      font=("Arial Black",10),bg="SteelBlue3",fg="Black").place(x=10,y=440)
        
#---------------------------------------------------------------------------------------------------
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def eliminarTorneo():
            ventanaTorneo.destroy()
            vtnEliminarT=Tk()
            vtnEliminarT.geometry("400x400")
            vtnEliminarT.title("Eliminar Torneo")
            vtnEliminarT.config(bg="SteelBlue3", cursor="hand2")

            tkinter.Label(vtnEliminarT, text="۝   ELIMINAR TORNEO   ۝",
                          font=("Times New Roman", 18),bg="RoyalBlue2" ,
                          fg="Black").pack(fill=tkinter.X)
            etiqueta=tkinter.Label(vtnEliminarT,
                                   text="¿Deseas eliminar un torneo?\n Por favor llenar los campos requeridos\nPara eliminar el torneo",
                                   font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=45,y=32)
            tkinter.Label(vtnEliminarT, text="- - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -" ,
                          font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=10,y=100)

            etiqueta=tkinter.Label(vtnEliminarT,text="Escriba el nombre del torneo que desea Eliminar:",
                                   font=("Times New Roman",14),
                                   bg="SteelBlue3", fg="Black").place(x=5,y=200)
            eliminarT=tkinter.Entry(vtnEliminarT,text="",
                                    font=("Times New Roman",14),
                                    bg="SteelBlue1", fg="Red")
            eliminarT.place(x=110,y=230)

            botonE2=tkinter.Button(vtnEliminarT,text="Eliminar Torneo",font=("Times New Roman",14),
                                  bg="DeepSkyBlue4", fg="red")#,command=eliminarTorneotxt())
            botonE2.place(x=120,y=275)
          #  
        boton=tkinter.Button(ventanaTorneo,text="Eliminar un Torneo",font=("Times New Roman",14),
                     bg="DeepSkyBlue4", fg="Black",command=eliminarTorneo)
        boton.place(x=290,y=490)

#--------------------------------------------------------------------------------
        #########menu manual de crear Torneo#####
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def vManual(self,nombre,fecha,lugar,numero):
        vtnPersonaje=Tk()
        vtnPersonaje.geometry("500x550")
        vtnPersonaje.title("Menú Torneo")
        vtnPersonaje.config(bg="SteelBlue3", cursor="hand2")
    
        tkinter.Label(vtnPersonaje, text="۝   ELECION DE PERSONAJE   ۝",
                  font=("Times New Roman", 18),bg="RoyalBlue2" ,
                  fg="Black").pack(fill=tkinter.X)
        etiqueta=tkinter.Label(vtnPersonaje,
                           text="Elija a los Personajes\ncon los que desea Luchar\njugador1",
                           font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=135,y=32)

        

        tkinter.Label(vtnPersonaje, text="- - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -" ,
                          font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=10,y=90)



        etiqueta=tkinter.Label(vtnPersonaje,
                               text="Seleccionar Luchadores:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=10,y=130)
        etiqueta=tkinter.Label(vtnPersonaje,
                               text="Seleccionar Luchadores:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=300,y=130)


        datos=DefiniciónDeLosPersonajes()
        luchadores=[]
        
        for linea in datos.AlterEgo:
            #print(datos.AlterEgo)
            luchadores+=[linea]
        else:
            numero=int(numero)
            if(numero>=1):
                comboHV=ttk.Combobox(vtnPersonaje, values=luchadores)
                comboHV.place(x=10,y=160)
                comboHVE=ttk.Combobox(vtnPersonaje, values=luchadores)
                comboHVE.place(x=300,y=160)
                
                print(1)
                if(numero>=2):
                    comboHV2=ttk.Combobox(vtnPersonaje, values=luchadores)
                    comboHV2.place(x=10,y=190)
                    comboHVE2=ttk.Combobox(vtnPersonaje, values=luchadores)
                    comboHVE2.place(x=300,y=190)
                    print(2)
                    if(numero>=3):
                        
                        comboHV3=ttk.Combobox(vtnPersonaje, values=luchadores)
                        comboHV3.place(x=10,y=220)
                        comboHVE3=ttk.Combobox(vtnPersonaje, values=luchadores)
                        comboHVE3.place(x=300,y=220)
                        print(3)
                        if(numero>=4):
                                
                            comboHV4=ttk.Combobox(vtnPersonaje, values=luchadores)
                            comboHV4.place(x=10,y=250)
                            comboHVE4=ttk.Combobox(vtnPersonaje, values=luchadores)
                            comboHVE4.place(x=300,y=250)
                            print(4)
                            if(numero==5):

                                comboHV5=ttk.Combobox(vtnPersonaje, values=luchadores)
                                comboHV5.place(x=10,y=280)
                                comboHVE5=ttk.Combobox(vtnPersonaje, values=luchadores)
                                comboHVE5.place(x=300,y=280)
                                print(5)

        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def validar3():
            if(numero>=1):
                if(numero>=2):
                    if(numero>=3):
                        if(numero>=4):
                            if(numero==5):
                                T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV.get(),comboHVE.get(),comboHV2.get(),comboHVE2.get(),comboHV3.get(),comboHVE3.get(),
                                                   comboHV4.get(),comboHVE4.get(),comboHV5.get(),comboHVE5.get()])
                                self.Torneos+=[T1]
                                vtnPersonaje.destroy()
                                M.menuInicial()
                            else:
                                T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV.get(),comboHVE.get(),comboHV2.get(),comboHVE2.get(),comboHV3.get(),comboHVE3.get(),
                                                   comboHV4.get(),comboHVE4.get()])
                                self.Torneos+=[T1]
                                vtnPersonaje.destroy()
                                M.menuInicial()
                        else:
                            T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV.get(),comboHVE.get(),comboHV2.get(),comboHVE2.get(),comboHV3.get(),comboHVE3.get()])
                            self.Torneos+=[T1]
                            vtnPersonaje.destroy()
                            M.menuInicial()
                    else:
                        T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV.get(),comboHVE.get(),comboHV2.get(),comboHVE2.get()])
                        self.Torneos+=[T1]
                        vtnPersonaje.destroy()
                        M.menuInicial()
                else:
                    T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV.get(),comboHVE.get()])
                    self.Torneos+=[T1]
                    vtnPersonaje.destroy()
                    M.menuInicial()
                    
            else:
                print("Error")
                
            
        
        boton=tkinter.Button(vtnPersonaje,text="Continuar",font=("Times New Roman",14),
                     bg="DeepSkyBlue4", fg="Black",command=validar3)
        boton.place(x=160,y=310)
    
#-----------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def JugvsIA(self,nombre,fecha,lugar,numero):
        vtnPerIA=Tk()
        vtnPerIA.geometry("400x450")
        vtnPerIA.title("Menú Torneo")
        vtnPerIA.config(bg="SteelBlue3", cursor="hand2")
        
        tkinter.Label(vtnPerIA, text="۝   ELECION DE PERSONAJE   ۝",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)
        etiqueta=tkinter.Label(vtnPerIA,
                               text="Elija a los Personajes\ncon los que desea Luchar",
                               font=("Times New Roman",15),bg="SteelBlue3", fg="blue4").place(x=110,y=32)

        tkinter.Label(vtnPerIA, text="- - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -" ,
                      font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=10,y=90)


        etiqueta=tkinter.Label(vtnPerIA,
                               text="Seleccionar Luchadores:",
                               font=("Times New Roman",14),
                               bg="SteelBlue3", fg="Black").place(x=120,y=130)

        datos=DefiniciónDeLosPersonajes()
        luchadores=[]
            
        for linea in datos.AlterEgo:
            #print(datos.AlterEgo)
            luchadores+=[linea]
                
        else:
            if(numero>=1):
                
                comboHV11=ttk.Combobox(vtnPerIA, values=luchadores)
                comboHV11.place(x=135,y=160)
                if(numero>=2):

                    comboHV12=ttk.Combobox(vtnPerIA, values=luchadores)
                    comboHV12.place(x=135,y=190)
                    if(numero>=3):

                        comboHV13=ttk.Combobox(vtnPerIA, values=luchadores)
                        comboHV13.place(x=135,y=220)
                        if(numero>=4):

                            comboHV14=ttk.Combobox(vtnPerIA, values=luchadores)
                            comboHV14.place(x=135,y=250)
                            if(numero==5):

                                comboHV15=ttk.Combobox(vtnPerIA, values=luchadores)
                                comboHV15.place(x=135,y=280)
#---------------------------------------------------------------------------------------------------                    
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def CrearT():
            P=DefiniciónDeLosPersonajes()
            Per=P.AlterEgo
            AE=random.sample(Per,5)
            if(numero>=1):
                if(numero>=2):
                    if(numero>=3):
                        if(numero>=4):
                            if(numero==5):
                                T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV11.get(),AE[0],comboHV12.get(),AE[1],comboHV13.get(),AE[2],
                                                   comboHV14.get(),AE[3],comboHV15.get(),AE[4]])
                                self.Torneos+=[T1]
                                vtnPerIA.destroy()
                                M.menuInicial()
                            else:
                                T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV11.get(),AE[0],comboHV12.get(),AE[1],comboHV13.get(),AE[2],
                                                   comboHV14.get(),AE[3]])
                                self.Torneos+=[T1]
                                vtnPerIA.destroy()
                                M.menuInicial()
                        else:
                            T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV11.get(),AE[0],comboHV12.get(),AE[1],comboHV13.get(),AE[2]])
                            self.Torneos+=[T1]
                            vtnPerIA.destroy()
                            M.menuInicial()
                    else:
                        T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV11.get(),AE[0],comboHV12.get(),AE[1]])
                        self.Torneos+=[T1]
                        vtnPerIA.destroy()
                        M.menuInicial()
                else:
                    T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,[comboHV11.get(),AE[0]])
                    self.Torneos+=[T1]
                    vtnPerIA.destroy()
                    M.menuInicial()      
        boton=tkinter.Button(vtnPerIA,text="Continuar",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black",command=CrearT)
        boton.place(x=160,y=310)

#---------------------------------------------------------------------------------------------------                    
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def IA(self,nombre,fecha,lugar,numero):
        vtnIA=Tk()
        vtnIA.geometry("400x450")
        vtnIA.title("Menú Torneo")
        vtnIA.config(bg="SteelBlue3", cursor="hand2")
        
        tkinter.Label(vtnIA, text="۝   IA   ۝",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)
#---------------------------------------------------------------------------------------------------
        """
        Nombre:
        Entrada:
        Salida:
        Restriccion:
        Objetivo:
        """
        def CrearIA():
            P=DefiniciónDeLosPersonajes()
            Per=P.AlterEgo
            AE=random.sample(Per,10)
            if(numero>=1):
                if(numero>=2):
                    if(numero>=3):
                        if(numero>=4):
                            if(numero==5):
                                T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,AE)
                                self.Torneos+=[T1]
                                vtnIA.destroy()
                                M.menuInicial()
                            else:
                                T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,AE[:-2])
                                self.Torneos+=[T1]
                                vtnIA.destroy()
                                M.menuInicial()
                        else:
                            T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,AE[:-4])
                            self.Torneos+=[T1]
                            vtnIA.destroy()
                            M.menuInicial()
                    else:
                        T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,AE[:-6])
                        self.Torneos+=[T1]
                        vtnIA.destroy()
                        M.menuInicial()
                else:
                    T1=DefiniciónDelTorneo(nombre,fecha,lugar,numero,AE[:-8])
                    self.Torneos+=[T1]
                    vtnIA.destroy()
                    M.menuInicial()
                            
                                
                                
            
        boton=tkinter.Button(vtnIA,text="Continuar",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black",command=CrearIA)
        boton.place(x=160,y=310)
        
               
                
#---------------------------------------------------------------------------------------------------
    """
    Nombre:
    Entrada:
    Salida:
    Restriccion:
    Objetivo:
    """
    def jugarTorneo(self):
        vtnJuegoT=Tk()
        vtnJuegoT.geometry("400x400")
        vtnJuegoT.title("Jugar Torneo")
        vtnJuegoT.config(bg="SteelBlue3", cursor="hand2")

        tkinter.Label(vtnJuegoT, text="۝   JUEGO TORNEO   ۝",
                          font=("Times New Roman", 18),bg="RoyalBlue2" ,
                          fg="Black").pack(fill=tkinter.X)






#------------------------------------------------------------------------------------------
##################
A=GranTorino()   #
A.menu()         #
M=MenuPrincipal()#
##################
