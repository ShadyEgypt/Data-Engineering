import pandas as pd
import os
import time



def csv_to_json(df, filename):
    new_filename = f"{filename}_converted.json"
    i = 0
    while((os.path.exists(new_filename))):
        i+=1
        new_filename = f"{filename}_converted{i}.json"
    path = os.path.join(new_filename)
    df.to_json(path, indent = 1, orient= 'records')
    return new_filename