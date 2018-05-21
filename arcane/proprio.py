from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from arcane.utils import to_json
from arcane.db import get_db

bp = Blueprint('proprio', __name__)

PROPRIETAIRES_ATT = ['id', 'nom','age', 'profession']

@bp.route('', methods=('GET', 'POST'))
def proprietaires():
    if request.method == 'GET':
        return display_proprietaires()
    elif request.method == 'POST':
        return add_proprietaire()



@bp.route('/<id>', methods=('GET', 'PUT', 'DELETE'))
def proprietaire(id):
    if request.method == 'GET':
        return display_proprietaire(id)
    elif request.method == 'PUT':
        return edit_proprietaire(id)
    elif request.method == 'DELETE':
        return delete_proprietaire(id)


def display_proprietaire(id):
    db = get_db()
    proprio = db.execute(
        'SELECT * FROM proprietaire WHERE id = ?', (id, )
    ).fetchone()
    return to_json([proprio])
        
def edit_proprietaire(id):
    db = get_db()
    new_data = {}

    for proprio_attr in PROPRIETAIRES_ATT:
        if proprio_attr in request.form:
            new_data[proprio_attr] = request.form[proprio_attr]


    db.execute(
        'UPDATE proprietaire SET ' + ' = ? , '.join(list(new_data.keys())) + ' = ?' + ' WHERE id = ?',
        tuple(new_data.values()) + (id,)
    )
    db.commit()

    return 'ok'


def display_proprietaires():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM proprietaire'
    ).fetchall()
    return to_json(posts)


def add_proprietaire():

    nom = request.form['nom']
    age = request.form['age']
    profession = request.form['profession']

    db = get_db()
    error = None

    if not nom:
        error = 'nom is required.'
    elif not profession:
        error = 'profession is required.'
    elif not age:
        error = 'age is required'
   

    if error is None:
        db.execute(
            'INSERT INTO proprietaire (nom, age, profession) VALUES (?, ?, ?)',
            (nom, age, profession)
        )
        db.commit()
        return 'ok'
    else:
        return error

    return render_template('auth/register.html')



def delete_proprietaire(id):
    db = get_db()
    delete = db.execute(
        'DELETE FROM proprietaire WHERE id = ?', (id)
    )
    db.commit()
    return to_json(delete)