from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from arcane.utils import to_json
from arcane.db import get_db

bp = Blueprint('ville', __name__)







@bp.route('/<ville_id>/appartements')
def appartement(ville_id):
    return display_appartements(ville_id)





def display_appartements(ville_id):
    db = get_db()
    villes = db.execute(
        'SELECT * FROM appartement WHERE ville_id = ?', (ville_id)
    ).fetchall()
    return to_json(villes)


