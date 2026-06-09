#File untuk mengimplementasikan file handling

import os

#Fungsi untuk membaca teks file
def read_file(nama):
   with open(nama, 'r') as dokumen:
      teks = dokumen.read()

   return teks

#Fungsi untuk membuat file baru
def create_file(nama, teks):
   with open(nama, 'w') as dokumen:
      dokumen.write(teks)

#Fungsi untuk menambha isi file
def append_file(nama, teks):
   with open (nama, 'a') as dokumen:
      dokumen.write(teks)

#Fungsi untuk menambah isi file
def delete_file(nama):
   os.remove(nama)

#Fungsi untuk menghapus isi file
def hapus_isi(nama):
   with open(nama, 'w') as dokumen:
      dokumen.write("")
