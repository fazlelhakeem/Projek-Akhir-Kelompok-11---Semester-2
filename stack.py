#file untuk membuat struktur data stack
class Stack:
   def __init__(self):
      self.data = []

   def is_empty(self):
      return len(self.data) == 0

   def push(self, tambah):
      self.data.append(tambah)

   def pop(self):
      if self.is_empty():
         return None
      return self.data.pop()

   def peek(self):
      if self.is_empty():
         return None
      return self.data[-1]

   def length(self):
      return len(self.data)