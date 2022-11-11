# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# --------------------
# funciones de la app
# --------------------

def calcular():
    messagebox.showinfo("Suma 1.0", "Hizo click en el boton calcular...")
    precio = int
    if x.get() == "general":
        if y.get() == "contado":
            precio=int((int(z.get())) - ((int(z.get()) * 0.15)))
    
        else:
            precio=int((int(z.get())) - ((int(z.get()) * 0.1)))
    else:  
        if y.get()=="contado":
            precio=int((int(z.get())) - ((int(z.get()) * 0.2)))
    
        else:
            precio=int((int(z.get())) - ((int(z.get()) * 0.05)))

    t_resultados.insert(INSERT, "El precio a pagar es de " + str(precio) +"\n")
def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados..")
    x.set("")
    y.set("")
    z.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará..")
    ventana_principal.destroy()

# ------------------
# ventana principal
# ------------------

# se crea una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS")

# tamañan de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "black")

# ------------------
# variables globales
# ------------------

x = StringVar()
y = StringVar()
z = StringVar()

# ------------------------
# frame entrada datos
# ------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=240)
frame_entrada.place(x=10,y=10)

# logo de la app
#logo = PhotoImage(file="img/logo.png")
#lb_logo = Label(frame_entrada, image=logo)
#lb_logo.place(x=61,y=61)

# etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Tipos de cliente")
titulo.config(bg="white", fg="red", font=("Arial",16))
titulo.place(x=100,y=10, width=230, height=30)

# etiqueta para x
lb_x = Label(frame_entrada, text = "Escriba el tipo de cliente: ")
lb_x.config(bg="white", fg="blue", font=("Arial",16))
lb_x.place(x=10, y=50)

# entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
entry_x.focus_set()
entry_x.place(x=315,y=50,width=115, height=30)

# etiqueta para y
lb_y = Label(frame_entrada, text = "Metodo de pago: ")
lb_y.config(bg="white", fg="blue", font=("Arial",16))
lb_y.place(x=10, y=90)

# entry para y
entry_y = Entry(frame_entrada,textvariable=y)
entry_y.config(font=("Arial",20), justify=LEFT, fg="blue")
entry_y.place(x=315,y=90,width=115, height=30)

# etiqueta para z
lb_z = Label(frame_entrada, text = "Monto: ")
lb_z.config(bg="white", fg="blue", font=("Arial",16))
lb_z.place(x=10, y=130)

# entry para z
entry_z = Entry(frame_entrada,textvariable=z)
entry_z.config(font=("Arial",20), justify=LEFT, fg="blue")
entry_z.place(x=315,y=130,width=115, height=30)

# ------------------------
# frame operaciones
# ------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=120)
frame_operaciones.place(x=10,y=260)

# boton para sumar
bt_calcular = Button(frame_operaciones, text="Calcular", command=calcular)
bt_calcular.place(x=45,y=45, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190,y=45, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335,y=45, width=100, height=30)

# ------------------------
# frame resultados
# ------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10,width=460,height=80)

# se ejecuta el metodo mainloop() de la clase Tk a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc)  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()