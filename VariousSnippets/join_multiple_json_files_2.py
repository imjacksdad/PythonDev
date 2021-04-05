import json
import pandas as pd

with open('example1.json') as f1:               # open the file
    data1 = json.load(f1)

with open('example2.json') as f2:                # open the file       
    data2 = json.load(f2)
    
df1 = pd.DataFrame([data1])                      # Creating DataFrames
df2 = pd.DataFrame([data2])                      # Creating DataFrames

MergeJson = pd.concat([df1, df2], axis=1)         # Concat DataFrames

MergeJson.to_json("MergeJsonDemo.json")          # Writing Json
