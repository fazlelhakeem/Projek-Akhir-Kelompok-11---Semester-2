#file untuk membuat struktur data graph
class Graph:
   def __init__(self):
      self.document = []
      self.edges = {}

   def add_document(self, doc):
      if doc not in self.document:
         self.document.append(doc)
         self.edges[doc] = []

   def add_edge(self, doc1, doc2, similarity):
      self.edges[doc2].append((doc1, similarity))
      self.edges[doc1].append((doc2, similarity))