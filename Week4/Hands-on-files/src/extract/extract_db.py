import pandas as pd
import psycopg2


def extract_db_data():
    try:
        src_conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="postgres",
            user="postgres",
            password="postgres"
        )

        src_cursor = src_conn.cursor()

        src_cursor.execute("SELECT * FROM src_table")

        src_data = src_cursor.fetchall()

        src_data = pd.DataFrame(src_data, \
            columns=['car_id','car_model','year_of_manufacture','price', 'fuel', 'year_of_selling'])

        return src_data, src_conn

    except Exception as exp:
        return("Error in extract_db_data")


if __name__ == "__main__":
    df, _ = extract_db_data()
    print(f"dataframe is: \n{df.head(10)}")
