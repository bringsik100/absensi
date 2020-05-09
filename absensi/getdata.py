#!/usr/bin/env python3
"""
Data
"""

"""
import library
"""
from datetime import datetime as dt
from datetime import timedelta as td
import sqlite3 as db
import sys
import os
from proses import process
from absensi import cls

"""
TODO:
- modul untuk menampilkan dan menyunting data pegawai
- modul untuk menampilkan dan menyunting jadwal
- modul untuk menampilkan dan menyunting liburan
"""

'''modul database'''

class DataBase:
	'''objek database'''
	
	def __init__(self,dbname = None):
		self.dbname = dbname
		try:
			self.conn = db.connect(f'{self.dbname}.db')
			self.cursor = self.conn.cursor()
			print('koneksi berhasil')
		except Exception:
			print(f'koneksi gagal \n {sys.exc_info()} \n Exception = {Exception()}\n')

class Table(DataBase):
	'''objek table'''
	def __init__(self,table):
		self.table = table

	def rows(self,*column = None):
			self.column = column
		'''mengambil data dalam tabel'''
		if self.column != None:
			try:
				self.cursor.execute(f'select {self.column} from {self.table}')
				return self.cursor.fetchall()
			except Exception:
				print(f'koneksi gagal \n {sys.exc_info()} \n Exception = {Exception()}\n')
				pass
		else:
			try:
				self.cursor.execute(f'select * from {self.table}')
				rows = self.cursor.fetchall()
			except Exception:
				print(f'gagal membaca data \n {sys.exc_info()} \n Exception = {Exception()}\n')

	def view(self,table,*column=None):
		'''tampilkan data dalam tabel'''
		self.column = column
		if self.column = None:
			try:
				self.cursor.execute(f'select * from {self.table}')
				print(self.cursor.fetchall())
			except Exception:
				print(f'gagal membaca data {self.table} \n {sys.exc_info()} \n Exception = {Exception()}\n')
		else:
			try:
				self.cursor.execute(f'select {self.column} from {self.table}')
				print(self.cursor.fetchall())
			except Exception:
				print(f'gagal membaca data {self.table} \n {sys.exc_info()} \n Exception = {Exception()}\n')

class CreateTable(Table): 
	'''objek pembuat tabel'''
	def create(self,*column):
		'''metode utama'''
		self.column = column
		try:
			self.cursor.execute(f'''create table if not exists {self.table}{self.column};''')
			self.conn.commit()
			print(f'buat data {self.table} berhasil')
		except Exception:
			print(f'buat tabel {self.table} gagal \n {sys.exc_info()} \n Exception = {Exception()}\n')

class InsertRow(Table):
	def value(self,*value):
		self.value = value
	def insert(self):
		try:
			self.cursor.execute(f'insert into {self.table}{self.column} values {self.value}')
			self.conn.commit()
			print(f'input data ke {self.table} berhasil')
		except Exception:
			print(f'input data ke tabel {self.table} gagal\n {sys.exc_info()} \n Exception = {Exception()}\n')
	
class UpdateRow(InsertRow):
	def update(self,row):
		self.row = row
		old_data = self.rows()[row]
		new_data = self.value
		for i in range(len(old_data)):
			if new_data[i] == None or new_data[i] == "":
				new_data[i] = old_data[i]
			else:
				return new_data[i]
		try:
			self.cursor.execute(f'insert into {self.table}{self.column} values{self.values}')
			self.conn.commit()
			print(f'update data ke {self.table} berhasil')
		except Exception:
			print(f'update data ke tabel {self.table} gagal \n {sys.exc_info()} \n Exception = {Exception()}\n')
class DelRow(Table):
	def Delete(self,row):
		self.row = self.rows[row]
		try:
			self.cursor.execute(f'delete {} from {self.rows}')
			self.conn.commit()
			print('hapus data (self.row) berhasil')
		except Exception:
			print('hapus data (self.row) gagal \n {sys.exc_info()} \n Exception = {Exception()}\n')

tab_pegawai = CreateTable('pegawai','noID integer primary key autoincrement','nopeg text','noakun text','nokartu text','nama text','titel text','departemen text')

tab_jadwal = CreateTable('jadwal','noID integer primary key autoincrement','nama text','`Jam Masuk` text','`Jam Keluar` text','`Telat` text','`Pulang Cepat` text','`Harus CIn` text','`Harus COut` text','`Normal` text','`Akhir Pekan` text','`Hari Libur` text','`Waktu Real` text')

tab_liburan = CreateTable('liburan','tanggal text','hari text')

tab_laporan = CreateTable('laporan','row_id integer primary key autoincrement','`NoPeg` text','`No. Akun` text','`No.` text','`Nama` text','`Auto-Assign` text','`Tanggal` text','`Jam Kerja` text','`Awal tugas` text','`Akhir tugas` text','`Masuk` text','`Keluar` text','`Normal` text','`Waktu real` text','`Telat` text','`Plg Awal` text','`Bolos` text','`Waktu Lembur` text','`Waktu Kerja` text','`Status` text','`Hrs C/In` text','`Hrs C/Out` text','`Departemen` text','`NDays` text','`Akhir Pekan` text','`Hari Libur` text','`Lama Hadir` text','`NDays_OT` text','`Lembur A.Pekan` text','`Libur Lembur` text')

def recover():
	"""recover tabel"""
	tab_pegawai
	tab_jadwal
	tab_liburan
	tab_laporan

#ubah_pegawai = EditTable('pegawai')
#ubah_jadwal = EditTable('jadwal')
#ubah_libur = EditTable('libur')
#ubah_laporan = EditTable('laporan')

def ubah_pegawai():
	'''sunting data pegawai'''
	pegawai=Table('pegawai')
	pegawai.column('nopeg','noakun','nokartu','nama','titel','departemen')
	pegawai.rows('nopeg','noakun','nokartu','nama','titel','departemen')
	
	def lihat():
		args = input('masukkan nama kolom atau biarkan kosong :\t')
		pegawai.view('pegawai',args)
	
	def tambah():
		"""tambah data pegawai"""
		tambah = InsertRow('pegawai')
		q0 = input('nopeg :\t')
		q1 = input('noakun :\t')
		q2 = input('nokartu :\t')
		q3 = input('nama :\t')
		q4 = input('titel :\t')
		q5 = input('departemen :\t')
		tambah.column = pegawai.column
		tambah.value(q0,q1,q2,q3,q4,q5)
		tambah.insert()
		
	def ubah():
		"""ubah data pegawai"""
		ubah.rows = pegawai.rows
		column = input('masukkan kolom pegawai yang akan dirubah :\t')
		ubah.column(column)
		value = input('masukkan nilai pegawai yang akan dirubah :\t')
		ubah.value(value)
		ubah = UpdateRow(row)

	def hapus():
		""" hapus data pegawai"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = DelRow(row)

def ubah_jadwal():
	"""sunting data jadwal"""
	jadwal=Table('pegawai')
	jadwal.column('nama','`Jam Masuk`','`Jam Keluar`','`Telat,`Pulang Cepat`','`Harus CIn`','`Harus COut`','`Normal`','`Akhir Pekan`','`Hari Libur`','`Waktu Real`')
	jadwal.rows('nama','`Jam Masuk`','`Jam Keluar`','`Telat,`Pulang Cepat`','`Harus CIn`','`Harus COut`','`Normal`','`Akhir Pekan`','`Hari Libur`','`Waktu Real`')
	
	def lihat():
		args = input('masukkan nama kolom atau biarkan kosong :\t')
		jadwal.view('jadwal',args)
	
	def tambah():
		"""tambah data jadwal"""
		tambah = InsertRow('jadwal')
		
		q0 = input('nama :\t')
		q1 = input('Jam Masuk :\t')
		q2 = input('Jam Keluar :\t')
		q3 = input('Telat :\t')
		q4 = input('Pulang Cepat :\t')
		q5 = input('Harus CIn :\t')
		q6 = input('Harus COut :\t')
		q7 = input('Normal :\t')
		q8 = input('Akhir Pekan :\t')
		q9 = input('Hari Libur :\t')
		q10 = input('Waktu Real :\t')
		
		tambah.column = jadwal.column
		tambah.value(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10)
		tambah.insert()

	def ubah():
		"""ubah data jadwal"""
		ubah.rows = jadwal.rows
		column = input('masukkan kolom jadwal yang akan dirubah :\t')
		ubah.column(column)
		value = input('masukkan nilai jadwal yang akan dirubah :\t')
		ubah.value(value)
		ubah = UpdateRow(row)

	def hapus():
		""" hapus data jadwal"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = DelRow(row)

def ubah_libur():
	'''sunting data libur'''
	libur=Table('libur')
	libur.column('tanggal text','hari text')
	libur.rows('tanggal text','hari text')
	
	def lihat():
		"""lihat data libur"""
		args = input('masukkan nama kolom atau biarkan kosong :\t')
		libur.view('libur',args)
	
	def tambah():
		"""tambah data libur"""
		tambah = InsertRow('libur')
		q0 = input('tanggal' :\t')
		q1 = input('hari :\t')
		tambah.column = libur.column
		tambah.value(q0,q1)
		tambah.insert()
		
	def ubah():
		"""ubah data libur"""
		ubah.rows = pegawai.rows
		column = input('masukkan kolom libur yang akan dirubah :\t')
		ubah.column(column)
		value = input('masukkan nilai libur yang akan dirubah :\t')
		ubah.value(value)
		ubah = UpdateRow(row)

	def hapus():
		""" hapus data libur"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = DelRow(row)

def ubah_laporan():
	'''sunting data laporan'''
	laporan=Table('laporan')
	laporan.column('row_id integer primary key autoincrement','`NoPeg` text','`No. Akun` text','`No.` text','`Nama` text','`Auto-Assign` text','`Tanggal` text','`Jam Kerja` text','`Awal tugas` text','`Akhir tugas` text','`Masuk` text','`Keluar` text','`Normal` text','`Waktu real` text','`Telat` text','`Plg Awal` text','`Bolos` text','`Waktu Lembur` text','`Waktu Kerja` text','`Status` text','`Hrs C/In` text','`Hrs C/Out` text','`Departemen` text','`NDays` text','`Akhir Pekan` text','`Hari Libur` text','`Lama Hadir` text','`NDays_OT` text','`Lembur A.Pekan` text','`Libur Lembur` text')
	laporan.rows('row_id integer primary key autoincrement','`NoPeg` text','`No. Akun` text','`No.` text','`Nama` text','`Auto-Assign` text','`Tanggal` text','`Jam Kerja` text','`Awal tugas` text','`Akhir tugas` text','`Masuk` text','`Keluar` text','`Normal` text','`Waktu real` text','`Telat` text','`Plg Awal` text','`Bolos` text','`Waktu Lembur` text','`Waktu Kerja` text','`Status` text','`Hrs C/In` text','`Hrs C/Out` text','`Departemen` text','`NDays` text','`Akhir Pekan` text','`Hari Libur` text','`Lama Hadir` text','`NDays_OT` text','`Lembur A.Pekan` text','`Libur Lembur` text')
	
	def lihat():
		"""lihat data laporan"""
		args = input('masukkan nama kolom atau biarkan kosong :\t')
		laporan.view('laporan',args)
	
	def tambah():
		"""tambah data laporan"""
		tambah = InsertRow('laporan')
		q0 = input('`NoPeg` : 	')
		q1 = input('`No. Akun` : 	')
		q2 = input('`No.` : 	')
		q3 = input('`Nama` : 	')
		q4 = input('`Auto-Assign` : 	')
		q5 = input('`Tanggal` : 	')
		q6 = input('`Jam Kerja` : 	')
		q7 = input('`Awal tugas` : 	')
		q8 = input('`Akhir tugas` : 	')
		q9 = input('`Masuk` : 	')
		q10 = input('`Keluar` : 	')
		q11 = input('`Normal` : 	')
		q12 = input('`Waktu real` : 	')
		q13 = input('`Telat` : 	')
		q14 = input('`Plg Awal` : 	')
		q15 = input('`Bolos` : 	')
		q16 = input('`Waktu Lembur` : 	')
		q17 = input('`Waktu Kerja` : 	')
		q18 = input('`Status` : 	')
		q19 = input('`Hrs C/In` : 	')
		q20 = input('`Hrs C/Out` : 	')
		q21 = input('`Departemen` : 	')
		q22 = input('`NDays` : 	')
		q23 = input('`Akhir Pekan` : 	')
		q24 = input('`Hari Libur` : 	')
		q25 = input('`Lama Hadir` : 	')
		q26 = input('`NDays_OT` : 	')
		q27 = input('`Lembur A.Pekan` : 	')
		q28 = input('`Libur Lembur` : 	')
		tambah.column = libur.column
		tambah.value(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28)
		tambah.insert()

	def ubah():
		"""ubah data laporan"""
		ubah.rows = pegawai.rows
		column = input('masukkan kolom libur yang akan dirubah :\t')
		ubah.column(column)
		value = input('masukkan nilai libur yang akan dirubah :\t')
		ubah.value(value)
		ubah = UpdateRow(row)

	def hapus():
		""" hapus data laporan"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = DelRow(row)

def main():
	"""modul utama"""
	cnxn()
	
	conn.close()
	pass
	
if __name__ == '__main__':
main()
