import psycopg2
import pandas as pd

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host='127.0.0.1',
        dbname = 'postgres',
        user = 'postgres',
        password = 'postgres',
        port = '5432'
    )
    cur  = conn.cursor()

    cur.execute('select degree, count(*) from education GROUP BY degree')
    df = pd.DataFrame(cur.fetchall(), columns=['degree','sum'])
    print(df.head())
    df.to_csv('./parsed_df.csv')
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()