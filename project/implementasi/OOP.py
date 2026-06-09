#File untuk mengimplementasikan OOP

import os
from . import Circular_Linked_List as cll
from . import file_handler as fh

class DaftarDocument:
   def __init__(self):
      self.data = cll.Circular_Linked_list()
      self.length = 0

   def tambah_daftar(self, tambah):
      self.data.tambah(tambah)
      self.length += 1

   def hapus_daftar(self, kurang):
      if self.data.hapus(kurang):
         self.length -= 1
         return 'File telah dihapus'
      else:
         return 'File tidak ada'

   def get_list_data(self):
      hasil = self.data.to_list()
      
      return hasil

   def search_dokumen(self, target):
      hasil = self.data.search(target, self.length)

      return hasil
      
   @staticmethod
   def init_daftar_document():
      list_nama = fh.read_file('daftar dokumen.txt').splitlines()

      daftar = DaftarDocument()

      for nama in list_nama:
         daftar.tambah_daftar(nama)

      return daftar

   @staticmethod
   def update_daftar(daftar_lst):
      daftar = DaftarDocument()
      daftar_str = '\n'.join(daftar_lst)

      fh.create_file('daftar dokumen.txt', daftar_str)

      for nama in daftar_lst:
         daftar.tambah_daftar(nama)

      return daftar