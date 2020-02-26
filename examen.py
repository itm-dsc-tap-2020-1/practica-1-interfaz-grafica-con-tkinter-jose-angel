import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Definiciones de funciones

def calificar(*args):
    calificacion = 0

    if (pregunta1.get() == "satisface las necesidades del presente sin comprometer la capacidad de las generaciones futuras para satisfacer sus propias necesidades"):
        calificacion = calificacion + 20

    if (pregunta2.get() == "impulsar un modelo de desarrollo económico mundial compatible con la conservación del medio ambiente y con la equidad social"):
        calificacion = calificacion + 20

    if (chk_state.get() == 1 and chk_state3.get() == 1):
        calificacion = calificacion + 20
    else: 
        if (chk_state.get() == 1 and chk_state3.get() == 0):
            calificacion = calificacion + 10
        else:
            calificacion = calificacion + 10

    #Obtener los valores del radiobutton
    if (radioPregunta3.get() == 1):
        calificacion = calificacion + 20
    if radioPregunta4.get() == 3:
        calificacion = calificacion + 20

    messagebox.showinfo('Calificacion', 'Calificacion final = ' + str(calificacion))    

#Creacion de la ventana 
ventana = tk.Tk()
ventana.title("Examen de Desarrollo Sustentable")

#Dimenciones de la ventana
width = 775
high = 250

#Obtener las medidas de la pantalla
widthScreen = ventana.winfo_screenwidth()
highScreen = ventana.winfo_screenheight()

#Calcular la posicion de la ventana en la pantalla
x = (widthScreen / 2) - (width / 2)
y = (highScreen / 2) - ( high / 2)

#Crear ventana con las dimenciones y la posicion final
ventana.geometry('%dx%d+%d+%d' % (width, high, x, y))
ventana.resizable(0, 0)

################################Crear Label en la Pestaña Datos Personales
labelPregunta1 = ttk.Label(ventana, text = "1.-¿Que es el Desarrollo sustentable ")
labelPregunta1.grid(column = 0, row = 0)

labelPregunta2 = ttk.Label(ventana, text = "2.-¿Cual es el objetivo del Desarrolo Sustentable ")
labelPregunta2.grid(column = 0, row = 1)

labelPregunta3 = ttk.Label(ventana, text = "3.-¿Quién decide los objetivos de desarrollo sostenible?")
labelPregunta3.grid(column = 0, row = 2)

labelPregunta4 = ttk.Label(ventana, text = "4.-¿Cuantos son los Objetivos del Desarrollo Sostenible?")
labelPregunta4.grid(column = 0, row = 4)

labelPregunta5 = ttk.Label(ventana, text = "5.-¿Objetivos de Desarrollo del Milenio? \n(Selecciona dos opciones correctas)")
labelPregunta5.grid(column = 0, row = 6)

###############################Crear caja de texto en la pestaña Datos Personales
pregunta1 = tk.StringVar()
getPregunta1 = ttk.Entry(ventana, width = 20, textvariable = pregunta1)
getPregunta1.grid(column = 1, row = 0)

pregunta2 = tk.StringVar()
getPregunta2 = ttk.Entry(ventana, width = 20, textvariable = pregunta2)
getPregunta2.grid(column = 1, row = 1)

##########################Creacion de RadioButton en la Pestaña Datos Extra
radioPregunta3 = tk.IntVar()

radio1Pregunta3 = ttk.Radiobutton(ventana, text = "Naciones Unidas", var = radioPregunta3, value = 1)
radio1Pregunta3.grid(column = 0, row = 3)

radio2Pregunta3 = ttk.Radiobutton(ventana, text = "OMS", var = radioPregunta3, value = 2)
radio2Pregunta3.grid(column = 1, row = 3, sticky = tk.W)

radio3Pregunta3 = ttk.Radiobutton(ventana, text = "Estados Unidos", var = radioPregunta3, value = 3)
radio3Pregunta3.grid(column = 2, row = 3, sticky = tk.W)

radio4Pregunta3 = ttk.Radiobutton(ventana, text = "Union Europea", var = radioPregunta3, value = 4)
radio4Pregunta3.grid(column = 3, row = 3, sticky = tk.W)

radioPregunta4 = tk.IntVar()

radio1Pregunta4 = ttk.Radiobutton(ventana, text = "4", var = radioPregunta4, value = 1)
radio1Pregunta4.grid(column = 0, row = 5)

radio2Pregunta4 = ttk.Radiobutton(ventana, text = "50", var = radioPregunta4, value = 2)
radio2Pregunta4.grid(column = 1, row = 5, sticky = tk.W)

radio3Pregunta4 = ttk.Radiobutton(ventana, text = "17", var = radioPregunta4, value = 3)
radio3Pregunta4.grid(column = 2, row = 5, sticky = tk.W)

radio4Pregunta4 = ttk.Radiobutton(ventana, text = "20", var = radioPregunta4, value = 4)
radio4Pregunta4.grid(column = 3, row = 5, sticky = tk.W)

############################Crear CheckButton en la Pestaña Datos Extras
chk_state = tk.IntVar()
chk = ttk.Checkbutton(ventana, text = "Mejorar la salud Materna", var = chk_state)
chk.grid(column = 0, row = 7)

chk_state2 = tk.IntVar()
chk = ttk.Checkbutton(ventana, text = "Aumentar el comercio", var = chk_state2)
chk.grid(column = 1, row = 7, sticky = tk.W)

chk_state3 = tk.IntVar()
chk = ttk.Checkbutton(ventana, text = "Reducir la moratalidad infantil", var = chk_state3)
chk.grid(column = 2, row = 7, sticky = tk.W)

chk_state4 = tk.IntVar()
chk = ttk.Checkbutton(ventana, text = "Posicionar una marca", var = chk_state4)
chk.grid(column = 3, row = 7, sticky = tk.W)

#Boton
accion = ttk.Button(ventana, text = "Calificar Examen", command = calificar)
accion.grid(column = 3, row = 8)

ventana.mainloop()