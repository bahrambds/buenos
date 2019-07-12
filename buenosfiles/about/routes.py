import psycopg2
from flask import Blueprint, render_template

about = Blueprint('about', __name__)

@about.route("/about")
def get_about():
    return render_template('about.html', title='About')
