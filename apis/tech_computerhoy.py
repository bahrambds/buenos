import requests
import psycopg2
newsapi = '4bd245502f3d4faaa85b68353b44010e'

url = f'https://newsapi.org/v2/everything?domains=computerhoy.com&pageSize=30&apiKey={newsapi}'
response = requests.get(url).json()

for art in response["articles"]: 
    conn = psycopg2.connect("dbname=article-database user=bb")
    cur = conn.cursor()
    try:
        art_title = art["title"].replace("'", '`')
    except Exception:
        art_title= art["title"]
    try:
        art_description = art["description"].replace("'", '`')
    except Exception:
        art_description= art["description"]          
    try:
        art_publishedAt = art["publishedAt"].replace("'", '`')
    except Exception:
        art_publishedAt= art["publishedAt"]         
    try:
        art_author = art["author"].replace("'", '`')
    except Exception:
        art_author= art["author"]          
    try:
        art_source = art["source"]["name"].replace("'", '`')
    except Exception:
        art_source= art["source"]["name"]
    try:
        art_url = art["url"].replace("'", '`')
    except Exception:
        art_url= art["url"]
    try:
        art_urltoImage = art["urlToImage"].replace("'", '`')
    except Exception:
        art_urltoImage= art["urlToImage"]

    try:
        cur.execute(f"insert into tech(title, description, date_published, author, source_name, url, img_url) values('{art_title}','{art_description}','{art_publishedAt}','{art_author}','{art_source}','{art_url}','{art_urltoImage}');")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    conn.commit()
    conn.close()
