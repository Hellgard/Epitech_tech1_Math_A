from random import *
import math
from time import *
from tkinter import *

## info de l'iteration :
# cette itération apporte la class reset permettant un meilleur controle
##

fenetre=Tk()
fenetre.title("pong")
fenetre.geometry("1000x1000")

Can=Canvas(fenetre, bg="white", height=1000, width=1000)
Can.place(x=0,y=0)
Can.create_rectangle(0,500,1000,500,fill='black') #jsp / x / longueur / y

## affichage des messages et des points
# remarque : les canvas ne pouvant pas avoir un background transparent, il est possible de voir des traits blancs quand la balle passe dessus

#'aptsj1/aptsj2' sont des notations correspondant à 'affichage points joueur 1' (ou 2)
aptsj1 = Label(fenetre, text=0,font=("fixedsys", 16),bg='white')
aptsj1.place(x=500,y=30)
aptsj2 = Label(fenetre, text=0,font=("fixedsys", 16),bg='white')
aptsj2.place(x=500,y=940)

#psdmsg est une notation correspondant à "pause message", indiquant au joueur que le jeu est en pause
psdmsg = Label(fenetre, text='',font=("fixedsys", 16),bg='white')
psdmsg.place(x=475,y=150)

#plybtn est une notation correspondant à "play message" qui indique au joueur comment continuer à jouer après qu'un point ait été marqué
plymsg = Label(fenetre, text='',font=("fixedsys", 16),bg='white')
plymsg.place(x=400,y=180)

Game=0 #variable pour le lancement du jeu


## classes ###


class balle:
    def __init__(self,rayon,vitessex,vitessey,x,y):
        self.r=rayon
        self.vx=vitessex
        self.vy=vitessey
        self.x=x
        self.y=y
        self.ball=Can.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r, fill='black')
    def deplace(self):
        if self.x>=1000-self.r or self.x<self.r:
            self.vx=-self.vx
        elif self.y>=1000-self.r:
            j1.p=j1.p+1
            b1.reset()
            partie.points()
            aptsj1.configure(text=j1.p)
        elif self.y<self.r:
            j2.p=j2.p+1
            b1.reset()
            partie.points()
            aptsj2.configure(text=j2.p)
        self.x=self.x+self.vx
        self.y=self.y+self.vy
        Can.coords(self.ball,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)
        self.rebond(j1.raq, 'haut')
        self.rebond(j2.raq, 'bas')
    def rebond(self,other,position):
        if position=='bas':
            if self.y>=(other.y-10):
                if self.x>other.x and self.x<other.x+other.l:
                    self.vy=-self.vy
        elif position=='haut':
            if self.y==(other.y+10):
                if self.x>other.x and self.x<other.x+other.l:
                    self.vy=-self.vy
    def reset(self):
        self.x=randint(500,600)
        self.y=randint(500,600)
        global Game
        a=randint(1,4)
        if a==1:
            self.vx=-self.vx
            self.vy=-self.vy
        elif a==2:
            self.vx=self.vx
            self.vy=-self.vy
        elif a==3:
            self.vx=-self.vx
            self.vy=self.vy
        else:
            self.vx=self.vx
            self.vy=self.vy
        Game=0
        plymsg.configure(text='hit SPACE to play')

class raquette:
    def __init__(self,x,y,largeur,couleur):
        self.x=x
        self.y=y
        self.l=largeur
        self.c=couleur
        self.pad=Can.create_rectangle(self.x,self.y,self.x+self.l,self.y+10,fill=self.c)
    def deplace(self,direction):
        global Game
        if Game==1:
            if direction==1:
                if self.x<1000-self.l:
                    self.x=self.x+30
            elif direction==-1:
                if self.x>0:
                    self.x=self.x-30
        Can.coords(self.pad,self.x,self.y,self.x+self.l,self.y+10)

class joueur:
    def __init__(self,numero,couleur,points=0):
        self.n=numero
        self.c=couleur
        self.p=points
        if self.n==1:
            self.raq=raquette(482,100,75,self.c)
        elif self.n==2:
            self.raq=raquette(482,900,75,self.c)

class partie:
    def __init__(self,points):
        self.p=points
    global Game
    def points(self):
        if j1.p>=self.p:
            plymsg.configure(text='  Player 1 wins')
            Game=3
            reset.fullreset()
        elif j2.p>=self.p:
            plymsg.configure(text='  Player 2 wins')
            Game=3
            reset.fullreset()


class reset:
    def __init__(self):
        return None
    def fullreset():
        reset.points()
        reset.raquettes()
        reset.screen()
        reset.game()
    def points():
        j1.p=0
        j2.p=0
    def raquettes():
        j1.raq.x=482
        j1.raq.deplace(0)
        j2.raq.x=482
        j2.raq.deplace(0)
    def screen():
        psdmsg.configure(text='')
        plymsg.configure(text='')
    def game():
        global Game
        Game=0


## fonctions ##


def deplace_pad(evt):
    global Game
    if evt.keycode==114:
        j2.raq.deplace(1)
    elif evt.keycode==113:
        j2.raq.deplace(-1)
    elif evt.keycode==40:
        j1.raq.deplace(1)
    elif evt.keycode==38:
        j1.raq.deplace(-1)
    elif evt.keycode==65:
        if Game==1:
            Game=0
            psdmsg.configure(text='pause')
        elif Game==0:
            Game=1
            reset.screen()
        elif Game==3:
            reset.fullreset()
            print('coucou')


def move():
    global Game
    if Game==1:
        b1.deplace()
    Can.after(3, move)


## création des différentes entités ##

b1=balle(10,1,1,10,200) #création de la balle avec les paramètres rayon, vitessex, vitessey, position x, position y

j1=joueur(1,'blue') #création joueur 1 avec une raquette de couleur bleue
j2=joueur(2,'red') #création joueur 2 avec une raquette de couleur rouge
partie=partie(2)

## déplacements et events ##

fenetre.bind_all('<Key>', deplace_pad)
move()
fenetre.mainloop()