import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import path
import pylab

working_dir = "./data"
# For .read_csv, always use header=0 when you know row 0 is the header row
data_filename = "ElectionsData.csv"
train = pd.read_csv(path.join(working_dir, data_filename), header=0)
train.to_csv(path.join(working_dir, data_filename + '-copy'), index=False)
train.Num_of_kids_born_last_10_years.dropna().hist()
pylab.show()
