from Hash_table import HashTable

#menghitung banyak kemunculan suatu kata
def hitung_frekuen(words):
    ht = HashTable()

    for kata in words:
        ht.increment(kata)

    return ht

#menghitung total kata yang ada
def total_kata(words):
    count = 0
    for _ in words:
        count += 1

    return count

#mengambil kata unik atau keys
def get_kata_unik(ht):
    return ht.keys()