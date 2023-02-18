import glob
import pandas as pd
import xml.etree.ElementTree as ET







def extract_from_csv(file_to_process):
    try:
        dataframe = pd.read_csv(file_to_process,index_col=None)
        return dataframe
    except Exception as exp:
        return('Error reading the csv file')
    

def extract_from_json(file_to_process):
    try:
        dataframe = pd.read_json(file_to_process, lines=True)
        return dataframe
    except Exception as exp:
        return('Error reading the json file \n', exp)
    

def extract_from_xml(file_to_process):
    try:
        tree = ET.parse(file_to_process)
        root = tree.getroot()
        list = []
        for child in root:
            car_model = child.find("car_model").text
            year_of_manufacture = int(child.find("year_of_manufacture").text)
            price = float(child.find("price").text)
            fuel = child.find("fuel").text
            
            d1 ={
                    "car_model": car_model,
                    "year_of_manufacture": year_of_manufacture,
                    "price": price,
                    "fuel": fuel
                }
            list.append(d1)
            dataframe = pd.DataFrame(list)
        return dataframe
    except Exception as exp:
        return("Error in xml reading",exp)


    




def extract_batch_files():
    try:
        relative_path = 'data_files/dealership_data/'
        # dataframe = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel', 'year_of_selling'])
        list = []
        for csv_file in glob.glob(f'{relative_path}/*.csv'):
            df = extract_from_csv(csv_file)
            dict_df = df.to_dict('records')
            for i in dict_df:
                list.append(i)


        for json_file in glob.glob(f"{relative_path}/*.json"):  
            df = extract_from_json(json_file)
            dict_df = df.to_dict('records')
            for i in dict_df:
                list.append(i)

        for xml_file in glob.glob(f'{relative_path}/*.xml'):
            df = extract_from_xml(xml_file)
            dict_df = df.to_dict('records')
            for i in dict_df:
                list.append(i)

        dataframe = pd.DataFrame(list)
        return dataframe

    except Exception as exp:
        print('Error in extract_batch_files function')
        return(exp)




if __name__ == '__main__':
    df = extract_batch_files()
    print(f'data shape is : {df.shape}')
    print(f'first ten records: \n {df.head(10)}')
    print(f'last ten records: \n {df.tail(10)}')