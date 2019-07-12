import psycopg2
from flask import Blueprint, render_template

curiosidades = Blueprint('curiosidades', __name__)

conn = psycopg2.connect("dbname=article-database user=bb")
cur = conn.cursor()
cur.execute("SELECT art_id FROM curiosidades;") 
len_range = len(cur.fetchall())
cur.execute("SELECT * FROM curiosidades order by date_published desc;") 
articles = []
for i in range(len_range): 
    articles.append(cur.fetchone())


@curiosidades.route("/curiosidades")
def get_curiosidades():
    return render_template('cat/curiosidades.html', title='Curiosidades', articles=articles)

@curiosidades.route("/curiosidades/<int:art_id>")
def get_curiosidades_art(art_id): 
    cur.execute(f"SELECT * FROM curiosidades where art_id={art_id};")
    art = cur.fetchall()
    return render_template('cat/curiosidades_art.html', title='Curiosidades', art=art)
