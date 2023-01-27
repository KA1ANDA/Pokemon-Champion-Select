from tkinter import *
import pygame
pygame.init()

pygame.mixer.music.load("themeSong.mp3")
pygame.mixer.music.play(-1)


class pokemon():
    """pokemonis zogadi agweriloba"""
    def __init__(self,name,health,damage,damageType):
        self.name = name
        self.health = health
        self.damage = damage
        self.damageType = damageType



def charmader_select():
    pygame.mixer.music.load("charmSound.mp3")
    pygame.mixer.music.play(0)
    health["text"]=Charmander.health
    name["text"] = Charmander.name
    type["text"] = Charmander.damageType
    damage["text"] = Charmander.damage
    canvas.delete('all')
    pokemonisbg = canvas.create_image(120, 230, image=pokemonbg1)
    photo = canvas.create_image(330, 230, image=filename1)
    type.config(bg="red", fg="white", font=("ARIAL 14 bold"))

def pikachu_select():
    pygame.mixer.music.load("pikaSound.mp3")
    pygame.mixer.music.play(0)
    health["text"]=pikachu.health
    name["text"] = pikachu.name
    type["text"] = pikachu.damageType
    damage["text"] = pikachu.damage
    canvas.delete('all')
    pokemonisbg = canvas.create_image(120, 230, image=pokemonbg2)
    photo = canvas.create_image(300, 230, image=filename2)
    type.config(bg="orange",fg="white",font=("ARIAL 14 bold"))

def Bulbasaur_select():
    pygame.mixer.music.load("bulbaSound.mp3")
    pygame.mixer.music.play(0)
    health["text"]=Bulbasaur.health
    name["text"] = Bulbasaur.name
    type["text"] = Bulbasaur.damageType
    damage["text"] = Bulbasaur.damage
    canvas.delete('all')
    pokemonisbg = canvas.create_image(120, 230, image=pokemonbg3)
    photo = canvas.create_image(300, 220, image=filename3)
    type.config(bg="green", fg="white", font=("ARIAL 14 bold"))


def Squirtle_select():
    pygame.mixer.music.load("squirtSound.mp3")
    pygame.mixer.music.play(0)
    health["text"]=Squirtle.health
    name["text"] = Squirtle.name
    type["text"] = Squirtle.damageType
    damage["text"] = Squirtle.damage
    canvas.delete('all')
    pokemonisbg = canvas.create_image(120, 230, image=pokemonbg4)
    photo = canvas.create_image(320, 220, image=filename4)
    type.config(bg="#3399FF", fg="white", font=("ARIAL 14 bold"))

#pokemnebi

pikachu = pokemon("pikachu","350HP ❤","200 ⚔","Electric")
Charmander = pokemon("Charmander","400HP ❤ ","110 ⚔","Fire")
Bulbasaur = pokemon("Bulbasaur","600HP ❤","60 ⚔","Nature")
Squirtle = pokemon("Squirtle","400HP ❤","170 ⚔","Water")


#MTAVARI FANJARA
win=Tk()
win.title("POKEMON")
pokemon_icon = PhotoImage(file="imgs/pokemon icon.png")
win.iconphoto(False,pokemon_icon)
win.geometry("600x600+800+250")
win.resizable(False,False)


#ZEVITA NAWILI
framezemota = Frame(win)
framezemota.pack(side=TOP)


#MTAVRI GVERDS SURATI

mainbg = PhotoImage(file="imgs/mainbg.png")

#CANVAS
canvas = Canvas(win,width=600,height=450)
canvas.create_image(300,200,image=mainbg)
canvas.create_text(300,180,text="Welcome Pokemon Master",fill="black",font=("ARIAL", 31, "bold"))
canvas.create_text(300,260,text="Choose Your PokḗMon",fill="yellow",font=("ARIAL", 25, "bold"))
canvas.pack()

#POKEMONEBIS SURATEBI

filename1 = PhotoImage(file="imgs/charm.png")
filename2 = PhotoImage(file="imgs/pika.png")
filename3 = PhotoImage(file="imgs/bulb.png")
filename4 = PhotoImage(file="imgs/squirt.png")

#POKEMOIS BACKGROUNDIS SURATEBI

pokemonbg1 = PhotoImage(file="imgs/firebg.png")
pokemonbg2 = PhotoImage(file="imgs/electrobg.png")
pokemonbg3 = PhotoImage(file="imgs/naturebg.png")
pokemonbg4 = PhotoImage(file="imgs/waterbg.png")




#HEALTH DA DMG SURATEBI
healthIonImg = PhotoImage(file="imgs/health-icon.png")
dmgIonImg = PhotoImage(file="imgs/dmg-icon.png")

#POKEBOLIS SURATI
pokeball = PhotoImage(file="imgs/ball.png")


#QVEVITA NAWILI
frame = Frame(win)
frame.pack(side=BOTTOM)


#maxasiateblebis chasaweri adgili

healthIcon = Label(framezemota,image=healthIonImg)
healthIcon.pack(side=LEFT)

health = Label(framezemota,fg="red",font="ARIAL 15",width=8,height=2)
health.pack(side=LEFT,padx=5)

name = Label(framezemota,bd=2,relief=RAISED,font="ARIAL 15",width=10,height=2)
name.pack(side=LEFT)

type = Label(framezemota,bd=2,relief=RAISED,font="ARIAL 15",width=10,height=2)
type.pack(side=LEFT)

damage = Label(framezemota,fg="black",font="ARIAL 15",width=8,height=2)
damage.pack(side=LEFT,padx=5)

dmgIcon = Label(framezemota,image=dmgIonImg)
dmgIcon.pack(side=LEFT)


gilaki1=Button(frame,width=100,height=100,image=pokeball,command=charmader_select).pack(side=LEFT,padx=20)
gilaki2=Button(frame,width=100,height=100,image=pokeball,command=pikachu_select).pack(side=LEFT,padx=20)
gilaki3=Button(frame,width=100,height=100,image=pokeball,command=Bulbasaur_select).pack(side=LEFT,padx=20)
gilaki4=Button(frame,width=100,height=100,image=pokeball,command=Squirtle_select).pack(side=LEFT,padx=20)










win.mainloop()