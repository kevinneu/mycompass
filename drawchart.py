# -*- coding: utf-8 -*-

import sys
import os
import pickle
import copy
import datetime
import numpy

import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker

import Public.Public as Public

from charts.CompanyInfoChart import CompanyInfoChart

__color_pink__ = '#ffc0cb'
__color_navy__ = '#000080'
__color_gold__ = '#fddb05'

__x_axis_rate__ = 10.0 / 230.0
__y_axis_rate__ = 0.3


if __name__ == '__main__':
	cwd = os.getcwd()

	print('Preparing UI')
	