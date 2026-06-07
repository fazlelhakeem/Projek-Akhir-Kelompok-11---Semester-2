import os

def read_file(nama):
   with open(nama, 'r') as dokumen:
      teks = dokumen.read()

   return teks

def create_file(nama, teks):
   with open(nama, 'w') as dokumen:
      dokumen.write(teks)

def append_file(nama, teks):
   with open (nama, 'a') as dokumen:
      dokumen.write(teks)

def delete_file(nama):
   os.remove(nama)

def hapus_isi(nama):
   with open(nama, 'w') as dokumen:
      dokumen.write()
