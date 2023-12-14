"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
from flask import *


# Création des objets Flask et Bdd
app = Flask(__name__)


# Les routes associées aux fonctions
@app.route("/")
def accueillir():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("accueil.html")

# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python

@app.route("/personne1")
def personne1():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("personne1.html")

@app.route("/personne2")
def personne2():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("personne2.html")

@app.route("/personne3")
def personne3():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("personne3.html")

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)