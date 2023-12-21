"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
import sqlite3


# La classe
class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""

    def __init__(self, chemin_bdd):
        """Initialise la base de données

        Parameters:
            chemin_bdd (string) : chemin vers le fichier SQLite
        """
        self.chemin_bdd = chemin_bdd

    def recuperer_task(self):
        """Récupère des données

        Returns:
            (list of tuples) : liste des taches
        """
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """
            SELECT *
            FROM Task;"""
        resultat = curseur.execute(requete_sql)
        task = resultat.fetchall()
        connexion.close()
        return task

    def creer_task(self, name, priority, id_categorie, id_etat, date_echeance):
        """Récupère des données

        Returns:
            liste de taches modifié 
        """
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            INSERT INTO Task
            VALUES ({name},{priority},{id_categorie},{id_etat},{date_echeance});"""
        resultat = curseur.execute(requete_sql)
        task = resultat.fetchall()
        connexion.close()
        return task

    def update_task(self, name, priority, id_categorie, id_etat, date_echeance, task):
        """Récupère des données

        Returns:
            liste de taches mise a jour
        """
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            UPDATE Task
            SET name = {name},priority = {priority},
            id_categorie = {id_categorie},id_etat = {id_etat}, 
            date_echeance = {date_echeance}))
            WHERE id_task = {task};"""
        resultat = curseur.execute(requete_sql)
        task = resultat.fetchall()
        connexion.close()
        return task

    def delete_task(self, id_task):
        """Récupère des données

        Returns:
            liste de taches avec la ligne de supprimé
        """
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            DELET FROM Task
            WHERE id_task = {id_task};"""
        resultat = curseur.execute(requete_sql)
        task = resultat.fetchall()
        connexion.close()
        return task


# Mise au point de la classe Bdd seule
if __name__ == "__main__":
    # TODO : ajoutez le code pour tester et mettre au point votre classe Bdd
    test = Bdd("bdd/todo.sqlite")  
    print(test.recuperer_task())