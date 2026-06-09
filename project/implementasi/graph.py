# file untuk membuat struktur data graph
class Graph:
   def __init__(self):
      self.document = []
      self.edges = {}

   def add_document(self, doc):
      """Menambahkan dokumen sebagai node di graph"""
      if doc not in self.document:
         self.document.append(doc)
         self.edges[doc] = []

   def add_edge(self, doc1, doc2, similarity):
      """
      Menambahkan edge antara dua dokumen.
      Jika edge sudah ada (pasangan yang sama dihitung ulang),
      nilai similarity-nya diperbarui.
      """
      #cek apakah edge sudah ada, kalau iya update nilainya
      for i, (other, _) in enumerate(self.edges[doc1]):
         if other == doc2:
            self.edges[doc1][i] = (doc2, similarity)
            for j, (o, _) in enumerate(self.edges[doc2]):
               if o == doc1:
                  self.edges[doc2][j] = (doc1, similarity)
                  break
            return

      #jika belum ada tambah baru
      self.edges[doc1].append((doc2, similarity))
      self.edges[doc2].append((doc1, similarity))

   def get_all_edges(self):
      """Mengembalikan semua edge unik beserta nilai similarity-nya"""
      seen = set()
      result = []
      for doc, edges in self.edges.items():
         for other, sim in edges:
            key = tuple(sorted([doc, other]))
            if key not in seen:
               seen.add(key)
               result.append((doc, other, sim))
      return result

   def get_edges_of(self, doc):
      """Mengembalikan semua edge yang terhubung ke dokumen tertentu"""
      return self.edges.get(doc, [])

   def has_document(self, doc):
      """Memeriksa apakah dokumen sudah ada di graph"""
      return doc in self.document

   #Fungsi unutk menyimpan graph ke file 
   def save_to_file(self, path):
      """
      Menyimpan seluruh isi graph ke file teks.
      Format:
        DOC:nama_dokumen
        EDGE:doc1|doc2|nilai_similarity
      """
      lines = []
      for doc in self.document:
         lines.append(f'DOC:{doc}')
      for doc1, doc2, sim in self.get_all_edges():
         lines.append(f'EDGE:{doc1}|{doc2}|{sim}')

      with open(path, 'w') as f:
         f.write('\n'.join(lines))

   @classmethod
   def load_from_file(cls, path):
      """
      Membaca graph dari file teks dan merekonstruksinya.
      Kalau file belum ada, kembalikan graph kosong.
      Format baris yang dikenali:
        DOC:nama_dokumen
        EDGE:doc1|doc2|nilai_similarity
      """
      graph = cls()
      try:
         with open(path, 'r') as f:
            for line in f:
               line = line.strip()
               if not line:
                  continue

               if line.startswith('DOC:'):
                  nama = line[4:]
                  graph.add_document(nama)

               elif line.startswith('EDGE:'):
                  bagian = line[5:].split('|')
                  if len(bagian) == 3:
                     doc1, doc2, sim_str = bagian
                     graph.add_document(doc1)
                     graph.add_document(doc2)
                     graph.add_edge(doc1, doc2, float(sim_str))

      except FileNotFoundError:
         pass   # file belum ada, mulai dengan graph kosong

      return graph
