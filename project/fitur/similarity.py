#File untuk melakukan perhitungan similarity
from . import preprocessing as pp
import implementasi.sorting as sort
import implementasi.searching as sc
import implementasi.frequency as fr
from implementasi.tree import Tree


#Fungsi untuk ekstrak kata dari tree
def ekstrak_dari_tree(tree):
   """
   Traversal melewati semua node 'word' di dalam tree, kumpulkan teksnya,
   lalu jalankan preprocessing (lowercase, hapus simbol, hapus stopwords).
   """
   kata_mentah = []
   for para in tree.root.children:
      for sent in para.children:
         for word in sent.children:
            w = word.data.strip()
            if w:
               kata_mentah.append(w)

   #Preprocessing menghasilkan list kata bersih
   return pp.preprocess(' '.join(kata_mentah))


#Fungsi utama similarity
def hitung_similarity(teks1, teks2):
   """
   Menghitung persentase kemiripan dua teks (Jaccard similarity).
   Alur:
     1. buat object tree untuk masing-masing dokumen
     2. ekstrak kata dari tree + preprocessing
     3. hitung frekuensi tiap kata dengan HashTable
     4. ambil kata unik dari HashTable
     5. Jaccard = irisan / gabungan * 100
   """
   #1. buat object tree
   tree1 = Tree()
   tree1.build_tree(teks1)
   tree2 = Tree()
   tree2.build_tree(teks2)

   #2. ekstrak kata dari tree
   kata1 = ekstrak_dari_tree(tree1)
   kata2 = ekstrak_dari_tree(tree2)

   #3. hitung frekuensi menggunakan HashTable
   ht1 = fr.hitung_frekuen(kata1)
   ht2 = fr.hitung_frekuen(kata2)

   #4. Ambil kata unik
   unik1 = set(fr.get_kata_unik(ht1))
   unik2 = set(fr.get_kata_unik(ht2))

   gabung = unik1 & unik2
   total  = unik1 | unik2

   if len(total) == 0: #jika tidak ada kata yang sama
      return 0.0

   #5. Hitung similarity
   nilai_sim = round((len(gabung) / len(total)) * 100, 2)
   return nilai_sim


#Fungsi untuk menghitung frekuensi kata (HashTable)
def frekuensi_kata(teks):
   #Menghitung frekuensi kemunculan setiap kata menggunakan HashTable.

   preprocessed_teks = pp.preprocess(teks)

   # Gunakan HashTable untuk menghitung frekuensi
   h_table = fr.hitung_frekuen(preprocessed_teks)

   # Konversi hasil HashTable ke dictionary 
   frekuensi = {}
   for kata, jumlah in h_table.items():
      frekuensi[kata] = jumlah

   return frekuensi


#Fungsi untuk sorting
def sort_freq(frekuensi):
   """Urutkan frekuensi dari terbanyak ke tersedikit (bubble sort)"""
   freq_lst = list(frekuensi.items())
   return tuple(sort.sort_by_frekuensi(freq_lst))


def sort_abjad(frekuensi):
   """Urutkan frekuensi secara alfabetis (bubble sort)"""
   freq_lst = list(frekuensi.items())
   return tuple(sort.sort_by_kata(freq_lst))


#Fungsi untuk mencari kata pada daftar frekuensi menggunakan binary search
def cari_kata(freq_abjad_tuple, target):
   """
   Mencari satu kata di daftar frekuensi yang sudah diurutkan abjad
   menggunakan Binary Search
   Mengembalikan tuple (kata, frekuensi) jika ditemukan, None jika tidak.
   """
   #Pisahkan hanya daftar kata
   kata_list = [item[0] for item in freq_abjad_tuple]
   indeks = sc.binary_search(kata_list, target)

   if indeks == -1:
      return None
   return freq_abjad_tuple[indeks]
