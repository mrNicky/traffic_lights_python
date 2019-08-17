from tkinter import *
import time
#Création widget principal
fenetre = Tk()
fenetre.title("Simulation de feux de signalisations")
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 100, 50         # coordonnées initialesdu premier feu

#Création widgets enfants
#Avec nos feux de signalisation
canvas = Canvas(fenetre, width=300, height=550)
canvas.pack(side=TOP, padx=5, pady=5)
ligne = canvas.create_line(150, 50, 150, 470, width=10)
def light():
    canvas.create_oval(x1, y1, x1+100, y1+100, width=1, fill="black")
    canvas.create_oval(x1, y1+250, x1+100, y1+150, width=1, fill="black")
    canvas.create_oval(x1, y1+400, x1+100, y1+300, width=1, fill="black")
def red(a):
    for i in range(a):
            canvas.create_oval(x1, y1, x1+100, y1+100, width=1, fill="red")
            fenetre.update()
            time.sleep(1)
def orange(a):
    for i in range(a):
            canvas.create_oval(x1, y1+250, x1+100, y1+150, width=1, fill="orange")
            fenetre.update()
            time.sleep(1)
def vert(a):
    for i in range(a):
            canvas.create_oval(x1, y1+400, x1+100, y1+300, width=1, fill="green")
            fenetre.update()
            time.sleep(1)
while True:
    light()
    red(5)
    light()
    vert(5)
    light()
    orange(2)
fenetre.mainloop()
