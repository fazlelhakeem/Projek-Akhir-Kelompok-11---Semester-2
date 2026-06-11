#File untuk menyimpan fitur-fitur di menu utama
import implementasi.OOP as dd
import implementasi.file_handler as fh
from . import data as dt
from . import similarity as sim
from . import preprocessing as pp


#Fungsi untuk create document
def create_document():
   while True:
      print('\n(ketik "0" untuk kembali)')

      display_daftar()

      while True:
         nama_file = input('\nMasukkan nama file yang ingin anda buat: ')

         if nama_file == '0':
            back = dt.log_menu.hapus()
            back()
            return

         daftar_lst = dt.daftar_dokumen.data.to_list()

         if nama_file in daftar_lst:
            pilih = input('File dengan nama tersebut sudah ada, apakah anda ingin membuat ulang (y/n)? ')
            if pilih.lower() == 'y':
               break
         else:
            daftar_lst.append(nama_file)
            dd.DaftarDocument.update_daftar(daftar_lst)
            break

      print('\nTuliskan teks yang ingin anda isi di bawah ini:')
      print('ketik "END" untuk mengakhiri. ketik "BACK" untuk undo baris sebelumnya')

      teks_perbaris = []
      while True:
         one_line = input()
         if one_line.strip() == 'END':
            break
         elif one_line.strip() == 'BACK':
            if teks_perbaris:
               teks_perbaris.pop()
            continue
         teks_perbaris.append(one_line)

      teks_file = '\n'.join(teks_perbaris)
      fh.create_file('file txt/' + nama_file + '.txt', teks_file)

      dt.daftar_dokumen = dd.DaftarDocument.update_daftar(daftar_lst)
      print(f'\nFile {nama_file}.txt berhasil dibuat!')


#Fungsi untuk delete document
def delete_document():
   while True:
      print('\n(ketik "0" untuk kembali)')

      display_daftar()

      while True:
         try:
            nama_file = input('\nMasukkan nama file yang ingin anda hapus: ')

            if nama_file == '0':
               back = dt.log_menu.hapus()
               back()
               return

            fh.delete_file('file txt/' + nama_file + '.txt')

         except FileNotFoundError:
            print(f'File {nama_file}.txt tidak ditemukan')
         else:
            daftar_lst = dt.daftar_dokumen.data.to_list()
            daftar_lst.remove(nama_file)
            dt.daftar_dokumen = dd.DaftarDocument.update_daftar(daftar_lst)
            break

      print(f'\nFile {nama_file}.txt berhasil dihapus!')


#Fungsi untuk menampilkan isi (teks) document
def display_teks(teks, nama_file):
   if teks == '':
      print(f'\nFile {nama_file}.txt kosong')
   else:
      print(f'\nFile : {nama_file}.txt')
      print('=' * 50)
      print(teks)
      print('=' * 50)

   print('\n1. Tambah Isi File')
   print('2. Hapus Isi File')
   print('0. Kembali')

   pilih = int(input('\nPilih menu: '))
   match pilih:
      case 1:
         dt.log_menu.tambah(display_teks)
         tambah_isi(teks, nama_file)
      case 2:
         dt.log_menu.tambah(display_teks)
         hapus_isi(teks, nama_file)
      case 0:
         back = dt.log_menu.hapus()
         back()
         return


#Fungsi untuk memilih file yang ingin dilihat isinya
def look_document():
   print('\n(ketik "0" untuk kembali)')

   while True:
      try:
         nomor_file = int(input('\nMasukkan nomor file yang ingin dilihat: '))

         if nomor_file == 0:
            back = dt.log_menu.hapus()
            back()
            return

         if nomor_file > dt.daftar_dokumen.length or nomor_file < 1:
            raise ValueError

      except ValueError:
         print('\nMohon masukkan nomor yang valid!')
      else:
         break

   try:
      nama_file = dt.daftar_dokumen.search_dokumen(nomor_file)
      teks = fh.read_file('file txt/' + nama_file + '.txt')
   except FileNotFoundError:
      print(f'\nFile {nama_file} tidak ditemukan!')
   else:
      dt.log_menu.tambah(look_document)
      display_teks(teks, nama_file)

#Fungsi untuk menambah isi file
def tambah_isi(teks, nama_file):
   print('\nTuliskan teks yang ingin anda tambahkan:')
   print('ketik "END" untuk mengakhiri. ketik "BACK" untuk undo baris sebelumnya')

   teks_perbaris = []
   while True:
      one_line = input()
      if one_line.strip() == 'END':
         break
      elif one_line.strip() == 'BACK':
         if len(teks_perbaris) == 0:
            back = dt.log_menu.hapus()
            back(teks, nama_file)
            return
         teks_perbaris.pop()
         continue
      teks_perbaris.append(one_line)

   teks_file = '\n'.join(teks_perbaris)
   fh.append_file('file txt/' + nama_file + '.txt', '\n' + teks_file)

   print(f'\nBerhasil menambah isi file {nama_file}.txt')
   teks_baru = fh.read_file('file txt/' + nama_file + '.txt')

   back = dt.log_menu.hapus()
   back(teks_baru, nama_file)
   return


#Fungsi untuk menghapus isi file
def hapus_isi(teks, nama_file):
   pilih = input(f'\nApakah anda yakin ingin menghapus isi file {nama_file}.txt (y/n)? ')

   if pilih.lower() == 'n':
      back = dt.log_menu.hapus()
      back(teks, nama_file)   
      return

   fh.hapus_isi('file txt/' + nama_file + '.txt')
   print(f'\nFile {nama_file}.txt berhasil dikosongkan')

   back = dt.log_menu.hapus()
   back('', nama_file)
   return


#Fungsi untuk menampilkan daftar file
def display_daftar():
   print('\n      Daftar File')
   print('=' * 23)

   if dt.daftar_dokumen.length == 0:
      print('Belum ada file yang dibuat')
      return False    

   print('No |       Nama       |')
   print('-' * 23)

   no = 1
   current = dt.daftar_dokumen.data.head
   while no <= dt.daftar_dokumen.length:
      print(f'{no:<2} | {current.data:<17}|')
      no += 1
      current = current.next

   print('=' * 23)
   return True


#Fungsi untuk menu lihat daftar file
def list_document():
   display_daftar()

   print('\n1. Lihat Isi File')
   print('0. Kembali')

   pilih = int(input('\nPilih menu: '))
   match pilih:
      case 1:
         dt.log_menu.tambah(list_document)
         look_document()
      case 0:
         back = dt.log_menu.hapus()
         back()
         return


#Fungsi untuk menu cek similarity
def cek_similarity():
   print('(ketik "0" untuk kembali)')

   while True:
      ada = display_daftar()
      if not ada:
         back = dt.log_menu.hapus()  
         if back:
            back()
         return

      try:
         doc1 = input('Masukkan nama dokumen pertama: ')
         if doc1 == '0':
            back = dt.log_menu.hapus()
            if back:
               back()
            return

         teks1 = fh.read_file('file txt/' + doc1 + '.txt')

         doc2 = input('Masukkan nama dokumen kedua: ')
         if doc2 == '0':
            back = dt.log_menu.hapus()
            if back:
               back()
            return

         teks2 = fh.read_file('file txt/' + doc2 + '.txt')

      except FileNotFoundError:
         print('\nNama file yang anda masukkan tidak valid')
      else:
         break

   hasil_sim = sim.hitung_similarity(teks1, teks2)

   # Simpan hasil ke Graph
   dt.similarity_graph.add_document(doc1)
   dt.similarity_graph.add_document(doc2)
   dt.similarity_graph.add_edge(doc1, doc2, hasil_sim)
   dt.similarity_graph.save_to_file('data file.txt')

   print(f'\nNilai kemiripan dokumen "{doc1}" dan "{doc2}" : {hasil_sim}%')

   print('\n1. Lihat Frekuensi Kata')
   print('0. Kembali')

   pilih = int(input('\nPilih menu: '))
   match pilih:
      case 1:
         dt.log_menu.tambah(cek_similarity)
         display_freq_kata(teks1, teks2, doc1, doc2)
      case 0:
         back = dt.log_menu.hapus()
         if back:
            back()
         return


#Fungsi untuk menu lihat riwayat similarity
def lihat_similarity():
   """
   Menampilkan riwayat semua similarity yang sudah pernah dihitung
   dalam sesi ini menggunakan Graph.
   """
   print('\n   Riwayat Similarity Dokumen ')
   print('=' * 57)

   edges = dt.similarity_graph.get_all_edges()

   if not edges:
      print('Belum ada similarity yang dihitung pada sesi ini.')
   else:
      print(f'\n{"No":<4} {"Dokumen 1":<22} {"Dokumen 2":<22} {"Similarity":>10}')
      print('-' * 57)
      for i, (d1, d2, s) in enumerate(edges, 1):
         print(f'{i:<4} {d1:<22} {d2:<22} {s:>9.2f}%')

   print('=' * 57)
   input('\nTekan Enter untuk kembali...')
   back = dt.log_menu.hapus()
   if back:
      back()


#Fungsi untuk menu lihat frekuensi kata
def display_freq_kata(teks1, teks2, doc1, doc2):
   while True:
      print('\n1. Tampilkan Berdasarkan Abjad')
      print('2. Tampilkan Berdasarkan Frekuensi')
      print('3. Cari Kata (Binary Search)')
      print('0. Kembali')

      pilih = int(input('\nPilih jenis tampilan: '))

      if pilih == 0:
         back = dt.log_menu.hapus()
         if back:
            back()
         return

      elif pilih == 1:
         freq1 = sim.frekuensi_kata(teks1)
         freq2 = sim.frekuensi_kata(teks2)
         sorted1 = sim.sort_abjad(freq1)
         sorted2 = sim.sort_abjad(freq2)
         cetak_frekuensi(sorted1, doc1)
         cetak_frekuensi(sorted2, doc2)

      elif pilih == 2:
         freq1 = sim.frekuensi_kata(teks1)
         freq2 = sim.frekuensi_kata(teks2)
         sorted1 = sim.sort_freq(freq1)
         sorted2 = sim.sort_freq(freq2)
         cetak_frekuensi(sorted1, doc1)
         cetak_frekuensi(sorted2, doc2)

      elif pilih == 3:
         target = input('\nMasukkan kata yang ingin dicari: ').lower().strip()

         #urutkan abjad lalu mencari menggunakan binary search
         freq1 = sim.frekuensi_kata(teks1)
         freq2 = sim.frekuensi_kata(teks2)
         sorted1 = sim.sort_abjad(freq1)
         sorted2 = sim.sort_abjad(freq2)

         hasil1 = sim.cari_kata(sorted1, target)
         hasil2 = sim.cari_kata(sorted2, target)

         print(f'\nHasil pencarian kata "{target}":')
         print('-' * 40)
         if hasil1:
            print(f'  {doc1:<20} : {hasil1[1]} kali')
         else:
            print(f'  {doc1:<20} : tidak ditemukan')

         if hasil2:
            print(f'  {doc2:<20} : {hasil2[1]} kali')
         else:
            print(f'  {doc2:<20} : tidak ditemukan')

      else:
         print('\nPilihan tidak valid!')

#Fungsi untuk  menampilkan frekuensi kata
def cetak_frekuensi(sorted_freq, nama_doc):
   """Helper untuk mencetak tabel frekuensi kata"""
   print(f'\nDaftar Frekuensi Kata — {nama_doc}')
   print('-' * 44)
   print(f'{"No":<4} {"Kata":<18} {"Frekuensi":>10}')
   print('-' * 44)
   for no, (kata, freq) in enumerate(sorted_freq, start=1):
      print(f'{no:<4} {kata:<18} {freq:>10}')
   print()
