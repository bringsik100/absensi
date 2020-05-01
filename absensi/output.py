#!/usr/bin/env python3
"""
Output
"""


import json
import csv
import string
from openpyxl import Workbook

class test_out_put:
	'''fungsi untuk output'''
	def __init__(self,buffer):
		'''buffer data dari main skrip'''
		self.buffer = buffer

	def _pr_test(self):
		'''output ke layar'''
		for i in self.buffer:
			print(i)

	def test_header(self):
		'''membaca data header dari judul.json'''
		with open('data/judul.json','r') as head_data:
			return list(json.load(head_data).keys())

	def _excel_test(self,title):
		'''output ke excell'''
		self.book = Workbook()
		self.sheet = self.book.active
		self.sheet.title = 'Absensi'
		'''daftar kolom untuk excell ouput'''
		self.column = list(string.ascii_uppercase)+['AA','AB','AC']
		'''header untuk mengisi baris pertama'''
		for i in range(len(self.test_header)):
			self.sheet.cell(column=i+1,row=1, value=header[i])

		'''isi sheet dari buffer'''
		for x in range(len(self.buffer)):
			z=list(self.buffer[x].values())
			for y in range(len(column)):
				self.sheet.cell(column=y+1,row=x+2,value=(z[y]))

		'''save ke excell'''
		wb.save('{}.xlsx'.format(self.sheet.title))

		def _json_test(self,title):
			'''output ke json'''
			self.title = title
			with open('{}.json'.format(self.title),'w') as outj:
				for i in self.buffer:
					for x in i:
						outj.write(x)

		def _csv_test(self,title):
			'''output ke csv'''
			self.title = title
			with open('{}.csv'.format(self.title), 'w', dialect='excell', newline='') as csvfile:
				x = csv.writer(csvfile, delimiter=',',quotechar='"')
				for i in self.buffer:
					for g in i:
						x.writerow(g)

if __name__ == '__main__':
	main()
