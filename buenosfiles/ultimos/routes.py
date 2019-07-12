import psycopg2
from flask import Blueprint, render_template, url_for, request

ultimos = Blueprint('ultimos', __name__)

conn = psycopg2.connect("dbname=article-database user=bb")
cur = conn.cursor()
cur.execute("select * from all_art;")
articles = cur.fetchall()

@ultimos.route("/")
@ultimos.route("/ultimos")
def get_ultimos():
    return render_template('ultimos.html', title='Ultimos', articles=articles)

@ultimos.route("/ultimos/<int:art_id>")
def get_art(art_id): 
    cur.execute(f"SELECT * FROM all_art where all_id={art_id};")
    art = cur.fetchall()
    return render_template('art.html', title='Article', art=art)

@ultimos.route("/search")
def get_query():        
    query = request.args.get("search")
    query = query.replace(' ', '+')
    cur.execute(f"SELECT * FROM all_art WHERE to_tsvector('english',title) @@ to_tsquery('english','{query}') or to_tsvector('english',source_name) @@ to_tsquery('english','{query}') or to_tsvector('english',description) @@ to_tsquery('english','{query}') or to_tsvector('english',content) @@ to_tsquery('english','{query}');") 
    len_range = len(cur.fetchall())
    cur.execute(f"SELECT * FROM all_art WHERE to_tsvector('english',title) @@ to_tsquery('english','{query}') or to_tsvector('english',source_name) @@ to_tsquery('english','{query}') or to_tsvector('english',description) @@ to_tsquery('english','{query}') or to_tsvector('english',content) @@ to_tsquery('english','{query}');")        
    searchquery = []
    for i in range(len_range):             
        searchquery.append(cur.fetchone())
    return render_template('search.html', title='Busca', searchquery=searchquery, query=query)

