import pandas as pd
from datetime import datetime


def transform_db_data(data, db_conn):
    try:
        db_cursor = db_conn.cursor()

        db_cursor.execute(
            """CREATE TABLE IF NOT EXISTS dest_table(
                car_id serial PRIMARY KEY,
                car_model VARCHAR(50),
                year_of_manufacture INT,
                price FLOAT8,
                fuel VARCHAR(50),
                year_of_selling DATE)
            """
        )

        print(f"data shape before is: {data.shape}")

        # Rouding price
        data['price'] = round(data.price, 2)

        # parse year_of_selling
        # print("years_of_selling type before parsing is")
        # print(type(data['year_of_selling'][0]))
        data['year_of_selling'] = pd.to_datetime(data['year_of_selling'])
        # deal with nan values
        data['year_of_selling'].apply(lambda x: None if pd.NaT else x.strftime('%Y%m%d'))
        # print("years_of_selling type before parsing is")
        # print(type(data['year_of_selling'][0]))

        # remove years more than this year
        current_year = datetime.today().year
        data = data[data["year_of_manufacture"] <= current_year]

        print(f"data shape after is: {data.shape}")


        return data, db_conn


    except Exception as exp:
        return(f"error in transform_db_data: {exp}")

    finally:
        db_conn.commit()
