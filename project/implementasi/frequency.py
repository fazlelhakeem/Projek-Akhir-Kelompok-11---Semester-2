from . import Hash_table as ht

#menghitung banyak kemunculan suatu kata
def hitung_frekuen(words):
    h_table = ht.HashTable()

    for kata in words:
        h_table.increment(kata)

    return h_table

#menghitung total kata yang ada
def total_kata(words):
    count = 0
    for _ in words:
        count += 1

    return count

#mengambil kata unik atau keys
def get_kata_unik(ht):
    return ht.keys()