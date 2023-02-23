import pygame
from pygame.locals import *
import random
 
size = 640, 320
width, height = size
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((400,400))
running = True


liste_mots = [] 
mot = input("Choisi un mot du fichier à deviner " )
print("Votre mot est" + mot)

with open("mots.txt") as fl:
    for l in fl:#on parcours le fichier mots ligne par ligne, donc mot par mot.
        liste_mots.append(l.rstrip("\n")) 
        
liste_mots= random.choice(liste_mots) #Fonction qui permet de choisir un mot au hasard dans la liste mots

lettres = [] # Liste vide où l'on stockera les lettres du mot
faux = 0 #la variable faux désignera le nombre d'erreur faites par le joueur.
trouve = False #Tant que le joueur trouve la bonne lettre, alors trouve = Faux 
corp_plein = ["O", "/", "|", "\\","/","\\"] #Liste de chaines de caractères qui nous permettrons d'illustrer le bonhomme pendu
corp = [" ", " ", " ", " "," "," "]

while running:
    for event in pygame.event.get():
        print(event)


while not trouve:
    trouve = True #Si le joueur ne trouve pas la bonne lettre, alors un bout du pendu se dessinera
    print("+---+")
    print("|   |")
    print("|   {}".format(corp[0]))
    print("|  {}{}{}".format(corp[1], corp[2], corp[3]))
    print("|  {} {}".format(corp[4], corp[5]))

    for l in mot:
        if l in lettres: #Si la lettre est présente dans le mot, elle s'affichera a la place du "_"
            print(l, end=" ")
        else:
            trouve = False
            print("_", end=" ") #Si la lettre n'est pas presente, le "_" restera présent
    print()
    print("Lettres utilisees -", end="") 
    for l in lettres:
        print(l, end=" | ")#Facultatif, mais ce print permet d'afficher les lettres utilisées.
    print()

    if faux > 5:               #Si le nombre d'erreur dépasse 5...
        print("Tu as perdu !") 
        break                  #... la partie est interrompue.

    if trouve:
        print("Tu as gagné, bravo !")
        break

    lettre = input("Entrez une lettre: ")
    lettres.append(lettre)

    if lettre not in mot:
        corp[faux] = corp_plein[faux]
        faux += 1 #Si la lettre n'est pas présente dans le mot, la variable faux augmentera +1.

pygame.quit()
