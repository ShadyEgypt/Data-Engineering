import pandas as pd
import os
import time


timestr = time.strftime(f'%Y%m%d-%H%M%S')
D_DIR = r'/home/shady/Data-Engineering/Week2/Challenge/jsonFiles'

def csv_to_json(df, filename):
    new_filename = f"{filename}_{timestr}.json"
    path = os.path.join(D_DIR,new_filename)
    jsonFile = df.to_json(path, indent = 1, orient= 'records')
    return jsonFile, new_filename