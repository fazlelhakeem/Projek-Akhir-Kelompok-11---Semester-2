from implementasi.stack import Stack
import implementasi.file_handler as fh
import fitur.similarity as sim
import fitur.menu as mn 
import implementasi.OOP as dd
import fitur.data as dt

def main():
   log_menu = Stack()

   while True:
      print()
      print('='*32)
      print('   PENDETEKSI SIMILARITY TEKS')
      print('='*32)

      print('1. Cek Similarity')
      print('2. Create File')
      print('3. Delete File')
      print('4. Lihat Daftar File')
      print('0. Exit')

      pilih = int(input('\nPilih menu: '))

      match pilih:
         case 1:
            log_menu.tambah(main)

            while True:
               hasil = mn.cek_similarity()

               if hasil == 0:
                  back = log_menu.hapus
                  back()
                  return

               print('='*32)
               print('1. Lihat frekunsi kata')

         case 2:
            log_menu.tambah(main)

            while True:
               hasil = mn.create_document(dt.daftar_dokumen)

               if hasil == 0:
                  back = log_menu.hapus()
                  back()
                  return
               
               

         case 3:
            log_menu.tambah(main)

            while True:
               hasil = mn.delete_document()

               if hasil == 0:
                  back = log_menu.hapus()
                  back()
                  return

         case 4:
            log_menu.tambah(main)

            while True:
               hasil = mn.list_document()

               if hasil == 0:
                  back = log_menu.hapus()
                  back()
                  return

               

         case 0:
            return

if __name__ == '__main__':
   main()