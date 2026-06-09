# file untuk membuat struktur data tree
class Node:
   def __init__(self, data, tipe='root'):
      self.data = data
      self.tipe = tipe
      self.children = []

   def add_child(self, child):
      self.children.append(child)


class Tree:
   def __init__(self):
      self.root = Node('ROOT')

   def build_tree(self, teks):
      """Membangun tree hierarki: ROOT → Paragraf → Kalimat → Kata"""
      pisah_paragraf = teks.split('\n')

      for p in pisah_paragraf:
         if p.strip() == '':
            continue

         node_p = Node(p, 'paragraph')
         self.root.add_child(node_p)

         sentences = self.split_sentence(p)

         for s in sentences:
            if s.strip() == '':
               continue
            node_s = Node(s, 'sentence')
            node_p.add_child(node_s)

            words = self.split_word(s)

            for w in words:
               if w.strip():
                  node_w = Node(w, 'word')
                  node_s.add_child(node_w)

   def split_sentence(self, paragraf):
      """Memecah paragraf menjadi beberapa kalimat"""
      kalimat = []
      current = ''

      for char in paragraf:
         current += char
         if char in '.!?':
            kalimat.append(current.strip())
            current = ''

      # Sisa kalimat yang tidak diakhiri tanda baca
      if current.strip():
         kalimat.append(current.strip())

      return kalimat

   def split_word(self, kalimat):
      """Memecah kalimat menjadi beberapa kata"""
      kata = []
      current = ''

      for char in kalimat:
         if char == ' ':
            if current != '':
               kata.append(current.strip())
               current = ''
         else:
            current += char   # BUG FIX: else ini harus di level luar (bukan di dalam if char==' ')

      # Sisa kata yang tidak diakhiri spasi
      if current.strip():
         kata.append(current.strip())

      return kata

   def count_nodes(self, tipe=None):
      """Menghitung jumlah node di tree, bisa difilter berdasarkan tipe"""
      count = 0
      def traverse(node):
         nonlocal count
         if tipe is None or node.tipe == tipe:
            count += 1
         for child in node.children:
            traverse(child)
      for child in self.root.children:
         traverse(child)
      return count
