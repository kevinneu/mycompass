# -*- coding: utf-8 -*-

import matplotlib.ticker as ticker
import matplotlib.font_manager as font_manager

#__font_properties__ =  font_manager.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc')

__xaxis_rate__ = 10.0 / 230.0
__yaxis_rate__ = 0.3

class CompanyInfoChart:
	'''
	Company Basic Information
	'''

	def __init__(self, parent, data):
		self._parent = parent
		self._companyInfo = data['companyinfo']

		self._Axes = None

		self._xaxis_size, \
		self._yaxis_size = self.calcChartSize()

		self._xaxis_width = self._xaxis_size * __xaxis_rate__
		self._yaxis_height = self._yaxis_size * __yaxis_rate__

	def calcChartSize(self):
		return (300.0, 1.8)

	def getChartGeometry(self):
		return (self._xaxis_size * __xaxis_rate__, self._yaxis_size * __yaxis_rate__)

	def initChart(self, imgObject, imgoffset, canvasSize):
		imgoffset_x, \
		imgoffset_y = imgoffset

		chartWidth = self._xaxis_width
		chartHeight = self._yaxis_height

		canvasWidth, \
		canvasHeight = canvasSize

		layoutparams = (imgoffset_x/canvasWidth, imgoffset_y/canvasHeight, chartWidth/canvasWidth, chartHeight/canvasHeight)

		axes = imgObject.add_axes(layoutparams)
		axes.set_frame_on(False)
		self._Axes = axes

		self.setXParam()
		self.setYParam()

	def setXParam(self):
		axes = self._Axes
		xaxis = axes.get_xaxis()

		axes.set_xlim(0, self._xaxis_size)

		xaxis.set_major_locator(ticker.NullLocator())

		for mal in axes.get_xticklabels(minor=False):
			mal.set_visible(False)

		for mil in axes.get_xticklabels(minor=True):
			mil.set_visible(False)

	def setYParam(self):
		axes = self._Axes
		yaxis = axes.get_yaxis()

		axes.set_ylim(0, self._yaxis_size)

		yaxis.set_major_locator(ticker.NullLocator)

		for mal in axes.get_yticklabels(minor=False):
			mal.set_visible(False)

		for mil in axes.get_yticklabels(minor=True):
			mil.set_visible(False)

	def paint(self):
		self.paintCompanyCodeAbbr(xbase=0.0, ybase=self._yaxis_size)
		self.paintIndexAbbr(xbase=self._xaxis_size, ybase=self._yaxis_size)
		self.paintCompanyName(xbase=0.0, ybase=self._yaxis_size-0.8)
		self.paintCompanyRegionField(xbase=48.0, ybase=self._yaxis_size)
		self.paintCompanyMajor(xbase=48.0, ybase=self._yaxis_size)
		self.paintCompanyIntro(xbase=90.0, ybase=self._yaxis_size)
		self.paintCompanyCategory(xbase=165.0, ybase=self._yaxis_size)

	def paintCompanyCodeAbbr(self, xbase, ybase):
		'''
		Trade Code, Company Abbreviation
		'''

		txtstr = self._companyInfo['stockCode'] + '   ' + self._companyInfo['stockAbbr']
		label = self._Axes.text(xbase, ybase, txtstr, fontproperties=__font_properties__, verticalalignment='top', horizontalalignment='left')
		label.set_fontsize(16.0)

	def paintIndexAbbr(self, xbase, ybase):
		txtstr = self._companyInfo['indexAbbr']
		label = self._Axes.text(xbase, ybase, txtstr, fontproperties = __font_properties__, verticalalignment='top', horizontalalignment='right')
		label.set_fontsize(16.0)

	def paintCompanyName(self, xbase, ybase):
		'''
		former name, full name, english name
		'''

		txtstr= self._companyInfo['basicInfo']['formerName']
		txtlist= txtstr.split('->')
		if len(txtlist) > 15:
			txtstr= ' -> '.join(txtlist[:5]) + ' ->\n' + ' -> '.join(txtlist[5:10]) + ' ->\n' + ' -> '.join(txtlist[10:15]) + ' ->\n' + ' -> '.join(txtlist[15:]) + '\n'
		elif len(txtlist) > 10:
			txtstr= ' -> '.join(txtlist[:5]) + ' ->\n' + ' -> '.join(txtlist[5:10]) + ' ->\n' + ' -> '.join(txtlist[10:]) + '\n'
		elif len(txtlist) > 5:
			txtstr= ' -> '.join(txtlist[:5]) + ' ->\n' + ' -> '.join(txtlist[5:]) + '\n'
		else:
			txtstr= ' -> '.join(txtlist) + '\n'
		txtstr += self._companyInfo['basicInfo']['companyName'] + '\n'
		txtstr += self._companyInfo['basicInfo']['companyEnglishName']

		label= self._Axes.text(xbase, ybase, txtstr, fontproperties=__font_properties__, verticalalignment='top', horizontalalignment='left')
		label.set_fontsize(4.5)

	def paintCompanyRegionFeild(self, xbase, ybase):
		'''
		Region, Industry, list date
		'''

		txtstr= self._companyInfo['companyBrief']['region'] + '   ' + self._companyInfo['companyBrief']['field'] + '   ' + self._companyInfo['issue']['listDate']

		label= self._Axes.text(xbase, ybase, txtstr, fontproperties=__font_properties__, verticalalignment='top', horizontalalignment='left')
		label.set_fontsize(6.5)

	def paintCompanyMajor(self, xbase, ybase):
		'''
		Major
		'''
		# Lookup table: (<textlength>, <words per line>, <fontsize>, <y offset>)
		lookups= (
			(20, 10, 12.0, 0.5), 
			(45, 15, 8.2, 0.5), 
			(80, 20, 6.2, 0.5), 
			(125, 25, 5.0, 0.5), 
			(180, 30, 4.1, 0.5),
			(245, 35, 3.5, 0.4),
			(999999, 37, 3.4, 0.4)
		)

		txtstr= self._companyInfo['basicInfo']['Major']
		length= len(txtstr)
		for sizelimit, linelimit, fontsize, yshift in lookups:
			if length <= sizelimit:
				txtstr= '\n'.join([txtstr[linelimit*idx : linelimit*(idx+1)] for idx in range(length//linelimit + 1)])
				fsize= fontsize
				ycoord= ybase - yshift
				break

		label= self._Axes.text(xbase, ycoord, txtstr, fontproperties=__font_properties__, verticalalignment='top', horizontalalignment='left', color='blue')
		label.set_fontsize(fsize)

	def paintCompanyIntro(self, xbase, ybase):
		'''
		Company Brief Introduction
		'''
		# lookup table: (<text length>, <words per line>, <font size>)
		lookups= (
			(150, 30, 7.0),
			(240, 40, 5.6),
			(329, 47, 4.8),
			(432, 54, 4.2),
			(576, 64, 3.5),
			(670, 67, 3.4),
			(792, 72, 3.1),
			(960, 80, 2.8),
			(1222, 94, 2.4),
			(1428, 102, 2.26),
			(1620, 108, 2.12),
			(1938, 114, 2.00),
			(999999, 130, 1.75)
		)

		txtstr= self._companyInfo['companyBrief']['companyIntro']		# 26 ~ 2600 workds
		length= len(txtstr)

		for sizelimit, linelimit, fontsize in lookups:
			if length <= sizelimit:
				txtstr= '\n'.join([txtstr[linelimit*idx : linelimit*(idx+1)] for idx in range(length//linelimit + 1)])
				fsize= fontsize
				break

		label= self._Axes.text(xbase, ybase, txtstr, fontproperties=__font_properties__, verticalalignment='top', horizontalalignment='left')
		label.set_fontsize(fsize)


	def paintCompanyCategory(self, xbase, ybase):
		'''
		Category Information
		'''
		infolist= self._companyInfo['field']

		for idx in range(len(infolist)//10 + 1):
			txtstr= '\n'.join(infolist[10*idx : 10*(idx+1)])
			if not txtstr:
				break
			xcoord= xbase + 25.0*idx
			label= self._Axes.text(xcoord, ybase, txtstr, fontproperties=__font_properties__, verticalalignment='top', horizontalalignment='left', color='blue')
			label.set_fontsize(3.4)

