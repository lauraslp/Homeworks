# 2. Create a simple script that will conver all csv files in a directory to json files (in the same or other directory).
# 1. Nuskaityti .csv failą ir pažiūrėti ką grąžina. Reikia, kad grąžintų list of dicts
# 2. Iš list of dicts padaryti json file

# Nuskaitomi .csv failai is nurodyto katalogo Dir, paverčiami i .json failus ir išsaugomi tame pačiame kalatoge

import csv
import json
import os

Dir = 'C:/Users/Laura/Desktop/Files' # Directory which contains your files
list_of_csv_files = list(filter(lambda f: f.endswith('.csv'), os.listdir(Dir))) # Returns a list of files with  ext. .csv in a directory Dir

for csv_file in list_of_csv_files:
    file_name = csv_file[:-4]  # File name without extension .csv
    csv_file_name = os.path.join(Dir, csv_file)
    json_file_name = os.path.join(Dir, file_name + '.json')

    with open(csv_file_name, 'r') as csv_file:
        # reader = csv.reader(file, delimiter=',', quotechar='"') #list(reader) - list of lists
        csv_reader = csv.DictReader(csv_file) # list(csv_reader) - list of dicts

        with open(json_file_name, 'w') as json_file:
            json.dump(list(csv_reader), json_file, indent = 2)





