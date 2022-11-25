import sys
import sklearn
import numpy as np
import matplotlib as mpl
import pandas as pd
import os
import tarfile
import urllib.request
data = pd.read_csv('data/diabetes_binary_health_indicators_BRFSS2015.csv')

#print(data.head)
#print(data.info)
#print(data.describe)