from calendar import c
import os
from flask import Flask,jsonify, redirect, render_template, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv  
load_dotenv()

app = Flask (__name__)

password = quote_plus(os.getenv('pswd_db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{}@localhost:5432/irene'.format(password)

# connexion à la base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # Créer une instance de BD


################################################################
#           La table categories
################################################################

class Categorie(db.Model):
    __tablename__="categories"  
    id = db.Column(db.Integer, primary_key=True) 
    libelle_categorie = db.Column(db.String(50), nullable=False)
    var = db.relationship('Livre', backref = 'Categorie',lazy=True)
    
    def __init__(self,libelle_categorie):   
        self.libelle_categorie = libelle_categorie
        
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
        'id': self.id,
        'libelle_categorie': self.libelle_categorie,   
        }
        
################################################################
#          La table livres
################################################################

class Livre (db.Model):
    __tablename__ = 'livres'
    id_livre = db.Column(db.Integer, primary_key=True)  
    isbn = db.Column(db.String(50), nullable=False) 
    titre = db.Column(db.String(50), nullable=False) 
    date_publication = db.Column(db.Date, nullable=False) 
    auteur = db.Column(db.String(50), nullable=False) 
    editeur = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    
    def __init__(self,isbn,titre,date_publication,auteur, editeur,id ):
        self.isbn= isbn
        self.titre =titre
        self.date_publication=date_publication
        self.auteur=auteur
        self. editeur= editeur
        self.id=id

    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id_livre': self.id_livre,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur, 
            'id':self.id,   
        }

db.create_all()

#################################################
#           Liste de tous les  livres
####################################################


@app.route('/livres')
def get_livres():
    livres = Livre.query.all()
    livres = [l.format() for l in livres]
    return jsonify({
        'success': True,
        'livres': livres,
        'total': Livre.query.count()
    })


#################################################################
#           Recherche d'un livre en particulier par son id
################################################################

@app.route('/livres/<int:id>')
def get_livre(id):
    livres = Livre.query.get(id)
    if livres is None:
        abort(404)
    else:
        return livres.format()
    
    
    
################################################################
#        la liste des livres d’une catégorie     
################################################################
@app.route('/categories/<int:id>/livres')
def get_categori(id):
    try:
        livres = Livre.query.filter(Livre.id==id)
        livres = [l.format() for l in livres]
        return jsonify({
                'Success': True,
                'Status_code': 200,
                'total': len(livres),
                'livres': livres
            })
    except:
        abort(404)
    finally:
        db.session.close()
    
################################################################
#            Liste de  toutes les catégories
################################################################

@app.route('/categories')
def get_categories():
    categories = Categorie.query.all()
    categories = [c.format() for c in categories]
    return jsonify({
        'success': True,
        'livres': categories,
        'nombre': len(categories)
    })
    
################################################################
#           Recherche d'une catégorie par son id
################################################################

@app.route('/categories/<int:id>')
def get_categorie(id):
    categories = Categorie.query.get(id)
    if categories is None:
        abort(404)
    else:
        return categories.format()
    
################################################################
#            Supprimer un livre
################################################################

@app.route('/livres/<int:id_livre>', methods=['DELETE'])
def supprimer_livr(id_livre):
    try:
        mon_livre = Livre.query.get(id_livre)
        mon_livre.delete()
        return jsonify({
                "success": True,
                "deleted_id": id_livre,})
    except:
        abort(400)
    finally:
        db.session.close()
        
################################################################
#            Supprimer une categorie
################################################################

@app.route('/categories/<int:id>', methods=['DELETE'])
def supprimer_categorie(id):
    try:
        ma_categorie = Categorie.query.get(id)
        ma_categorie.delete()
        return jsonify({
                "success": True,
                "deleted_id": id,
            })
    except:
        abort(400)
    finally:
        db.session.close()
        
################################################################
#            Modifier les informations d’un livre
################################################################
@app.route('/livres/<int:id>', methods=['PATCH'])
def change_livre(id):
    body = request.get_json()
    livre = Livre.query.get(id)
    try:
        if 'titre' in body and 'auteur' in body and 'editeur' in body:
            livre.titre = body['titre']
            livre.auteur = body['auteur']
            livre.editeur = body['editeur']
        livre.update()
        return livre.format()
    except:
        abort(404)
        
################################################################
#           Modifier le libellé d’une categorie
################################################################

@app.route('/categories/<int:id>', methods=['PATCH'])
def change_name(id):
    body = request.get_json()
    categorie = Categorie.query.get(id)
    try:
        if 'categorie' in body:
            categorie.libelle_categorie = body['categorie']
        categorie.update()
        return categorie.format()
    except:
        abort(404)
        
