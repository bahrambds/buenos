import json
import psycopg2

with open('temp/spymuyint.json') as json_file:
    data = json.load(json_file)

    for i in data:
        conn = psycopg2.connect("dbname=article-database user=bb")
        cur = conn.cursor()
        content = i['content'].replace('(function() {                const checkExist = setInterval(function() {                    if (typeof twttr !== \\undefined\\) {                        twttr.ready(function (twttr) {                            twttr.widgets.createTweet(                                "1140888895166537729",                                document.getElementById("embedTweet_1140888895166537729"),                                {                                    lang : \\es\\,                                    width: \\60%\\,                                    align: \\center\\,                                }                            );                        });                        clearInterval(checkExist);                    }                }, 100); // check every 100ms            })();', '').replace('(function() {\\n                const checkExist = setInterval(function() {\\n                    if (typeof twttr !== \\undefined\\) {\\n                        twttr.ready(function (twttr) {\\n                            twttr.widgets.createTweet(\\n                                "1139504201615237120",\\n                                document.getElementById("embedTweet_1139504201615237120"),\\n                                {\\n                                    lang : \\es\\,\\n                                    width: \\60%\\,\\n                                    align: \\center\\,\\n                                }\\n                            );\\n                        });\\n\\n                        clearInterval(checkExist);\\n                    }\\n                }, 100); // check every 100ms\\n            })();', '').replace("'","").replace("\\t","\n").replace("\\n","").replace("\\r","\n\n").replace("\\xa0","").replace("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","\t\t\t").replace("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                                                   \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "\t\t\t").replace("\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "\t\t\t").replace("\n\n\n\n\n\n\n","")
        url = i['url']
        title = i['title'].replace("'","")
        img_url = i['img_url']
        source_name = i['source_name'].replace("'","")
        description = i['description'].replace("'","")
        author = i['author']
        date_published = i['date-published']
            
        try:
            cur.execute(f"insert into naturaleza(title, content, url, img_url, source_name, description, author, date_published) values('{title}','{content}','{url}','{img_url}','{source_name}','{description}','{author}', '{date_published}');")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        conn.commit()
        conn.close()
            


print('success...')

