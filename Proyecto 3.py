
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

class Archivos:
    def __init__(self):
        self.Acceso=open("acceso.txt")
        self.Luchadores=open("Luchadores.txt")
        self.DatoLuchadores=self.Luchadores.readlines()
    def datosAcceso(self):
        return self.Acceso.readlines()
    def BuscarIndiceLuchadores(self,buscar):
        datos=self.DatoLuchadores
        return datos.index(buscar)
    def BuscarDatosLuchadores(self,buscar):
        for linea in self.DatoLuchadores:
            if(linea == buscar):
                return False
            else:
                continue
        return True
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
        
                    
def Convertir_A_String(lista):
    if isinstance(lista, list):#El parámetro de entrada debe de ser una lista(restricción).
        string = ""
        for linea in lista:
            string += linea
        return string
    else:#Se imprime el error en el caso de que el parámetro de entrada no cumple con las restriciones predeterminadas.
        #print("Error: No se puede convertir a string, debido a que el tipo de dato de entrada no es una lista.")
        None
               
        


        




#PUNTO E
class DefiniciónDeLasLuchas: #Punto e
    def __init__(self):
        
        self.alterEgoDePrimerLuchador =""
        self.alterEgoDelSegundoLuchador="" 
        self.Ganador1erRound=""
        self.Ganador2doRound=""
        self.Ganador3erRound=""
        self.GanadorDeLaLucha =""

        
        
class GranTorino(Archivos):

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
                        
                        A=MenuPrincipal()
                        A.menuInicial()
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
#PUNTO C
class DefiniciónDeLosPersonajes:
    def __init__(self):
        self.Tipo=""
        self.Sexo=""
        self.hombre=""
        self.AlterEgo=""
        self.velocidad=0
        self.Fuerza=0
        self.Inteligencia=0
        self.DefensaPersonal=0
        self.Magia=0
        self.Telepatia=0
        self.Estrategia=0
        self.Volar=0
        self.Elsticidad=0
        self.Regeneracion=0
        
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
        def validarPersonaje():
            a=Archivos()
            
            if(a.BuscarDatosLuchadores("Nombre de su alter ego:"+alterEgo.get()+"\n")):

                return menuPersonaje2(comboHV.get(),comboHV2.get(),entry4.get(),alterEgo.get())

                
            else:
                messagebox.showerror("Error","El alter ego de su personaje ya existe")
                    
        
        boton=tkinter.Button(vtnPersonaje,text="Continuar\nCreacion",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black", command=validarPersonaje)
        boton.place(x=160,y=320)
    #################################
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
            #entry13=tkinter.Entry(vtnPersonaje2,text="",
                                    #font=("Times New Roman",12),
                                    #bg="SteelBlue1", fg="Black")
            #entry13.place(x=200,y=380)
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

            def validarPoderes():
                #print(int(entry5.get()),int(entry6.get()),(int(entry7.get()))+(int(entry8.get()))+(int(entry9.get())))
                suma=0
                suma+=int(entry5.get())
                suma+=(int(entry6.get()))+(int(entry7.get()))+(int(entry8.get()))+(int(entry9.get()))
                #print(suma)
                #print(int(entry10.get())+(int(entry11.get()))+(int(entry12.get()))+(int(entry13.get())))
                suma+=int(entry10.get())
                suma+=int(entry11.get())
                suma+=int(entry12.get())
                #print(entry13.get())
                #suma+=int(entry13.get())
                suma+=int(entry14.get())
                suma+=int(entry15.get())
                print(suma)
                if(suma==100):
                    archivo=open("Luchadores.txt","a")
                    
                    #tipo,sexo,nombre,alterEgo)
                    print(nombre)
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

                    A=MenuPrincipal()
                    A.menuInicial()

                    
                else:
                    messagebox.showerror("Error","La suma de las habilidades no suma 100")
            
            boton=tkinter.Button(vtnPersonaje2,text="Crear Personaje",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=validarPoderes)
            boton.place(x=350,y=550)


#-------------------------------------------------------------------------------

def eliminarPersonaje():
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
    def Eliminar():
        if(a.BuscarDatosLuchadores("Nombre de su alter ego:"+eliminarP.get()+"\n"))==False:
           indice=a.BuscarIndiceLuchadores("Nombre de su alter ego:"+eliminarP.get()+"\n")
           #A=Archivos()
           eliminado=a.EliminarLuchador("Nombre de su alter ego:"+eliminarP.get()+"\n",indice)
           Archivo=open("Luchadores.txt","w")
           Archivo.write(eliminado)
           Archivo.close()
           messagebox.showinfo("Eliminado","Luchador eliminado")
           vtnEliminarP.destroy()
           A=MenuPrincipal()
           A.menuInicial()
           

           
           
    
    botonE=tkinter.Button(vtnEliminarP,text="Eliminar Personaje",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="red",command=Eliminar)#,command=eliminarPersonajetxt())
    botonE.place(x=120,y=275)



#----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Ventana del menu principal/Inicial

class MenuPrincipal:
    
    
    def __init__(self):
        self.Vpersonajes=DefiniciónDeLosPersonajes()
    
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
        def Crear():
    
            a=DefiniciónDeLosPersonajes()
            a.menuPersonaje()
            ventanaIni.destroy()
            
                       
        btn1=tkinter.Button(ventanaIni,text=" Crear y Borrar\n  Personaje  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=Crear)
        btn1.place(x=50,y=150)
        #
        def Torneo():
            a=DefiniciónDelTorneo()
            a.ventanaTorneo()
            ventanaIni.destroy()
            
        
        btn2=tkinter.Button(ventanaIni,text=" Crear y Borrar\n     Torneo   ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black",command=Torneo)
        btn2.place(x=230,y=150)
        #
        btn3=tkinter.Button(ventanaIni,text="   Estadisticas  \n    De Las Luchas  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black")
        btn3.place(x=130,y=235)
        #
        btnJugarT=tkinter.Button(ventanaIni,text=" JUGAR TORNEO  ",font=("Times New Roman",14),
                                 bg="DeepSkyBlue4", fg="Black", command=jugarTorneo).place(x=125,y=320)
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

def jugarTorneo():
    vtnJuegoT=Tk()
    vtnJuegoT.geometry("400x400")
    vtnJuegoT.title("Jugar Torneo")
    vtnJuegoT.config(bg="SteelBlue3", cursor="hand2")

    tkinter.Label(vtnJuegoT, text="۝   JUEGO TORNEO   ۝",
                      font=("Times New Roman", 18),bg="RoyalBlue2" ,
                      fg="Black").pack(fill=tkinter.X)


#----------------------------------------------------------------------------------------
#PUNTO D
class DefiniciónDelTorneo:#Punto d
    def __init__(self):
        self.NombreDelTorneo=[]
        self.Fecha=[]
        self.LugarDelTorneo=[]
        self.NúmeroDeLuchas=0 
        self.Luchas= []
        self.BandoGanador=""
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
        #
        boton=tkinter.Button(ventanaTorneo,text="MANUAL",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black")
        boton.place(x=10,y=320)
        #
        boton=tkinter.Button(ventanaTorneo,text="PERSONA VS PROGRAMA",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black")
        boton.place(x=10,y=355)
        #
        boton=tkinter.Button(ventanaTorneo,text="PROGRAMA VS PROGRAMA",font=("Times New Roman",14),
                             bg="DeepSkyBlue4", fg="Black")
        boton.place(x=10,y=390)
        #
        tkinter.Label(ventanaTorneo, text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" ,
                      font=("Arial Black",10),bg="SteelBlue3",fg="Black").place(x=10,y=440)
        #

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


        
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
###############
a=GranTorino()#
a.menu()      #
###############
