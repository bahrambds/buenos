import psycopg2
from flask import Blueprint, render_template

naturaleza = Blueprint('naturaleza', __name__)

conn = psycopg2.connect("dbname=article-database user=bb")
cur = conn.cursor()
cur.execute("SELECT art_id FROM naturaleza;") 
len_range = len(cur.fetchall())
cur.execute("SELECT art_id, title, description, date_published, author, source_name, url, coalesce(nullif(img_url, 'None'), 'https://estaticos.muyinteresante.es/media/cache/760x570_thumb/uploads/images/article/5cff5c385bafe8165cfb8250/plantas-extincion_0.jpg') FROM naturaleza order by date_published desc;") 
articles = []
for i in range(len_range): 
    articles.append(cur.fetchone())


@naturaleza.route("/naturaleza")
def get_naturaleza():
    return render_template('cat/naturaleza.html', title='Naturaleza', articles=articles)

@naturaleza.route("/naturaleza/<int:art_id>")
def naturaleza_art(art_id): 
    cur.execute(f"SELECT art_id, title, description, date_published, author, source_name, url, coalesce(nullif(img_url, 'None'), 'https://estaticos.muyinteresante.es/media/cache/760x570_thumb/uploads/images/article/5cff5c385bafe8165cfb8250/plantas-extincion_0.jpg') FROM naturaleza where art_id={art_id};")
    art = cur.fetchall()
    return render_template('art.html', title='Naturaleza', art=art)
