#!/usr/bin python3

import pandas as pd
import glob
import os

path = os.environ.get('INPUT_FOLDER')
output_path = os.environ.get('OUTPUT_FOLDER')
filename = 'all_year.csv'
files = sorted(glob.glob(os.path.join(path + "/*.csv")))

li =[]

for f in files:
    df = pd.read_csv(f, index_col=None, header=0)
    li.append(df)

df_concat = pd.concat(li, axis=0, ignore_index=True)

df_concat.to_csv(output_path+"/"+filename)


