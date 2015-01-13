# -*- coding:utf-8 -*-

import csv
import datetime
import mpl_toolkits.axes_grid.axes_size as Size
from mpl_toolkits.axes_grid import Divider
import matplotlib.pyplot as plt
import numpy as np


csvfile = file('../Data/table_600718ss.csv', 'rb')

reader = csv.reader(csvfile)

data = []
for line in reader:
    data.append(line)

header = data.pop(0)

imgDataDict = {}.fromkeys(header)
imgData = []

for item in data:
    for i in range(0,6,1):
        imgDataDict[header[i]] = item[i]
    imgData.append([item[0], imgDataDict])

csvfile.close()

'''
Draw
'''

x = range(0, imgData.__len__() - 1, 1)
y = []
print x.__len__()
print y.__len__()
labels = []

for item1 in imgData:
    y.append(item1[1]['Close'])

    labels.append(item[0])
#    y.append(item1['Close'])
    #print item2

class CsvDataFile():
    def __init__(self, filename):
        self._csvfile = file(filename,'rb')
        self._reader = csv.reader(self._csvfile)
        self._data = []
        for line in self._reader:
            self._data.append(line)

        header = self._data.pop(1)

