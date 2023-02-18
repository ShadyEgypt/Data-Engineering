import pandas as pd
from datetime import datetime

def transform_batch(data):
    try:
        print(f"data shape before is: {data.shape}")

        # Rouding price
        data['price'] = round(data.price, 2)

        # print("years_of_selling type before parsing is")
        # print(type(data['year_of_selling'][0]))
        # parse year_of_selling
        data['year_of_selling'] = pd.to_datetime(data['year_of_selling'])
        # deal with nan values
        data['year_of_selling'].apply(lambda x: None if pd.NaT else x.strftime('%Y%m%d'))
        # print("years_of_selling type before parsing is")
        # print(type(data['year_of_selling'][0]))


        # remove years more than this year
        current_year = datetime.today().year
        data = data[data["year_of_manufacture"] <= current_year]

        print(f"data shape after is: {data.shape}")


        return data


    except Exception as exp:
        return("Error in transform_batch")



if __name__ == "__main__":
    df = pd.read_csv("data_files/dealership_data/used_car_prices1.csv")
    print(df.head(10))
    df_t = transform_batch(df)
    print(df_t.head(10))
