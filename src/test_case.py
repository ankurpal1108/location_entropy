# data1 link: http://download.geonames.org/export/dump/
# data1 is the location data for places of interest in India. The IN.zip file was downloaded, extracted, column names were added and saved as a csv file.
#
# data2 link: https://fusiontables.google.com/DataSource?dsrcid=579353#rows:id=1
# data2 is the locations of Nuclear power stations worldwide.
#
# Entropies are calculated for all the columns of both the datasets, while the data1 has remove_missing parameter set to False, data2 has it set to True.
# Both data sets have numerical and string columns.

import pandas as pd
from location_entropy import cal_location_entropy

data1 = pd.read_csv('../data/IN.csv', encoding='cp1252', low_memory=False)
data1_all_col_ents = data1.apply(lambda x: cal_location_entropy(x, remove_missing=False), axis = 0)
data2 = pd.read_csv('../data/Nuclear power stations worldwide.csv')
data2_all_col_ents = data2.apply(lambda x: cal_location_entropy(x, remove_missing=True), axis = 0)