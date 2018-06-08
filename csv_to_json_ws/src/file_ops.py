import os
from pathlib import Path
import csv
import json

#BASE_FILE_PATH = os.path.dirname('../files/')
BASE_FILE_PATH = '../files/'
INPUT_FILE_DIR = "input-files/"
OUTPUT_FILE_DIR = "output-files/"
#ALLOWED_EXTENSIONS = set(['txt', 'csv'])

def save_file(file_to_upload):
    if not file_to_upload:
        return
    else:
        filename = file_to_upload.filename
        print("Saving file: {}".format(filename))
        target = BASE_FILE_PATH + INPUT_FILE_DIR
        print("Target directory: {}".format(target))
        
        if not os.path.isdir(target):
            print('creating target dir')
            os.mkdir(target)
            
        dest_file_path = target + filename
        print("Saving file as: {}".format(dest_file_path))
        file_to_upload.save(dest_file_path)
            
    return str(dest_file_path)
    

def convert_csv_to_json(csv_file_name):
    """
    Converts CSV file to JSON
    :param csv_file_name: Full path of csv file to be converted
    """
    filename = os.path.basename(csv_file_name)
    print("Converting file: {} to json".format(filename))
    
    with open(csv_file_name) as f:
        csv_reader = csv.DictReader(f)
        rows = list(csv_reader)
    # csv_reader = csv.DictReader(csv_file, fieldnames)    
    
    target = BASE_FILE_PATH + OUTPUT_FILE_DIR
    print("Target directory: {}".format(target))
    
    json_file_temp_path = Path(target + filename)
    json_file_path = str(json_file_temp_path.with_suffix('.json'))
    print("Saving JSON file as: {}".format(json_file_path))
    
    with open(json_file_path, 'w') as f:
        json.dump(rows, f)
     
    return json_file_path   