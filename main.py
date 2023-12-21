"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
from flask import *
from bdd import*
from sqlite3 import*


# Création des objets Flask et Bdd
app = Flask(__name__)
bdd = Bdd("bdd/todo.sqlite")


@app.route("/Ajouter")
def Ajouter():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("Ajouter.html")

@app.route("/Modifier")
def Modifier():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("Modifier.html")

@app.route("/Supprimer")
def Supprimer():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("Supprimer.html")

@app.route("/")
def tester_bdd():
    # Récupération des personnes de la base de données SQLite
    Task = bdd.recuperer_task()
    print(Task)
    # Transmission pour affichage
    return render_template(
        "accueil.html",
        Task=Task
    )

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
