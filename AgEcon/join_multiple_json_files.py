import json
#import pandas as pd

files=['0111000.1990.json','0111000.1991.json','0111000.1992.json','0111000.1993.json','0111000.1994.json']

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('combined.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)
