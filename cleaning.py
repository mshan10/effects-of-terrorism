

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

nRowsRead = 1000 # specify 'None' if want to read whole file
# globalterrorismdb.csv has 170350 rows in reality, but we are only loading/previewing the first 1000 rows
dataSet = pd.read_csv('../ProjData/globalterrorismdb_0718dist.csv', delimiter=',', encoding="ISO-8859-1")
dataSet.dataframeName = 'globalterrorismdb.csv'
nRow, nCol = dataSet.shape
print("There are " + str(nRow) + " rows in the dataset")

dataSet.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)
dataSet=dataSet[['Year', 'Month', 'Day', 'Country', 'Region', 'city', 'latitude', 'longitude', 'AttackType', 'Killed', 'Wounded', 'Target', 'Summary', 'Group', 'Target_type', 'Weapon_type', 'Motive']]