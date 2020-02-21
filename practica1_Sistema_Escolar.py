import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import Text
from tkinter import messagebox
from tkinter import scrolledtext

#Definiciones de funciones

#Funcion salir 
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

def imprimirTodo(*args):
    #messagebox.showinfo('Imprimir', 'Nombre: ')
    if not (nombre.get() and aPaterno.get() and aMaterno.get() and direccion.get() and radio.get() and objetivoVida.get()):
        messagebox.showinfo('Imprimir', 'Revisar los Campos')
    else:
        tiempo = ""
        tiempo1 = ""
        tiempo2 = ""
        tiempo3 = ""
        tiempo4 = ""

        if (chk_state.get() == 0 and chk_state2.get() == 0 and chk_state3.get() == 0 and chk_state4.get() == 0):
            tiempo = "Ningun pasatiempo"
        else:
            #Obtener los valores del checkbutton
            if (chk_state.get() == 1):
                tiempo1 = "Futbol"
            if chk_state2.get() == 1:
                tiempo2 = "Dormir"
            if (chk_state3.get() == 1):
                tiempo3 = "Leer"
            if (chk_state4.get() == 1):
                tiempo4 = "Peliculas"

        #Obtener los valores del radiobutton
        if (radio.get() == 1):
            estadoCivil = "Soltero"
        if radio.get() == 2:
            estadoCivil = "Casado"
        if radio.get() == 3:
            estadoCivil = "Viudo"
        if radio.get() == 4:
            estadoCivil = "Divorciado"

        messagebox.showinfo('Imprimir', 'Nombre: ' + nombre.get() + '\nApellido Paterno: ' + aPaterno.get() 
                            + '\nApellido Materno: ' + aMaterno.get() + '\nDireccion: ' + direccion.get() 
                            + '\nColonia: ' + colonia.get() + '\nCiudad: ' + ciudad.get() 
                            + '\nMunicipio: ' + municipio.get() + '\nPasatiempos:\n' + tiempo + ' ' + tiempo1 + ' ' + tiempo2 + ' ' + tiempo3 + ' ' + tiempo4 
                            + '\nEstadoCivil: ' + estadoCivil
                            + '\nObjetivo de Vida: ' + objetivoVida.get())

def imprimirDatos(*args):
    #messagebox.showinfo('Imprimir', 'Nombre: ')
    if not (nombre.get() and aPaterno.get() and aMaterno.get() and direccion.get()):
        messagebox.showinfo('Imprimir', 'Revisar los Campos')
    else:
        messagebox.showinfo('Imprimir', 'Nombre: ' + nombre.get() + '\nApellido Paterno: ' + aPaterno.get() 
                            + '\nApellido Materno: ' + aMaterno.get() + '\nDireccion: ' + direccion.get() 
                            + '\nColonia: ' + colonia.get() + '\nCiudad: ' + ciudad.get() 
                            + '\nMunicipio: ' + municipio.get())

def imprimirExtras(*args):
    tiempo = ""
    #messagebox.showinfo('Imprimir', 'Nombre: ')
    if not (radio.get() and objetivoVida.get()):
        messagebox.showinfo('Imprimir', 'Revisar los Campos')
    else:
        tiempo = ""
        tiempo1 = ""
        tiempo2 = ""
        tiempo3 = ""
        tiempo4 = ""

        if (chk_state.get() == 0 and chk_state2.get() == 0 and chk_state3.get() == 0 and chk_state4.get() == 0):
            tiempo = "Ningun pasatiempo"
        else:
            #Obtener los valores del checkbutton
            if (chk_state.get() == 1):
                tiempo1 = "Futbol"
            if chk_state2.get() == 1:
                tiempo2 = "Dormir"
            if (chk_state3.get() == 1):
                tiempo3 = "Leer"
            if (chk_state4.get() == 1):
                tiempo4 = "Peliculas"

        #Obtener los valores del radiobutton
        if (radio.get() == 1):
            estadoCivil = "Soltero"
        if radio.get() == 2:
            estadoCivil = "Casado"
        if radio.get() == 3:
            estadoCivil = "Viudo"
        if radio.get() == 4:
            estadoCivil = "Divorciado"

        messagebox.showinfo('Imprimir', 'Pasatiempos:\n' + tiempo + ' ' + tiempo1 + ' ' + tiempo2 + ' ' + tiempo3 + ' ' + tiempo4
                            + '\nEstadoCivil: ' + estadoCivil
                            + '\nObjetivo de Vida: ' + objetivoVida.get())

def acerca():
    messagebox.showinfo('Acerca de', 'Desarrollado por Jose Angel' 
                        + '\nApple Inc. 2020')

#Creacion de la ventana 
ventana = tk.Tk()
ventana.title("Sistema Escolar")

#Dimenciones de la ventana
width = 470
high = 275

#Obtener las medidas de la pantalla
widthScreen = ventana.winfo_screenwidth()
highScreen = ventana.winfo_screenheight()

#Calcular la posicion de la ventana en la pantalla
x = (widthScreen / 2) - (width / 2)
y = (highScreen / 2) - ( high / 2)

#Crear ventana con las dimenciones y la poscion final
ventana.geometry('%dx%d+%d+%d' % (width, high, x, y))
ventana.resizable(0, 0)

#Creacion del menu
barraMenu = Menu(ventana)
ventana.config(menu = barraMenu)

#Menu Sistema
menuSistema = Menu(barraMenu)
menuSistema.add_command(label = "Imprimir", command = imprimirTodo)
menuSistema.add_separator()
menuSistema.add_command(label = "Salir", command = funcion_salir)
barraMenu.add_cascade(label = "Sistema", menu = menuSistema)

#Menu Ayuda
menuAyuda = Menu(barraMenu)
menuAyuda.add_command(label = "Acerca de", command = acerca)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

#Creacion de Pestañas
tabControl = ttk.Notebook(ventana)
tabControl.pack(expand = 1, fill = "both")

#Pestaña de Datos Personales
tabDatos = ttk.Frame(tabControl)
tabControl.add(tabDatos, text = 'Datos Personales')

#Pestaña de Datos Extras
tabExtras = ttk.Frame(tabControl)
tabControl.add(tabExtras, text = 'Datos Extras')

################################Crear Label en la Pestaña Datos Personales
labelNombre = ttk.Label(tabDatos, text = "Nombre: ")
labelNombre.grid(column = 0, row = 0)

labelAPaterno = ttk.Label(tabDatos, text = "Apellido Paterno: ")
labelAPaterno.grid(column = 0, row = 1)


labelAMaterno = ttk.Label(tabDatos, text = "Apellido Materno: ")
labelAMaterno.grid(column = 0, row = 2)

labelDireccion = ttk.Label(tabDatos, text = "Direccion: ")
labelDireccion.grid(column = 0, row = 3)

labelColonia = ttk.Label(tabDatos, text = "Colonia: ")
labelColonia.grid(column = 0, row = 4)

labelCiudad = ttk.Label(tabDatos, text = "Ciudad: ")
labelCiudad.grid(column = 0, row = 5)

labelMunicipio = ttk.Label(tabDatos, text = "Municipio: ")
labelMunicipio.grid(column = 0, row = 6)

###############################Crear caja de texto en la pestaña Datos Personales
nombre = tk.StringVar()
getNombre = ttk.Entry(tabDatos, width = 20, textvariable = nombre)
getNombre.grid(column = 1, row = 0)

aPaterno = tk.StringVar()
getAPaterno = ttk.Entry(tabDatos, width = 20, textvariable = aPaterno)
getAPaterno.grid(column = 1, row = 1)

aMaterno = tk.StringVar()
getAMaterno = ttk.Entry(tabDatos, width = 20, textvariable = aMaterno)
getAMaterno.grid(column = 1, row = 2)

direccion = tk.StringVar()
getDireccion = ttk.Entry(tabDatos, width = 20, textvariable = direccion)
getDireccion.grid(column = 1, row = 3)

##############################Lista desplegable (Select) en la pestaña Datos Personales
colonia = tk.StringVar()
getColonia = ttk.Combobox(tabDatos, width = 19, textvariable = colonia)

ciudad = tk.StringVar()
getCiudad = ttk.Combobox(tabDatos, width = 19, textvariable = ciudad)

municipio = tk.StringVar()
getMunicipio = ttk.Combobox(tabDatos, width = 19, textvariable = municipio)

#########################################Valores del select
getColonia ['values'] =  ('Centro', 'Vasco de Quiroga', 'Villas del Pedregal')
getColonia.grid(column = 1, row = 4)
getColonia.current(0)

getCiudad ['values'] =  ('Morelia', 'Quiroga', 'Lazaro Cardenas')
getCiudad.grid(column = 1, row = 5)
getCiudad.current(0)

getMunicipio ['values'] =  ('Morelia', 'Tarimbaro', 'San Juanito Itzicuaro')
getMunicipio.grid(column = 1, row = 6)
getMunicipio.current(0)

#Boton
accion = ttk.Button(tabDatos, text = "Imprimir Datos Personales", command = imprimirDatos)
accion.grid(column = 2, row = 7)

################################Crear Label en la Pestaña Datos Extras
labelPasaTiempo = ttk.Label(tabExtras, text = "Pasatiempos")
labelPasaTiempo.grid(column = 0, row = 0)

labelEstadoCivil = ttk.Label(tabExtras, text = "Estado Civil")
labelEstadoCivil.grid(column = 0, row = 2)

labelObjetivo = ttk.Label(tabExtras, text = "Objetivo de Vida")
labelObjetivo.grid(column = 0, row = 4)


############################Crear CheckButton en la Pestaña Datos Extras
chk_state = tk.IntVar()
chk = ttk.Checkbutton(tabExtras, text = "Futbol", var = chk_state)
chk.grid(column = 0, row = 1)

chk_state2 = tk.IntVar()
chk = ttk.Checkbutton(tabExtras, text = "Dormir", var = chk_state2)
chk.grid(column = 1, row = 1, sticky = tk.W)

chk_state3 = tk.IntVar()
chk = ttk.Checkbutton(tabExtras, text = "Leer", var = chk_state3)
chk.grid(column = 2, row = 1, sticky = tk.W)

chk_state4 = tk.IntVar()
chk = ttk.Checkbutton(tabExtras, text = "Peliculas", var = chk_state4)
chk.grid(column = 3, row = 1, sticky = tk.W)

##########################Creacion de RadioButton en la Pestaña Datos Extra
radio = tk.IntVar()

radio1 = ttk.Radiobutton(tabExtras, text = "Soltero", var = radio, value = 1)
radio1.grid(column = 0, row = 3)

radio2 = ttk.Radiobutton(tabExtras, text = "Casado", var = radio, value = 2)
radio2.grid(column = 1, row = 3, sticky = tk.W)

radio3 = ttk.Radiobutton(tabExtras, text = "Viudo", var = radio, value = 3)
radio3.grid(column = 2, row = 3, sticky = tk.W)

radio4 = ttk.Radiobutton(tabExtras, text = "Divorciado", var = radio, value = 4)
radio4.grid(column = 3, row = 3, sticky = tk.W)

#####################Creacion de Caja de Tecto en la pestaña Datos Extras

#Dimenciones del ScrolText
scrol_ancho = 36
scrol_alto = 5

#Creacion del ScrollText
scrol = scrolledtext.ScrolledText(tabExtras, width = scrol_ancho, height = scrol_alto)
scrol.grid(column = 0, columnspan = 3, row = 5, sticky = tk.W)

#Caja de Texto
# objetivoVida = tk.StringVar()
# getObjetivoVida = Text(scrol, height = 1, width = 50, padx = 20)
# getObjetivoVida.pack(ipady = 35)

objetivoVida = tk.StringVar()
getObjetivoVida = tk.Entry(scrol, width = scrol_ancho, textvariable = objetivoVida)
getObjetivoVida.pack(ipady = 35)

#Boton
accion2 = ttk.Button(tabExtras, text = "Imprimir Datos Extras", command = imprimirExtras)
accion2.grid(column = 3, row = 6)

ventana.mainloop()
