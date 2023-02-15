import pygame
import random

# Initialiser Pygame
pygame.init()

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définir les dimensions de la fenêtre
WIDTH = 600
HEIGHT = 400

# Ouvrir une fenêtre graphique
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Charger la police pour le jeu
font = pygame.font.Font(None, 36)

# Liste des mots pour le jeu
word_list = ["ecole; politique; python; nicotine; cactus; chauve; radio; boucle; cougar; sondage"]

word=random.choice(word_list) #crée une variable baptisée guess pour stoker le mot le temps de la partie
guess='*****'

# Initialiser les variables nécessaires
display = ["_"] * len(word)
used_letters = []
lives = 6

class Pendu:
    def __init__(self, master):
        self.master = master
        master.title("Jeu du Pendu")
        
        self.words = ["ecole; politique; python; nicotine; cactus; chauve; radio; boucle; cougar; sondage"]
        self.word = random.choice(self.words)
        
        self.message = tk.Label(master, text="Bienvenue au jeu du Pendu!")
        self.message.pack()
        
        self.display = tk.Label(master, text="_ " * len(self.word))
        self.display.pack()
        
        self.bouton_quitter = tk.Button(master, text="Quitter", command=master.quit)
        self.bouton_quitter.pack()

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            guess = chr(event.key).lower()
            if guess in used_letters:
                print("You already used this letter. Try another one.")
            elif guess in word:
                print("Good job! The letter exists in the word.")
                for i in range(len(word)):
                    if word[i] == guess:
                        display[i] = guess
            else:
                print("Sorry, the letter doesn't exist in the word.")
                lives -= 1
                used_letters.append(guess)

    # Dessiner le fond de la fenêtre
    screen.fill(WHITE)

    # Afficher le mot à deviner
    text = font.render(" ".join(display), True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Mettre à jour l'affichage
    pygame.display.update()


def zone_texte(mot):
    erreurs = 0
    while erreurs < len(mot):
        erreurs+=1
    texte = "_ " * erreurs
    return texte

# victoire permet de savoir si la saisie_texte = mot, si c'est le cas, elle return "gagné"
def victoire(saisie_texte, mot):
    reponse = ""
    for x in saisie_texte:
        if x != " ":
            reponse += x
    if reponse == mot :
        return "gagné"
   
root = tk.Tk()
mon_pendu = Pendu(root)
root.mainloop()

pygame.quit()
