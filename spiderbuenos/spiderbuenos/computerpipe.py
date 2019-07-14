import json
import psycopg2

with open('temp/computer.json') as json_file:
    data = json.load(json_file)

    for i in data:
        conn = psycopg2.connect("dbname=article-database user=bb")
        cur = conn.cursor()
        content = i['content']
        href = i['href']

    try:
        cur.execute(f"update tech set content = '{content}' where url = '{href}';")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    conn.commit()
    conn.close()



print('success...')