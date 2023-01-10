from random import *
import tkinter as tk

w2 = tk.Tk()
w2.title("Paramétrage de votre démineur")
w2.geometry("300x100")

LabelQuestion = tk.Label(w2, text="largeur:  " , bg ="#ACACAC")
LabelQuestion.grid(row=1,column=0, padx = 5, pady = 5)

LabelQuestionMine = tk.Label(w2, text="mines:  " , bg ="#ACACAC")
LabelQuestionMine.grid(row=2,column=0, padx = 5, pady = 5)


largeur= tk.IntVar()
largeur.set(16)
setlargeur = tk.Entry(w2, textvariable=largeur, bg ="bisque", fg="maroon", width="5")
setlargeur.focus_set()
setlargeur.grid(row=1,column=1, padx = 5, pady = 5)

mines= tk.IntVar()
mines.set(40                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       )
setmine = tk.Entry(w2, textvariable=mines, bg ="bisque", fg="maroon", width="5")
setmine.focus_set()
setmine.grid(row=2,column=1, padx = 5, pady = 5)


BoutonQuitter = tk.Button(w2, text ="Lancer", command = w2.destroy)
BoutonQuitter.grid(row=3,column=0, padx = 5, pady = 5)








w2.mainloop()

largeur= int(largeur.get())
mines = int(mines.get())
hauteur= largeur

w = tk.Tk()
w.geometry("600x600")
w.minsize(600,600)
w.maxsize(600,600)

mine=9
can_width = 600 # dimensions fenetre
can_height = 600
can = tk.Canvas(w, width=can_width, height=can_height) # création canevas
can.grid()
dark=True
if dark==True:
    baseColor = "black"
    couleurs = {0: "lime", 1: "lime",2:"lime", 3:"lime" , 4:"lime" ,5:"lime" ,6:"lime", 7:"lime",8:"lime",9:"lime"}
else:
    baseColor = "black"
    couleurs = {0: "black", 1: "blue",2:"green", 3:"red" , 4:"purple" ,5:"red" ,6:"brown", 7:"purple",8:"pink",9:"black"}
allflags=[]




size = can_width/largeur


demineur = [[0 for _ in range(largeur)] for _ in range(hauteur)]
ouverts = [[False for _ in range(largeur)] for _ in range(hauteur)]
size = can_width/largeur
def afficherjeu(t):
    x1=0
    x2=size
    y1=x1
    y2=x2
    for i in range(len(t)):
        for j in range(len(t)):
            can.create_rectangle(x1,y1,x2,y2, fill=baseColor,outline="lime")
            can.create_line(x1,y1,x2,y2,fill="lime")
            can.create_line(x2,y1,x1,y2,fill="lime")
            x1+=size
            x2+=size
        y1+=size
        y2+=size
        x1=0
        x2=size


def flag(event):
    pos1 = event.x
    pos2 = event.y
    X= int(pos1//size)
    Y= int(pos2//size)
    x1=X*size
    x2=x1+size
    y1=Y*size
    y2=y1+size
    flag=X,Y
    a=0
    for i in range(len(allflags)):
        if flag==allflags[i]:
            del allflags[i]
            can.create_rectangle(x1,y1,x2,y2,fill=baseColor,activedash=True,outline="lime")
            can.create_line(x1,y1,x2,y2,fill="lime")
            can.create_line(x2,y1,x1,y2,fill="lime")
            a=1
    if a==0:
        allflags.append(flag)
        can.create_rectangle(x1,y1,x2,y2,fill="black",activedash=True,outline="magenta")
        can.create_line(x1,y1,x2,y2,fill="magenta")
        can.create_line(x2,y1,x1,y2,fill="magenta")

def clic(event):
    discover(event.x,event.y)

def discover(x,y):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    # position du pointeur de la souris
    pos1 = x
    pos2 = y
    X= int(pos1//size)
    Y= int(pos2//size)
    x1=X*size
    x2=x1+size
    y1=Y*size
    y2=y1+size
    
    if demineur[int(Y)][int(X)]==0 and ouverts[int(Y)][int(X)]==False and pos1>=0 and pos2>=0 and pos1<=largeur*size and pos2<=hauteur*size:
        ouverts[int(Y)][int(X)]=True
        if pos1+size<=largeur*size:
            discover(pos1+size,pos2)
        if pos1-size>=0:
            discover(pos1-size,pos2)
        if pos2+size<=hauteur*size:
            discover(pos1,pos2+size)
        if pos2-size>=0:
            discover(pos1,pos2-size)
        if pos1-size>=0 and pos2-size>=0:
            discover(pos1-size,pos2-size)
        if pos1+size<=largeur*size and pos2+size<=hauteur*size:
            discover(pos1+size,pos2+size)
        if pos1-size>=0 and pos2+size<=hauteur*size:
            discover(pos1-size,pos2+size)
        if pos1+size<=largeur*size and pos2-size>=0:
            discover(pos1+size,pos2-size)
        can.create_rectangle(x1,y1,x2,y2,fill="black",outline="lime")
    if demineur[int(Y)][int(X)]!=0:
        can.create_rectangle(x1,y1,x2,y2,fill="black",outline="lime")
        can.create_text(x2-size/2,y2-size/2, text=str(demineur[int(Y)][int(X)]),
            fill=couleurs[demineur[int(Y)][int(X)]],
            font=("OCR A Extended",int(size/2)))
    if demineur[int(Y)][int(X)]==9:
        affichersoluce(demineur)
        can.create_text(can_height/2,can_width/2, text="GAME OVER",
            fill="red",
            font=("OCR A Extended",int(50)))
    ouverts[int(Y)][int(X)]=True
    

def verif(event):
    total=0
    for i in range(mines):
        for j in range(len(result)):
            if allflags[i]==result[j]:
                total+=1
    if total==mines:
        affichersoluce(demineur)
        can.create_text(can_height/2,can_width/2, text="GAME WIN!!",
            fill="red",
            font=("OCR A Extended",int(50)))
    else:       
        affichersoluce(demineur)
        can.create_text(can_height/2,can_width/2, text="GAME OVER",
            fill="red",
            font=("OCR A Extended",int(50)))


def affichersoluce(t):
    x1=0
    x2=size
    y1=x1
    y2=x2
    # for j in range(tableau.shape[0]):
    for i in range(len(t)):
        for j in range(len(t)):
            can.create_rectangle(x1,y1,x2,y2,fill="black",outline="lime")
            if demineur[i][j]!=0 and demineur[i][j]!=9:
                can.create_text(x2-size/2, y2-size/2, text=str(demineur[i][j]),fill=couleurs[demineur[i][j]],font=("OCR A Extended",int(size/2)))
            elif demineur[i][j]==9:
                can.create_rectangle(x1,y1,x2,y2,fill="red",outline="lime")
                can.create_text(x2-size/2, y2-size/2, text="\U0001f4a3",font=("OCR A Extended",int(size/2)))
            x1+=size
            x2+=size
        y1+=size
        y2+=size
        x1=0
        x2=size
    


def mineur(mines,largeur,hauteur):
    largeur-=1
    hauteur-=1
    result=[]
    for i in range(mines):
        a=True
        while a==True:
            ligne=int(randint(0,largeur))
            colone=int(randint(0,hauteur))
            if demineur[ligne][colone]!=mine:
                demineur[ligne][colone]=mine
                a=False
        pos=colone,ligne
        result.append(pos)
        if colone!=0: #
            if demineur[ligne][colone-1]!=mine:
                demineur[ligne][colone-1]+=1
        
        if colone!=hauteur:
            if demineur[ligne][colone+1]!=mine:
                demineur[ligne][colone+1]+=1
        
        if ligne!=largeur:
            if demineur[ligne+1][colone]!=mine:
                demineur[ligne+1][colone]+=1
        
        if ligne!=0:
            if demineur[ligne-1][colone]!=mine:
                demineur[ligne-1][colone]+=1
        
        if ligne-1>=0 and colone-1>=0:
            if demineur[ligne-1][colone-1]!=mine:
                demineur[ligne-1][colone-1]+=1
        
        if ligne-1>=0 and colone+1<=hauteur:
            if demineur[ligne-1][colone+1]!=mine:
                demineur[ligne-1][colone+1]+=1

        if ligne+1<=largeur and colone-1>=0:
            if demineur[ligne+1][colone-1]!=mine:
                demineur[ligne+1][colone-1]+=1
        
        if ligne+1<=largeur and colone+1<=hauteur:
            if demineur[ligne+1][colone+1]!=mine:
                demineur[ligne+1][colone+1]+=1
    return result

w.bind('<Button-1>', clic)
w.bind('f', flag)
w.bind('v', verif)


 #plaçage des mines 
  #taille d'une case

result=mineur(mines,largeur,hauteur)

""" Fonction d'affichage du tableau """ 



afficherjeu(demineur)
#affichage
print(str(mines)+" à trouver les marquer avec 'f' appuyer sur 'v' une fois toutes les mines trouvées")

w.title("Démineur")
w.mainloop()

