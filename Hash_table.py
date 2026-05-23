class HashTable:
    #Konstruktor untuk membuat objek hash table baru.
    def __init__(self,size=100):
        self.size = size
        self.table = []

        for _ in range(size):
            self.table.append([])
    
    #Mengubah key menjadi angka indeks untuk penyimpanan
    def hash_function(self,key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
        
    #Memasukkan data baru atau memperbarui data lama jika sebelumnya sudah ada data.
    def insert(self , key, value):
        index = self.hash_function(key)

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key,value)
                return
            
        bucket.append((key,value))

    #method untuk Mengambil nilai (value) berdasarkan key.
    def get(self,key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
            
        return None
    
    #method untuk memeriksa apakah memiliki value atau tidak
    def contain(self,key):
        return self.get(key) is not None
    
    #method untuk manambahkan
    def increment(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, bucket[i][1] + 1)
                return
        
        bucket.append((key, 1))

    #method mengambil key dan value
    def items(self):
        result = []
        for bucket in self.table:
            for k, v in bucket:
                result.append((k, v))
        return result
        
    #method mengembalikan key
    def keys(self):
        result = []
        for bucket in self.table:
            for k, _ in bucket:
                result.append(k)
        return result
    
