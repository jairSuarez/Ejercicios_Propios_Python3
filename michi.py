from tkinter import *
from tkinter import messagebox
import random
import os

os.system("cls")

def newGame(tablero, libres, botones):
    del libres[:]
    for x in range(1, 10):
        tablero[x] = ""
        libres.append(x)
        botones[x-1].config(text= x, bg= "grey", relief= "raised")

#todas las posibles combinaciones ganadoras
def winner(tab, signo):
    if tab[1] == signo and tab[2] == signo and tab[3] == signo or \
       tab[4] == signo and tab[5] == signo and tab[6] == signo or \
       tab[7] == signo and tab[8] == signo and tab[9] == signo or \
       tab[1] == signo and tab[4] == signo and tab[7] == signo or \
       tab[2] == signo and tab[5] == signo and tab[8] == signo or \
       tab[3] == signo and tab[6] == signo and tab[9] == signo or \
       tab[1] == signo and tab[5] == signo and tab[9] == signo or \
       tab[7] == signo and tab[5] == signo and tab[3] == signo:
        return True

def movPy(_botones, _di, _libres):
    if _libres == []:
        return
    py = random.choice(_libres)
    _libres.remove(py)
    _di[py] = "X" 
    _botones[py-1].config(text= "X", bg= "red", relief= "sunken")

    if winner(_di, "X"):
        
        if messagebox.askyesno(message="¡Te ganó Python!\n¿Otra ronda?", title= "Juego Terminado"):
            newGame(_di, _libres, _botones)
        else:
            messagebox.showinfo(message="Gracias por jugar!\nNos vemos :D")
            tablero.destroy()
        return

def marcar(boton, botones,  di, libres):
    usr = boton.cget("text")
    if usr not in libres: #Si quiero seleccionar un cuadro que ya está marcado, ignora el codigo restante
        #print("No disponible")
        return
    libres.remove(usr)#Deja de estar disponible el boton con el numero especificado
    di[usr] = "O"
    boton.config(text="O", bg="lightblue", relief="sunken")
    if winner(di, "O"):
        if messagebox.askyesno(message="¡Le ganaste a Python!\n¿Otra ronda?", title= "Juego Terminado"):
            newGame(di, libres, botones)
        else:
            messagebox.showinfo(message="Gracias por jugar!\nNos vemos :D")
            tablero.destroy()
        return

    movPy(botones, di, libres)

    if libres == []:
        messagebox.showwarning(message="Opciones agotadas", title="Empate")
        tablero.destroy()


tablero = Tk()
tablero.geometry("1000x800") #(AnchoxAlto)
tablero.title("Michi")

b = []
cont = 0
estPos = {}
n = [x for x in range(1,10)]


for fila in range(3):
    for columna in range(3):
        cont += 1
        b.append( Button(tablero, text=cont, height=4, width=8 , relief="raised", bd=7, bg="grey") )
        b[cont-1].grid(column=columna, row=fila)
        b[cont-1].config(font=('Console',35))
        estPos[cont] = ""


b[0].config(command= lambda:marcar(b[0], b, estPos, n))
b[1].config(command= lambda:marcar(b[1], b, estPos, n))
b[2].config(command= lambda:marcar(b[2], b, estPos, n))

b[3].config(command= lambda:marcar(b[3], b, estPos, n))
b[4].config(command= lambda:marcar(b[4], b, estPos, n))
b[5].config(command= lambda:marcar(b[5], b, estPos, n))

b[6].config(command= lambda:marcar(b[6], b, estPos, n))
b[7].config(command= lambda:marcar(b[7], b, estPos, n))
b[8].config(command= lambda:marcar(b[8], b, estPos, n))

tablero.mainloop()

