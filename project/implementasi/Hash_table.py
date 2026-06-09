class HashTable:
    # Konstruktor untuk membuat objek hash table baru
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # BUG FIX: range(10) → range(self.size)

    # Mengubah key menjadi angka indeks untuk penyimpanan
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    # Memasukkan data baru atau memperbarui data lama jika sebelumnya sudah ada
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    # Mengambil nilai (value) berdasarkan key
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    # Memeriksa apakah key ada di dalam tabel
    def contain(self, key):
        return self.get(key) is not None

    # Menambahkan frekuensi data yang sudah ada, atau mendaftarkan baru dengan nilai 1
    def increment(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, bucket[i][1] + 1)
                return

        bucket.append((key, 1))

    # Mengambil semua pasangan key-value
    def items(self):
        result = []
        for bucket in self.table:
            for k, v in bucket:
                result.append((k, v))
        return result

    # Mengembalikan semua key
    def keys(self):
        result = []
        for bucket in self.table:
            for k, _ in bucket:
                result.append(k)
        return result
