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

def cnxn():
	'''menyambungkan ke data/report.db'''
	try:
		conn=db.connect('data/report.db')
		print('koneksi berhasil')	
	except Exception:
		print(f'koneksi gagal\n{sys.exc_info()} \n')
		pass

def recover():
	"""recover tabel"""
	def tab_pegawai():
		try:
			conn.execute('''create table if not exist pegawai(
			noID integer primary key autoincrement
			,nopeg text
			,noakun text
			,nokartu text
			,nama text
			,titel text
			,departemen text)
			''')
			conn.commit()
			print('tabel pegawai berhasil dibuat')
		except Exception:
			print(f'tabel pegawai gagal dibuat karena:\n{sys.exc_info()} \n') 
	
	def tab_jadwal():
		try:
			conn.execute('''create table if not exist jadwal(
			noID integer primary key autoincrement
			,nama text
			,`Jam Masuk` text
			,`Jam Keluar` text
			,`Telat` text
			,`Pulang Cepat` text
			,`Harus CIn` text
			,`Harus COut` text
			,`Normal` text
			,`Akhir Pekan` text
			,`Hari Libur` text
			,`Waktu Real` text)
			''')
			conn.commit()
			print('tabel jadwal berhasil dibuat')
		except Exception:
			print(f'tabel jadwal gagal dibuat karena:\n{sys.exc_info()} \n')
	def tab_liburan():
		try:
			conn.execute('''create table if not exist liburan(
			tanggal text
			,hari text)
			''')
			conn.commit()
			print('tabel liburan berhasil dibuat')
		except Exception:
			print(f'tabel liburan gagal dibuat karena:\n{sys.exc_info()} \n') 
	
	def tab_laporan():
		try:
			"""buat table baru di database"""
			conn = db.connect("data/report.db")
			conn.execute("""create table if not exists absensi (row_id integer primary key autoincrement
			,`NoPeg` text
			,`No. Akun` text
			,`No.` text
			,`Nama` text
			,`Auto-Assign` text
			,`Tanggal` text
			,`Jam Kerja` text
			,`Awal tugas` text
			,`Akhir tugas` text
			,`Masuk` text
			,`Keluar` text
			,`Normal` text
			,`Waktu real` text
			,`Telat` text
			,`Plg Awal` text
			,`Bolos` text
			,`Waktu Lembur` text
			,`Waktu Kerja` text
			,`Status` text
			,`Hrs C/In` text
			,`Hrs C/Out` text
			,`Departemen` text
			,`NDays` text
			,`Akhir Pekan` text
			,`Hari Libur` text
			,`Lama Hadir` text
			,`NDays_OT` text
			,`Lembur A.Pekan` text
			,`Libur Lembur` text);""")
			conn.commit()
			print('tabel laporan berhasil dibuat')
		except Exception:
			print(f'tabel laporan gagal dibuat karena:\n{sys.exc_info()} \n') 

def vari_bl(baru,lama):
	"""nilai var baru dan lama"""
	if baru == None or baru == "":
		return lama
	else:
		return baru

def vari_null(var):
	"""nilai var null"""
	if var == None or var == "":
		return ""
	else:
		return var

def ubah_pegawai():
	cnxn()
	"""ubah & hapus data pegawai"""
	def view_all():
		cls()
		"""lihat semua data pegawai"""
		conn.execute('select * from pegawai')
		return ubah_pegawai()
	def tambah():
		cls()
		"""tambah data pegawai"""
		q0 = input('nopeg :\t')
		q1 = input('noakun :\t')
		q2 = input('nokartu :\t')
		q3 = input('nama :\t')
		q4 = input('titel :\t')
		q5 = input('departemen :\t')
		
		q0 = vari_null(q0)
		q1 = vari_null(q1)
		q2 = vari_null(q2)
		q3 = vari_null(q3)
		q4 = vari_null(q4)
		q5 = vari_null(q5)
		try:
			conn.execute(f'''insert into pegawai(
			nopeg,noakun,nokartu,nama,titel,departemen)
			values({q0},{q1},{q2},{q3},{q4},{q5});
			''')
			conn.commit()
			cls()
			print(f'\ndata pegawai {q3} telah masuk ke database \n')
			return ubah_pegawai()
		except Exception:
			cls()
			print(f'\ndata pegawai {q3} gagal masuk karena:\n{sys.exc_info()}\n') 
			return ubah_pegawai()
	
	def ubah():
		"""tambah data pegawai"""
		cls()
		cari = input('masukkan ID pegawai yang akan dirubah :\t')
		try:
			data_lama=conn.execute(f'select from pegawai where noID={cari};')
			print('ubah data pegawai? \t')
			opsi_ubah = input('Ya atau Tidak \n')
			if opsi_ubah.lower == 'y':
				print('masukkan data yang akan dirubah \n')
				q0 = input('nopeg :\t')
				q1 = input('noakun :\t')
				q2 = input('nokartu :\t')
				q3 = input('nama :\t')
				q4 = input('titel :\t')
				q5 = input('departemen :\t')
				
				q0 = vari_bl(q0,data_lama[0])
				q1 = vari_bl(q1,data_lama[1])
				q2 = vari_bl(q2,data_lama[2])
				q3 = vari_bl(q3,data_lama[3])
				q4 = vari_bl(q4,data_lama[4])
				q5 = vari_bl(q5,data_lama[5])
				try:
					conn.execute(f'''update nopeg
					,noakun
					,nokartu
					,nama
					,titel
					,departemen	from pegawai where noID={cari} 
					values({q0},{q1},{q2},{q3},{q4},{q5});
					''')
					cls()
					print(f'\ndata pegawai {nama} berhasil diubah \n')
					return ubah_pegawai()
			else:
				cls()
				print('perintah dibatalkan \n')
				return ubah_pegawai()
		except Exception:
			cls()
			print(f'\ndata pegawai tidak ditemukan karena:\n{sys.exc_info()}\n') 
			return ubah_pegawai()
	
	def hapus():
		""" hapus data pegawai"""
		cls()
		cari = input('masukkan ID pegawai yang akan dirubah :\t')
		try:
			data_lama=conn.execute(f'select from pegawai where noID={cari};')
			print('hapus data pegawai? \t')
			opsi_ubah = input('Ya atau Tidak \n')
			if opsi_ubah.lower == 'y':
				try:
					execute(f'delete from pegawai where noID={cari};')
					cls()
					print('data pegawai telah dihapus \n')
					return ubah_pegawai()
				except Exception:
					cls()
					print(f'\ndata pegawai tidak bisa dihapus karena:\n{sys.exc_info()}\n') 
					return ubah_pegawai()
			else:
				cls()
				print('perintah dibatalkan \n')
				return ubah_pegawai()
		except Exception:
			cls()
			print(f'\ndata pegawai tidak ditemukan karena:\n{sys.exc_info()}\n') 
			return ubah_pegawai()

def ubah_jadwal():
	cnxn()
	"""ubah & hapus data jadwal"""
	def view_all():
		cls()
		"""lihat semua data jadwal"""
		conn.execute('select * from jadwal')
		return ubah_jadwal()
	def tambah():
		cls()
		"""tambah data jadwal"""
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
		
		q0 = vari_null(q0)
		q1 = vari_null(q1)
		q2 = vari_null(q2)
		q3 = vari_null(q3)
		q4 = vari_null(q4)
		q5 = vari_null(q5)
		q6 = vari_null(q6)
		q7 = vari_null(q7)
		q8 = vari_null(q8)
		q9 = vari_null(q9)
		q10 = vari_null(q10)
		
		try:
			conn.execute(f'''insert into jadwal(
			nama,`Jam Masuk`,`Jam Keluar`,`Telat,`Pulang Cepat`,`Harus CIn`,`Harus COut`,`Normal`,`Akhir Pekan`,`Hari Libur`,`Waktu Real`)
			values({q0},{q1},{q2},{q3},{q4},{q5},{q6},{q7},{q8},{q9},{q10});
			''')
			conn.commit()
			cls()
			print(f'\ndata jadwal {q0} telah masuk ke database \n')
			return ubah_jadwal()
		except Exception:
			cls()
			print(f'\ndata jadwal {q0} gagal masuk karena:\n{sys.exc_info()}\n') 
			return ubah_jadwal()

	def ubah():
		"""tambah data jadwal"""
		cls()
		cari = input('masukkan ID jadwal yang akan dirubah :\t')
		try:
			data_lama=conn.execute(f'select from jadwal where noID={cari};')
			print('ubah data jadwal? \t')
			opsi_ubah = input('Ya atau Tidak \n')
			if opsi_ubah.lower == 'y':
				print('masukkan data yang akan dirubah \n')
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
				
				q0 = vari_bl(q,data_lama[0])
				q1 = vari_bl(q,data_lama[1])
				q2 = vari_bl(q,data_lama[2])
				q3 = vari_bl(q,data_lama[3])
				q4 = vari_bl(q,data_lama[4])
				q5 = vari_bl(q,data_lama[5])
				q6 = vari_bl(q,data_lama[6])
				q7 = vari_bl(q,data_lama[7])
				q8 = vari_bl(q,data_lama[8])
				q9 = vari_bl(q,data_lama[9])
				q10 = vari_bl(q,data_lama[10])
				try:
					conn.execute(f'''update nama,`Jam Masuk`,`Jam Keluar`,`Telat,`Pulang Cepat`,`Harus CIn`,`Harus COut`,`Normal`,`Akhir Pekan`,`Hari Libur`,`Waktu Real`)	from jadwal where noID={cari} 
					values({q0},{q1},{q2},{q3},{q4},{q5},{q6},{q7},{q8},{q9},{q10});
					''')
					cls()
					print(f'\ndata jadwal {nama} berhasil diubah \n')
					return ubah_jadwal()
			else:
				cls()
				print('perintah dibatalkan \n')
				return ubah_jadwal()
		except Exception:
			cls()
			print(f'\ndata jadwal tidak ditemukan karena:\n{sys.exc_info()}\n') 
			return ubah_jadwal()
	
	def hapus():
		""" hapus data jadwal"""
		cls()
		cari = input('masukkan ID jadwal yang akan dirubah :\t')
		try:
			data_lama=conn.execute(f'select from jadwal where noID={cari};')
			print('hapus data jadwal? \t')
			opsi_ubah = input('Ya atau Tidak \n')
			if opsi_ubah.lower == 'y':
				try:
					execute(f'delete from jadwal where noID={cari};')
					cls()
					print('data jadwal telah dihapus \n')
					return ubah_jadwal()
				except Exception:
					cls()
					print(f'\ndata jadwal tidak bisa dihapus karena:\n{sys.exc_info()}\n') 
					return ubah_jadwal()
			else:
				cls()
				print('perintah dibatalkan \n')
				return ubah_jadwal()
		except Exception:
			cls()
			print(f'\ndata jadwal tidak ditemukan karena:\n{sys.exc_info()}\n') 
			return ubah_jadwal()

def ubah_libur():
	cnxn()
	"""ubah & hapus data libur"""
	def view_all():
		cls()
		"""lihat semua data libur"""
		conn.execute('select * from libur')
		return ubah_libur()

	def tambah():
		cls()
		"""tambah data libur"""
		q0 = input('tanggal :\t')
		q1 = input('hari :\t')
		
		q0 = vari_null(q0)
		q1 = vari_null(q1)

		try:
			conn.execute(f'''insert into libur(tanggal,libur)
			values({q0},{q1},{q2},{q3},{q4},{q5});
			''')
			conn.commit()
			cls()
			print(f'\ndata libur {q1} telah masuk ke database \n')
			return ubah_libur()
		except Exception:
			cls()
			print(f'\ndata libur {r} gagal masuk karena:\n{sys.exc_info()}\n') 
			return ubah_libur()
	
	def ubah():
		"""tambah data libur"""
		cls()
		cari = input('masukkan ID libur yang akan dirubah :\t')
		try:
			data_lama=conn.execute(f'select from libur where noID={cari};')
			print('ubah data libur? \t')
			opsi_ubah = input('Ya atau Tidak \n')
			if opsi_ubah.lower == 'y':
				print('masukkan data yang akan dirubah \n')
				q0 = input('nopeg :\t')
				q1 = input('noakun :\t')
				q2 = input('nokartu :\t')
				q3 = input('nama :\t')
				q4 = input('titel :\t')
				q5 = input('departemen :\t')
				
				q0 = vari_bl(q0,data_lama[0])
				q1 = vari_bl(q1,data_lama[1])
				q2 = vari_bl(q2,data_lama[2])
				q3 = vari_bl(q3,data_lama[3])
				q4 = vari_bl(q4,data_lama[4])
				q5 = vari_bl(q5,data_lama[5])
				try:
					conn.execute(f'''update nopeg
					,noakun
					,nokartu
					,nama
					,titel
					,departemen	from libur where noID={cari} 
					values({q0},{q1},{q2},{q3},{q4},{q5});
					''')
					cls()
					print(f'\ndata libur {nama} berhasil diubah \n')
					return ubah_libur()
			else:
				cls()
				print('perintah dibatalkan \n')
				return ubah_libur()
		except Exception:
			cls()
			print(f'\ndata libur tidak ditemukan karena:\n{sys.exc_info()}\n') 
			return ubah_libur()
	
	def hapus():
		""" hapus data libur"""
		cls()
		cari = input('masukkan ID libur yang akan dirubah :\t')
		try:
			data_lama=conn.execute(f'select from libur where noID={cari};')
			print('hapus data libur? \t')
			opsi_ubah = input('Ya atau Tidak \n')
			if opsi_ubah.lower == 'y':
				try:
					execute(f'delete from libur where noID={cari};')
					cls()
					print('data libur telah dihapus \n')
					return ubah_libur()
				except Exception:
					cls()
					print(f'\ndata libur tidak bisa dihapus karena:\n{sys.exc_info()}\n') 
					return ubah_libur()
			else:
				cls()
				print('perintah dibatalkan \n')
				return ubah_libur()
		except Exception:
			cls()
			print(f'\ndata libur tidak ditemukan karena:\n{sys.exc_info()}\n') 
			return ubah_libur()

def main():
	"""modul utama"""
	cnxn()
	
	conn.close()
	pass
	
if __name__ == '__main__':
main()
