import psycopg2

conn = psycopg2.connect("dbname=article-database user=bb")
cur = conn.cursor()

commands = (
        """
        DROP TABLE if exists all_art;
        """,
        """
        CREATE TABLE all_art as table template with no data;
        """,         
        """
        alter TABLE all_art add column all_id int generated always as identity;
        """,
        """
        insert into all_art (art_id, title, description, date_published, author, source_name, url, img_url, content)((select * from tech) union all (select * from naturaleza))  order by date_published desc ;
        """,
        """
        create index tit_idx on all_art using gin(to_tsvector('english', title));
        """,
        """
        create index descr_idx on all_art using gin(to_tsvector('english', description));
        """,
        """
        create index cont_idx on all_art using gin(to_tsvector('english', content));
        """,
        """
        create index source_idx on all_art using gin(to_tsvector('english', source_name));
        """)
try:
    for command in commands:
        cur.execute(command)
    conn.commit()
    cur.close
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
        if conn is not None:
            conn.close()
