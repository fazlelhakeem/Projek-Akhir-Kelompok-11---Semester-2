class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Circular_Linked_list:
    def __init__(self):
        self.head = None

    #Menambahkan node baru di akhir rantai.
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head #Menunjuk ke diri sendiri
            new_node.prev = self.head #Menunjuk ke diri sendiri
            return
        
        #Menyambungkan pada bagian sebelum head ke paling akhir
        tail = self.head.prev 

        tail.next = new_node #Menambah data baru ke paling akhir
        new_node.prev = tail #Menyambungkan sebelum data baru ke bagian akhir sebelumnya

        new_node.next = self.head #Menghubungkan setelah data baru ke head
        self.head.prev = new_node #Menyambungkan pada bagian sebelum head ke data baru
    
    #Mencari apakah suatu data ada di dalam list.
    def search(self, target):
        curr = self.head

        #Looping sepanajang data
        while curr:
            #kondisi jika data ditemukan
            if curr.data == target:
                return True
            curr = curr.next

            #jika data kembali ke awal
            if curr == self.head:
                break

        return False
    
    #Mengubah struktur Circular Linked List menjadi List biasa bawaan Python ([]).
    def to_list(self):
        result = []
        curr = self.head
        #looping untuk merubah Circular linked list menjadi list
        while curr:
            result.append(curr.data)
            curr = curr.next

            #jika data kembali ke awal
            if curr == self.head:
                break

        return result


