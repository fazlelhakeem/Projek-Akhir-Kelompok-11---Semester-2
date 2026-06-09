from implementasi.stack import Stack
import implementasi.file_handler as fh
import fitur.similarity as sim
import fitur.menu as mn
import implementasi.OOP as dd
import fitur.data as dt


def main():
   while True:
      print()
      print('=' * 32)
      print('   PENGHITUNG SIMILARITY TEKS')
      print('=' * 32)
      print('1. Cek Similarity')
      print('2. Lihat Riwayat Similarity')
      print('3. Create File')
      print('4. Delete File')
      print('5. Lihat Daftar File')
      print('0. Exit')

      try:
         pilih = int(input('\nPilih menu: '))
      except ValueError:
         print('Masukkan angka yang valid!')
         continue

      match pilih:
         case 1:
            dt.log_menu.tambah(main)
            mn.cek_similarity()

         case 2:
            dt.log_menu.tambah(main)
            mn.lihat_similarity()

         case 3:
            dt.log_menu.tambah(main)
            mn.create_document()

         case 4:
            dt.log_menu.tambah(main)
            mn.delete_document()

         case 5:
            dt.log_menu.tambah(main)
            mn.list_document()

         case 0:
            print('\nTerima kasih telah menggunakan program ini!')
            exit()

         case _:
            print('Pilihan tidak valid!')


if __name__ == '__main__':
   main()
