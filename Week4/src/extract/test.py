import glob
import pandas as pd
import xml.etree.ElementTree as ET


# function for csv
def extract_from_csv(file_to_process):
    try:
        dataframe = pd.read_csv(file_to_process)
        return dataframe

    except Exception as exp:
        return("Error in csv reading")


# function for json
def extract_from_json(file_to_process):
    try:
        dataframe = pd.read_json(file_to_process, lines=True)
        return dataframe
    except Exception as exp:
        return ("Error in json reading")


# function for the xml
def extract_from_xml(file_to_process):
    try:
        dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
        tree = ET.parse(file_to_process)
        root = tree.getroot()

        for child in root:
            car_model = child.find("car_model").text
            year_of_manufacture = int(child.find("year_of_manufacture").text)
            price = float(child.find("price").text)
            fuel = child.find("fuel").text
            dataframe = dataframe.append(
                {
                    "car_model": car_model,
                    "year_of_manufacture": year_of_manufacture,
                    "price": price,
                    "fuel": fuel
                },
                ignore_index = True
            )

        return dataframe

    except Exception as exp:
        return("Error in xml reading")


# main function
def extract_batch_files():
    try:
        relative_path = "data_files/dealership_data/"
        df = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel", "year_of_selling"])

        for csv_file in glob.glob(f"{relative_path}/*.csv"):
            df = df.append(extract_from_csv(csv_file), ignore_index=True)

        
        for json_file in glob.glob(f"{relative_path}/*.json"):
            df = df.append(extract_from_json(json_file), ignore_index=True)

        
        for xml_file in glob.glob(f"{relative_path}/*.xml"):
            df = df.append(extract_from_xml(xml_file), ignore_index=True)

        return df
    
    except Exception as exp:
        return("Error in main extract function")


if __name__ == "__main__":
    df = extract_batch_files()
    print(f"data shape is : {df.shape}")
    print(f"dataframe is: \n{df}")