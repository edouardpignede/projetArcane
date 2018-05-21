from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from arcane.utils import to_json
from arcane.db import get_db

bp = Blueprint('appart', __name__)

APPARTEMENTS_ATT = ['proprietaire_id', 'ville_id', 'nom', 'description_appart', 'type_de_bien', 'nombre_de_chambres', 'surface']

@bp.route('', methods=('GET', 'POST'))
def appartements():
    if request.method == 'GET':
        return display_appartements()
    elif request.method == 'POST':
        return add_appartement()



@bp.route('/<id>', methods=('GET', 'PUT', 'DELETE'))
def appartement(id):
    if request.method == 'GET':
        return display_appartement(id)
    elif request.method == 'PUT':
        return edit_appartment(id)
    elif request.method == 'DELETE':
        return delete_appartement(id)


def display_appartement(id):
    db = get_db()
    appart = db.execute(
        'SELECT * FROM appartement WHERE id = ?', (id, )
    ).fetchone()
    return to_json([appart])
        
def edit_appartment(id):
    db = get_db()
    new_data = {}

    for appart_attr in APPARTEMENTS_ATT:
        if appart_attr in request.form:
            new_data[appart_attr] = request.form[appart_attr]


    db.execute(
        'UPDATE appartement SET ' + ' = ? , '.join(list(new_data.keys())) + ' = ?' + ' WHERE id = ?',
        tuple(new_data.values()) + (id,)
    )
    db.commit()

    return 'ok'


def display_appartements():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM appartement'
    ).fetchall()
    return to_json(posts)


def add_appartement():

    proprietaire_id = request.form['proprietaire_id']
    ville_id = request.form['ville_id']
    nom = request.form['nom']
    description_appart = request.form['description_appart']
    type_de_bien = request.form['type_de_bien']
    nombre_de_chambres = request.form['nombre_de_chambres']
    surface = request.form['surface']

    db = get_db()
    error = None

    if not proprietaire_id:
        error = 'proprietaire_id is required.'
    elif not nom:
        error = 'nom is required.'
    elif not ville_id:
        error = 'ville_id is required'
    elif db.execute(
        'SELECT id FROM ville WHERE id = ?', (ville_id,)
    ).fetchone() is None:
        error = "City {} doesn't exist.".format(ville_id)

    if error is None:
        db.execute(
            'INSERT INTO appartement (proprietaire_id, ville_id, nom, description_appart, type_de_bien, nombre_de_chambres, surface) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (proprietaire_id, ville_id, nom, description_appart, type_de_bien, nombre_de_chambres, surface)
        )
        db.commit()
        return 'ok'
    else:
        return error

    return render_template('auth/register.html')



def delete_appartement(id):
    db = get_db()
    delete = db.execute(
        'DELETE FROM appartement WHERE id = ?', (id)
    )
    db.commit()
    return 'delete'