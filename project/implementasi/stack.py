#file untuk membuat struktur data stack
class Stack:
   def __init__(self):
      self.data = []

   def is_empty(self):
      return len(self.data) == 0

   def tambah(self, tambah):
      self.data.append(tambah)

   def hapus(self):
      if self.is_empty():
         return None
      return self.data.pop()

   def peek(self):
      if self.is_empty():
         return None
      return self.data[-1]

