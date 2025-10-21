import csv
import os

def locator_loader(csv_path:str)->dict:
    locators={}
    if not os.path.exists(csv_path):
        raise FileNotFoundError("Locator file not found at: {csv_path}")
    try:
        with open("config/locators.csv") as f:
         reader=csv.DictReader(f)
         for row in reader:
             locators[row["element_name"]]={
                 "selector_type":row["selector_type"],
                 "selector_value":row['selector_value']
            }
    except:
        print("Error loading locators file on {csv_path}")
        
    
    return locators
    