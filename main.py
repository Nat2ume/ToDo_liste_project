"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
from flask import *
from bdd import*


# Création des objets Flask et Bdd
app = Flask(__name__)
bdd = Bdd("bdd/todo.sqlite")


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

@app.route("/bdd")
def tester_bdd():
    # Récupération des personnes de la base de données SQLite
    Task = bdd.recuperer_task()
    print(Task)
    # Transmission pour affichage
    return render_template(
        "todo_bdd.html",
        Task=Task
    )

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
