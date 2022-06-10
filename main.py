import random


# Fonction qui calcule un nombre aléatoire
def nombre_aleatoire(max):
    return random.randint(0, max)


# Fonction qui contient le jeu
def jeu():
    # TODO
    print(nombre_aleatoire(100))


# Fonction principale
if __name__ == '__main__':
    jeu()
