# TP Python 11 Juin 2022, réalisation du jeu du plus ou moins en python

## Travail à réaliser :
- Ecrire la fonction jeu pour faire le plus ou moins
- Ecrire des menus pour rendre le jeu interactif

### La fonction jeu : 
Le but de cette fonction est de stocker un nombre aléatoire et de le faire deviner au joueur. 
Pour calculer le nombre aléatoire il suffit d'appeller la fonction nombre_aleatoire(nombre_max). Il suffit donc de remplacer nombre_max pour le nombre maximum souhaité.
Il faudra ensuite écrire l'algorithme permettant de faire fonctionner le jeu.

#### L'algorithme du jeu
1. Stocker un nombre aléatoire
2. Demander à l'utilisateur un nombre
3. Comparer ce nombre avec le nombre stocké
4. En fonction du nombre :
    4. Le nombre est trop petit : afficher c'est plus et retourner à l'étape 2
    5. Le nombre est trop grand : afficher c'est moins et retourner à l'étape 2 
    6. Le nombre est correcte : afficher victoire

### Pour aller plus loin
Dans la suite, on peut ajouter différentes choses pour rendre le jeu interactif :
* Un compteur de coups
* Un menu pour choisir le nombre max
* Un menu pour refaire une partie  

## Quelques notions de python
Pour afficher du texte on utilise la commande print :
* ```print("un peu de texte")```
* ```print("on affiche une variable "+variable)```

Demander à l'utilisateur de saisir un nombre : 
* ```nombre = input("saisir un nombre : ")```

### Les boucles et conditionnelles :
##### La boucle Tant Que :
Elle permet d'effectuer des actions tant qu'une donnée ne vérifie une condition :

``` python
while (nombre != nombreAleatoire): #Tant que nombre est différent nombreAleatoire
    nombre = input("saisir un nombre : ")
```

##### Les conditionnelles :
Elle permet d'effectuer des actions si une condition est validée
```python
if nombre > nombreAleatoire: #Si nombre est plus grand que nombre aléatoire
    print("c'est moins")
elif nombre < nombreAleatoire: #Sinon si nombre est plus petit que nombre aléatoire
    print("c'est plus")
else: #Sinon
    print("victoire") 
```
### Pour lancer le programme :
* En ligne de commande : ```python3 jeu.py```
* En version web : https://geekflare.com/fr/online-compiler/python
