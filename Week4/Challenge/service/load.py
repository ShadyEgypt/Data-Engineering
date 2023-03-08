from sqlalchemy import create_engine
import psycopg2
import pandas as pd


def create_table(artist):
    try:
        db_conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="albums",
            user="shady",
            password="shady"
        )

        db_cursor = db_conn.cursor()
        table_name = artist.replace(' ', '_')
        db_cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {table_name}(
                Album VARCHAR(200),
                Song VARCHAR(200))
            """
        )
        print('Table created in database successfully!')
    except Exception as exp:
        return(f"Error in load_db_data: {exp}")

    finally:
        db_conn.commit()
        db_conn.close()




def load_db_data(df, artist):
    table_name = artist.replace(' ', '_')
    print(df.head())
    for i in df.index:

            db_conn = psycopg2.connect(
                host="localhost",
                port=5432,
                database="albums",
                user="shady",
                password="shady"
            )
            
            db_cursor = db_conn.cursor()
            album = df['album'][i].replace("'", "")
            song = df['song'][i].replace("'", "")
            db_cursor.execute(f"""INSERT INTO {table_name}(album, song)
            VALUES ('{album}', '{song}')""")
            print('loaded to database successfully!')
            db_conn.commit()
            db_conn.close()


def load_data(data_to_load, target_dir):
    try:
        data_to_load.to_csv(target_dir, index=False)
        return(f"Saved in: {target_dir}")

    except Exception as exp:
        return(f"Error in load_data: {exp}")


if __name__== '__main__':
    file = pd.read_csv('Challenge/data_results/Amr Diab.csv')
    load_db_data(file, 'Amr Diab')
