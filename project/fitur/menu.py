#file untuk mnyimpan fitur-fitur di menu utama
import implementasi.OOP as dd
import implementasi.file_handler as fh
from . import data as dt

def create_document(daftar):
   print('\n(ketik "0" untuk kembali ke menu utama)')

   while True:
      nama_file = input('\nMasukkan nama file yang ingin anda buat: ')

      if nama_file == '0': #jika user ingin kembali
         return 0

      daftar_lst = dt.daftar_dokumen.data.to_list()

      if nama_file in daftar_lst:
         pilih = input('File dengan nama tersebut sudah ada, apakah anda ingin membuat ulang (y/n)? ')
         if pilih.lower() == 'y':
            break
      else:
         daftar_lst.append(nama_file)
         dd.DaftarDocument.update_daftar(daftar_lst)
         break

   print('\nTuliskan teks yang ingin anda isi di bawah ini: ')
   print('ketik "END" untuk mengakhiri. ketik "BACK" untuk undo baris sebelumnya')

   teks_perbaris = []
   while True:
      one_line = input()
      if one_line.strip() == 'END':
            break
      elif one_line.strip() == 'BACK':
         teks_perbaris.pop()
         continue

      teks_perbaris.append(one_line)

   teks_file = '\n'.join(teks_perbaris) #menggabungkan teks_perbaris yang berupa list menjadi string panjang
   fh.create_file('file txt/'+nama_file+'.txt', teks_file) #membuat file baru

   #mengupdate data file
   dt.daftar_dokumen = dd.DaftarDocument.update_daftar(daftar_lst)

   print(f'\nFile {nama_file}.txt berhasil dibuat!')

def delete_document():
   print('\n(ketik "0" untuk kembali ke menu utama)')

   while True:
      try:  
         nama_file = input('\nMasukkan nama file yang ingin anda hapus: ')

         if nama_file == '0':
            return 0
         
         fh.delete_file('file txt/'+nama_file+'.txt')

      except FileNotFoundError:
         print(f'File {nama_file}.txt tidak ditemukan')
      else:
         daftar_lst = dt.daftar_dokumen.data.to_list()
         daftar_lst.remove(nama_file)
         dt.daftar_dokumen.update_daftar(daftar_lst)
         break

   print(f'\nFile {nama_file}.txt berhasil dihapus!')

def look_document(daftar):
   print('(ketik "0" untuk kembali ke menu utama)\n')

   list_document(daftar)

   while True:
      try:
         nama_file = input('Masukkan nama file yang ingin anda hapus: ')

         if nama_file == 0:
            return 0

         teks = fh.read_file(nama_file+'.txt')

      except FileNotFoundError:
         print(f'File {nama_file} tidak ditemukan')
      else:
         break
   
   print('\n', teks)
   print()

def cek_similarity():
   print('(ketik "0" untuk kembali ke menu utama)')

   while True:
      try:
         doc1 = input('Masukkan nama dokumen pertama: ')

         if doc1 == 0:
            return 0
         teks1 = fh.read_file(doc1+'.txt')
         
         doc2 = input('Masukkan nama dokumen kedua: ')
         
         if doc2 == 0:
            return 0
         teks2 = fh.read_file(doc2+'.txt')
      except FileNotFoundError:
         print('\nNama file yang anda masukkan tidak valid')
      else:
         break

   hasil_sim = sim.cek_similarity(teks1, teks2)

   print(f'Nilai kemiripan kedua teks pada dokumen {doc1} dan {doc2} adalah: {hasil_sim}%\n')

def list_document():
   print('\n      Daftar File')
   print('-'*23)

   if dt.daftar_dokumen.length == 0:
      print('Belum ada file yang dibuat')
      return 0

   no = 1
   current = dt.daftar_dokumen.data.head
   print('No |       Nama       |')

   while no <= dt.daftar_dokumen.length:
      print(f'{no:<2} | {current.data:<17}|')
      no += 1
      current = current.next

   print('='*32)
   print('1. Lihat Isi File')
   print('0. Kembali')
   
   pilih = int(input('\nPilih menu: '))
   match pilih:
      case 1:
         log_menu.tambah(list_document)
         

      case 0:
         back = log_menu.hapus()
         back()
         return 