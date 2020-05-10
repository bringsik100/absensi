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
from sqlite import Error as er
import sys
import os
from proses import process

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
		self.conn = db.connect(f'{self.dbname}')
		self.cursor = self.conn.cursor()
		print('koneksi berhasil')

	def close(self):
		self.conn.close()

class CreateTable(DataBase): 
	'''objek pembuat tabel'''
	def __init__(self.table,*column):
		self.table = table
		self.column = column

	def create(self,table):
		'''metode utama'''
		try:
			self.cursor.execute(f'create table if not exists {self.table}{self.column};')
			self.conn.commit()
			print(f'buat data {self.table} berhasil \n')
		except Exception:
			print(f'buat tabel {self.table} gagal \n {sys.exc_info()} \n error = {er}\n')



def recover():
	'''modul pembuat tabel'''
	tab_pegawai = CreateTable('pegawai','noID integer primary key autoincrement','nopeg text','noakun text','nokartu text','nama text','titel text','departemen text')
	tab_pegawai.create()

	tab_jadwal = CreateTable('jadwal','noID integer primary key autoincrement','nama text','`Jam Masuk` text','`Jam Keluar` text','`Telat` text','`Pulang Cepat` text','`Harus CIn` text','`Harus COut` text','`Normal` text','`Akhir Pekan` text','`Hari Libur` text','`Waktu Real` text')
	tab_jadwal.create()

	tab_liburan = CreateTable('liburan','tanggal text','hari text')
	tab_liburan.create()

	tab_laporan = CreateTable('laporan','row_id integer primary key autoincrement','`NoPeg` text','`No. Akun` text','`No.` text','`Nama` text','`Auto-Assign` text','`Tanggal` text','`Jam Kerja` text','`Awal tugas` text','`Akhir tugas` text','`Masuk` text','`Keluar` text','`Normal` text','`Waktu real` text','`Telat` text','`Plg Awal` text','`Bolos` text','`Waktu Lembur` text','`Waktu Kerja` text','`Status` text','`Hrs C/In` text','`Hrs C/Out` text','`Departemen` text','`NDays` text','`Akhir Pekan` text','`Hari Libur` text','`Lama Hadir` text','`NDays_OT` text','`Lembur A.Pekan` text','`Libur Lembur` text')
	tab_laporan.create()

#ubah_pegawai = EditTable('pegawai')
#ubah_jadwal = EditTable('jadwal')
#ubah_libur = EditTable('libur')
#ubah_laporan = EditTable('laporan')

class Ubah:
	'''objek untuk melihat, menambah, mengubah, dan menghapus data'''
	def __init__(self,dbname,table):
	self.conn = db.connect(dbname)
	self.curs = self.conn.cursor()
	self.table = self.table
	self.column = None
	self.rows = self.curs.execute(f'select * from {self.table};').fetchall()

	def view(self):
		'''fungsi untuk melihat data'''
		for row in self.rows:
			print(row)

	def inserts(self,values):
		'''fungsi untuk menambah data'''
		self.values=values
		try:
			self.curs.execute(f'insert into {self.table}{self.column} values {self.values};')
			print(f'menambahkan data ke {self.table } berhasil \n')
		except Exception:
			print(f'menambahkan data ke tabel {self.table} gagal \n {sys.exc_info()} \n error = {er}\n')
	
	def updates(self,row,**kwargs):
		'''fungsi untuk mengubah data'''
		self.row = row
		self.kwargs=kwargs
		try:
			self.curs.execute(f'update {self.table} set {self.kwargs} where ID = {self.row};')
			print(f'mengubah data di tabel {self.table } berhasil \n')
		except Exception:
			print(f'menngubah data di tabel {self.table} gagal \n {sys.exc_info()} \n error = {er}\n')
	
	def delrow(self,row_id):
		'''fungsi untuk menghapus data'''
		self.row_id = row_id
		try:
			self.curs.execute(f'delete from {self.table} where ID = {row_id}')
			self.conn.commit()
			print(f'menghapus data di tabel {self.table } berhasil \n')
		except Exception:
			print(f'menghapus data di tabel {self.table} gagal \n {sys.exc_info()} \n error = {er}\n')

def pegawai():
	ubah_pegawai=Ubah('report.db','pegawai')
	ubah_pegawai.column = ['nopeg','noakun','nokartu','nama','titel','departemen']

	def lihat():
		'''lihat data pegawai'''
		ubah_pegawai.view()

	def tambah(self):
		"""tambah data pegawai"""
		q0 = input('nopeg :\t')
		q1 = input('noakun :\t')
		q2 = input('nokartu :\t')
		q3 = input('nama :\t')
		q4 = input('titel :\t')
		q5 = input('departemen :\t')
		ubah_pegawai.insert(q0,q1,q2,q3,q4,q5)

	def ubah(self):
		"""ubah data pegawai"""
		row = input('masukkan nomor baris pegawai yang akan dirubah :\t')
		kwargs = input('masukkan kolom dan data pegawai yang akan dirubah :\t')
		ubah_pegawai.updates(row,kwargs)

	def hapus(self):
		""" hapus data pegawai"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = delrow(row)

def jadwal():
	"""sunting data jadwal"""
	ubah_jadwal= Ubah('jadwal')
	ubah_jadwal.column('nama','`Jam Masuk`','`Jam Keluar`','`Telat,`Pulang Cepat`','`Harus CIn`','`Harus COut`','`Normal`','`Akhir Pekan`','`Hari Libur`','`Waktu Real`')

	def lihat(self):
		'''lihat data jadwal'''
		ubah_jadwal.view()
	
	def tambah(self):
		'''tambah data jadwal'''
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
		ubah_jadwal.inserts(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10)

	def ubah(self):
		"""ubah data jadwal"""
		row = input('masukkan nomor baris jadwal yang akan dirubah :\t')
		kwargs = input('masukkan kolom dan data jadwal yang akan dirubah :\t')
		ubah_jadwal.updates(row,kwargs)

	def hapus(self):
		""" hapus data jadwal"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = delrow(row)

def libur():
	'''sunting data libur'''
	ubah_jadwal= Ubah('jadwal')
	libur.column('tanggal text','hari text')

	def lihat(self):
		"""lihat data libur"""
		ubah_libur.view()

	def tambah(self):
		"""tambah data libur"""
		q0 = input('tanggal :\t')
		q1 = input('hari :\t')
		ubah_libur.inserts(q0,q1)
		
	def ubah(self):
		"""ubah data libur"""
		row = input('masukkan baris libur yang akan dirubah :\t')
		kwargs = input('masukkan nilai libur yang akan dirubah :\t')
		ubah_libur.updates(row,kwargs)

	def hapus(self):
		""" hapus data libur"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = delrow(row)

def laporan():
	'''sunting data laporan'''
	ubah_laporan=Table('laporan')
	laporan.column('row_id integer primary key autoincrement','`NoPeg` text','`No. Akun` text','`No.` text','`Nama` text','`Auto-Assign` text','`Tanggal` text','`Jam Kerja` text','`Awal tugas` text','`Akhir tugas` text','`Masuk` text','`Keluar` text','`Normal` text','`Waktu real` text','`Telat` text','`Plg Awal` text','`Bolos` text','`Waktu Lembur` text','`Waktu Kerja` text','`Status` text','`Hrs C/In` text','`Hrs C/Out` text','`Departemen` text','`NDays` text','`Akhir Pekan` text','`Hari Libur` text','`Lama Hadir` text','`NDays_OT` text','`Lembur A.Pekan` text','`Libur Lembur` text')

	def lihat(self):
		"""lihat data libur"""
		ubah_laporan.view()

	def tambah(self):
		"""tambah data laporan"""
		q0 = input('`NoPeg` : ')
		q1 = input('`No. Akun` : ')
		q2 = input('`No.` : ')
		q3 = input('`Nama` : ')
		q4 = input('`Auto-Assign` : ')
		q5 = input('`Tanggal` : ')
		q6 = input('`Jam Kerja` : ')
		q7 = input('`Awal tugas` : ')
		q8 = input('`Akhir tugas` : ')
		q9 = input('`Masuk` : ')
		q10 = input('`Keluar` : ')
		q11 = input('`Normal` : ')
		q12 = input('`Waktu real` : ')
		q13 = input('`Telat` : ')
		q14 = input('`Plg Awal` : ')
		q15 = input('`Bolos` : ')
		q16 = input('`Waktu Lembur` : ')
		q17 = input('`Waktu Kerja` : ')
		q18 = input('`Status` : ')
		q19 = input('`Hrs C/In` : ')
		q20 = input('`Hrs C/Out` : ')
		q21 = input('`Departemen` : ')
		q22 = input('`NDays` : ')
		q23 = input('`Akhir Pekan` : ')
		q24 = input('`Hari Libur` : ')
		q25 = input('`Lama Hadir` : ')
		q26 = input('`NDays_OT` : ')
		q27 = input('`Lembur A.Pekan` : ')
		q28 = input('`Libur Lembur` : ')
		ubah_libur.inserts(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28)

	def ubah(self):
		"""ubah data laporan"""
		row = input('masukkan baris laporan yang akan dirubah :\t')
		kwargs = input('masukkan nilai laporan yang akan dirubah :\t')
		ubah_laporan.updates(row,kwargs)

	def hapus(self):
		""" hapus data laporan"""
		row = input('masukkan baris data yang akan dihapus :\t')
		hapus = delrow(row)

def main():
	"""modul utama"""
	pass
	
if __name__ == '__main__':
	main()
