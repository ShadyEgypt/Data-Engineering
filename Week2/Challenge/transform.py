import pandas as pd
import os
from sklearn import preprocessing



def transform(df, name):
    # Decluttering Data
    df.drop_duplicates()
    #Getting numerical columns
    numeric_cols = df.select_dtypes(include='number').columns
    numeric_col = [x for x in numeric_cols]
    #Fill null values with mean values
    for i in numeric_col:
        df[i].fillna(df[i].mean(), inplace=True)
    #Getting categorical columns
    categ_cols = df.select_dtypes(exclude='number').columns
    categ_col = [x for x in categ_cols]
    #Label Encoding
    label_encoder = preprocessing.LabelEncoder()
    for i in categ_col:
        if i not in ['dateRep', 'date']:
            df[i]=label_encoder.fit_transform(df[i])
    # #save file
    originalName = os.path.splitext(name)[0]
    newName = f'{originalName}_transformed.csv'
    i = 0
    while((os.path.exists(newName))):
        i+=1
        newName = f"{originalName}_transformed{i}.json"
    df.to_json(newName,indent = 1, orient= 'records')
    return newName





    