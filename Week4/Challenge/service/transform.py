

def transform_batch(data):
    try:
        print(f"data shape before transformation is: {data.shape}")
        data.drop_duplicates()
        print(f"data shape after removing duplicates is: {data.shape}")
        data.dropna()
        print(f"data shape after removing rows with NAN values is: {data.shape}")
        return data


    except Exception as exp:
        return("Error in transform_batch")




