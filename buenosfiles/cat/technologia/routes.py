import psycopg2
from flask import Blueprint, render_template
tech = Blueprint('tech', __name__)

conn = psycopg2.connect("dbname=article-database user=bb")
cur = conn.cursor()
cur.execute("SELECT art_id FROM tech;") 
len_range = len(cur.fetchall())
cur.execute("SELECT * FROM tech order by date_published desc;") 
articles = []
for i in range(len_range): 
    articles.append(cur.fetchone())


@tech.route("/tech")
def get_tech():
    return render_template('cat/tech.html', title='Tech', articles=articles)

@tech.route("/tech/<int:art_id>")
def get_tech_art(art_id): 
    cur.execute(f"SELECT * FROM tech where art_id={art_id};")
    art = cur.fetchall()
    return render_template('cat/tech_art.html', title='Tech', art=art)
