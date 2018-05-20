from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from arcane.utils import to_json
from arcane.db import get_db

bp = Blueprint('appart', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM proprietaire'
    ).fetchall()


    return to_json(posts)