#file untuk membuat struktur data queue
class Queue:
   def __init__(self):
      self.data = []

   def is_empty(self):
      return len(self.data) == 0

   def enqueue(self, tambah):
      self.data.append(tambah)

   def dequeue(self):
      if self.is_empty():
         return None
      return self.data.pop(0)

   def peek(self):
      if self.is_empty():
         return None
      return self.data[0]

   def length(self):
      return len(self.data)