LIVRE_API documentation

Getting Started

Installation des Dépendances

Python 3.10.0

pip 21.3.1 from C:\Users\ASUS\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme python docs

Dépendances de PIP
Pour installer les dépendances, ouvrez le dossier /Documentation et exécuter la commande suivante:

pip install -r requirements.txt
or
pip3 install -r requirements.txt

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier requirements.txt.

clé de Dépendances

.Flask est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

.SQLAlchemy est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

.Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Pour le démarrer sur Windows, executez:

set FLASK_APP=app.py
set FLASK_ENV=development
flask run

API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json: { "success":False "error": 400 "message":"Ressource non disponible" }

L'API vous renvoie 4 types d'erreur: . 400: Bad request ou ressource non disponible . 500: Internal server error . 422: Unprocessable . 404: Not found

Endpoints

. ## GET/livres

GENERAL:
    Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 

    
EXEMPLE: curl http://localhost:5000/livres
{
    "livres": [
        {
            "auteur": "Alexande Dumas",
            "date_publication": "Mon, 14 May 2001 00:00:00 GMT",
            "editeur": "par Flammarion",
            "id": 4,
            "id_livre": 3,
            "isbn": "vbn",
            "titre": "les trois mousquetaires"
        },
        {
            "auteur": "Albert_camus",
            "date_publication": "Sat, 19 Feb 1972 00:00:00 GMT",
            "editeur": "Gallimard",
            "id": 9,
            "id_livre": 5,
            "isbn": "Sdn",
            "titre": "La peste "
        },
        {
            "auteur": "Voltaire",
            "date_publication": "Wed, 23 Aug 2000 00:00:00 GMT",
            "editeur": "Gauthier",
            "id": 9,
            "id_livre": 6,
            "isbn": "Dfe",
            "titre": "Candide "
        },
        {
            "auteur": "Henri",
            "date_publication": "Wed, 30 May 2001 00:00:00 GMT",
            "editeur": " Editions Nomi",
            "id": 7,
            "id_livre": 8,
            "isbn": "Gnu",
            "titre": "Louvre"
        },
        {
            "auteur": "Guy",
            "date_publication": "Sun, 21 Mar 1999 00:00:00 GMT",
            "editeur": "Gallimard",
            "id": 7,
            "id_livre": 9,
            "isbn": "Qsd",
            "titre": "Bel Amie"
        },
        {
            "auteur": "Gérard",
            "date_publication": "Wed, 19 Aug 1987 00:00:00 GMT",
            "editeur": "villiers",
            "id": 5,
            "id_livre": 10,
            "isbn": "Dbn",
            "titre": "Panama"
        },
        {
            "auteur": "Georges",
            "date_publication": "Tue, 18 Feb 2003 00:00:00 GMT",
            "editeur": "Le Livre de Poche",
            "id": null,
            "id_livre": 4,
            "isbn": "Bvf",
            "titre": "le chien jaune"
        },
        {
            "auteur": "mamadou",
            "date_publication": "Fri, 12 Feb 1999 00:00:00 GMT",
            "editeur": "rene",
            "id": null,
            "id_livre": 1,
            "isbn": "bnb",
            "titre": "ocean"
        }
    ],
    "success": true,
    "total": 8
}


.##GET/livres(id_livre) GENERAL: Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

EXEMPLE: http://localhost:5000/livres/6
{
    "auteur": "Voltaire",
    "date_publication": "Wed, 23 Aug 2000 00:00:00 GMT",
    "editeur": "Gauthier",
    "id": 9,
    "id_livre": 6,
    "isbn": "Dfe",
    "titre": "Candide "
}

. ## DELETE/livres (id_livre)

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

    EXEMPLE: curl -X DELETE http://localhost:5000/livres/3
    {
    "deleted_id": 3,
    "success": true
}

. ##PATCH/livres(id_livre) GENERAL: Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre. Il retourne un livre mis à jour.

EXEMPLE.....Avec Patch
{
    "auteur": "Guy",
    "date_publication": "Sun, 21 Mar 1999 00:00:00 GMT",
    "editeur": "Gallimard",
    "id": 7,
    "id_livre": 9,
    "isbn": "Qsd",
    "titre": "Bel Amie"
}
. ## GET/categories

  GENERAL:
      Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
  
  EXEMPLE: curl http://localhost:5000/categories

  {
    "livres": [
        {
            "id": 1,
            "libelle_categorie": "histoire"
        },
        {
            "id": 4,
            "libelle_categorie": "science"
        },
        {
            "id": 5,
            "libelle_categorie": "Mathematique"
        },
        {
            "id": 6,
            "libelle_categorie": "poème"
        },
        {
            "id": 7,
            "libelle_categorie": "Culture generale"
        },
        {
            "id": 9,
            "libelle_categorie": "Biologie"
        },
        {
            "id": 10,
            "libelle_categorie": "Théâtre"
        },
        {
            "id": 11,
            "libelle_categorie": "Narratifs"
        },
        {
            "id": 12,
            "libelle_categorie": "Epistolaire"
        },
        {
            "id": 13,
            "libelle_categorie": "Graphiques"
        },
        {
            "id": 14,
            "libelle_categorie": "Forme brève"
        },
        {
            "id": 15,
            "libelle_categorie": "cuisne"
        },
        {
            "id": 16,
            "libelle_categorie": "Humour"
        },
        {
            "id": 17,
            "libelle_categorie": "Bande dessinée"
        },
        {
            "id": 18,
            "libelle_categorie": "Jeunesse"
        },
        {
            "id": 19,
            "libelle_categorie": "art musique et cinema"
        }
    ],
    "nombre": 16,
    "success": true
}

.##GET/categories(id) GENERAL: Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

EXEMPLE: http://localhost:5000/categories/6

{
    "id": 6,
    "libelle_categorie": "poème"
}

. ## DELETE/categories (id)

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

    EXEMPLE: curl -X DELETE http://localhost:5000/categories/11

    {
    "deleted_id": 19,
    "success": true
}


. ##PATCH/categories(id) GENERAL: Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie. Il retourne une nouvelle categorie avec la nouvelle valeur.

EXEMPLE.....Avec Patch
{
    "id": 15,
    "libelle_categorie": "cuisne"
}

.##GET/categories(id)/livres
GENERAL:
Cet endpoint permet de lister les livres appartenant à une categorie donnée.
Il renvoie la classe de la categorie et les livres l'appartenant.

  EXEMPLE: http://localhost:5000/livres/categories/4

  {
    "Status_code": 200,
    "Success": true,
    "livres": [],
    "total": 0
}

