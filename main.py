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

@app.route("/ajouter2", methods=["POST"])
def ajouter_base_donnée():
    nom_tache = request.form["nom"]
    priorite =request.form["prio"]
    catego = request.form["catégorie"]
    etat = request.form["stade"]
    date = request.form["date"]
    connexion = sqlite3.connect("bdd/todo.sqlite")
    curseur = connexion.cursor()
    curseur.execute(f"""Insert into Task (name, priority, categorie, etat, date_echeance) 
    Values ('{nom_tache}', '{priorite}', '{catego}', '{etat}', '{date}');""")
    connexion.commit()
    connexion.close()
    return redirect("/")

@app.route("/modif_nom", methods=["POST"])
def modifier_base_donnée():
    nom_tache = request.form["nom"]
    num_tache = request.form["num"]
    connexion = sqlite3.connect("bdd/todo.sqlite")
    curseur = connexion.cursor()
    curseur.execute(f"""Insert into Task (name, priority, categorie, etat, date_echeance) 
    Values ('{nom_tache}', '{priorite}', '{catego}', '{etat}', '{date}');""")
    connexion.commit()
    connexion.close()
    return redirect("/")

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

@app.route("/supprimer2", methods=["POST"])
def Supprimer2():
    """Gère l'accueil des utilisateurs"""
    nom_tache = request.form["nom"]
    connexion = sqlite3.connect("bdd/todo.sqlite")
    curseur = connexion.cursor()
    curseur.execute(f"""Delete from Task 
    WHERE name='{nom_tache}';""")
    connexion.commit()
    connexion.close()
    return redirect("/")


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
