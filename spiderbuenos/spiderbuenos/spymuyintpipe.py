import json
import psycopg2

with open('spymuyint.json') as json_file:
    data = json.load(json_file)

    for i in data:
        conn = psycopg2.connect("dbname=article-database user=bb")
        cur = conn.cursor()
        content = i['content'].replace("'","").replace("\\t","\n").replace("\\n","").replace("\\r","\n\n").replace("\\xa0","")
        url = i['url']
        title = i['title'].replace("'","")
        img_url = i['img_url']
        source_name = i['source_name'].replace("'","")
        description = i['description'].replace("'","")
        author = i['author']
        date_published = i['date-published']
        
        try:
            cur.execute(f"insert into ciencia(title, content, url, img_url, source_name, description, author, date_published) values('{title}','{content}','{url}','{img_url}','{source_name}','{description}','{author}', '{date_published}');")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        conn.commit()
        conn.close()
            


print('success...')
