#file untuk membuat struktur data tree
class Node:
   def __init__(self, data, tipe = 'root'):
      self.data = data
      self.tipe = tipe
      self.children = []

   def add_child(self, child):
      self.children.append(child)

class Tree:
   def __init__(self):
      self.root = Node('ROOT')

   def build_tree(self, teks):
      #fungsi untuk membuat tree dari teks yang diberikan
      pisah_paragraf = teks.split('\n')

      for p in pisah_paragraf:
         if p == '':
            continue

         node_p = Node(p, 'paragraph')
         self.root.add_child(node_p)

         sentences = self.split_sentence(p)

         for s in sentences:
            node_s = Node(s, 'sentence')
            node_p.add_child(node_s)

            words = self.split_word(s)

            for w in words:
               node_w = Node(w, 'word')
               node_s.add_child(node_w)


   def split_sentence(self, paragraf):
      #fungsi untuk memecah paragraf menjadi beberapa kalimat
      kalimat = []
      current = ''

      for char in paragraf:
         current += char

         if char in '.!?':
            kalimat.append(current.strip())
            current = ''

      #jika ada sisa kalimat namun tidak diakhiri tanda baca ". ! ?"
      if current != '': 
         kalimat.append(current.strip())

      return kalimat

   def split_word(self, kalimat):
      #fungsi untuk memecah kalimat menjadi beberapa kata
      kata = []
      current = ''

      for char in kalimat:
         if char == ' ':
            if current != '':
               kata.append(current.strip())
               current = ''
            else:
               current += char

      #jika ada sisa kata namun tidak diakhiri spasi
      if current != '':
         kata.append(current.strip())

      return kata