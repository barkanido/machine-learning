import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import path
import pylab

working_dir = "./data"
# For .read_csv, always use header=0 when you know row 0 is the header row
data_filename = "ElectionsData.csv"
data_full_path = path.join(working_dir, data_filename)
train = pd.read_csv(data_full_path, header=0)
data_copy_full_path = data_full_path + '-copy'

# backup just in case
train.to_csv(data_copy_full_path, index=False)


def categorize(df, columns):
    for column in columns:
        df[column + '_categorical'] = df[column].astype('category')
        df = df.drop(column, 1)


# categorize stuff
categorize(train, ('Vote', 'Married'))

without_missing_data = train.dropna()

# categorize Married
categorize(without_missing_data, ('Vote', 'Married'))

train.Num_of_kids_born_last_10_years.dropna().hist()
pylab.show()
