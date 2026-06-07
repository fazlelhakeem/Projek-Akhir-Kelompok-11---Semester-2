from . import preprocessing

def hitung_similarity(teks1, teks2):
   #Preprocessing dokumen
   preprocessed_teks1 = preprocessing.preprocess(teks1)
   preprocessed_teks2 = preprocessing.preprocess(teks2)

   #Menghitung jumlah kata unik di kedua dokumen
   teks1_unik = set(preprocessed_teks1)
   teks2_unik = set(preprocessed_teks2)
   gabung_unik = teks1_unik & teks2_unik
   total_unik = teks1_unik | teks2_unik

   #menghitung nilai similarity
   nilai_sim = (gabung_unik / total_unik) * 100

   return nilai_sim