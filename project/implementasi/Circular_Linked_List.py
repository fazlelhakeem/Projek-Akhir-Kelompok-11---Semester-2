#File untuk mengimplementasikan struktur data Circular Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Circular_Linked_list:
    def __init__(self):
        self.head = None

    #Fungsi untuk menambahkan node baru di akhir
    def tambah(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head 
            new_node.prev = self.head 
            return
        
        #menyambungkan pada bagian sebelum head ke paling akhir
        tail = self.head.prev 

        tail.next = new_node #menambah data baru setelah tail
        new_node.prev = tail #menyambungkan prev data baru ke tail

        new_node.next = self.head #menghubungkan next data baru ke head
        self.head.prev = new_node #Menyambungkan pada prev head ke data baru
        self.head = new_node #mengubah data baru menjadi head
    
    #Fungsi untuk mencari suatu data di dalam linked list berdasarkan nomor
    def search(self, target, len_data):
        curr = self.head

        if len_data == 0:
            return False

        #Looping sepanajang data
        for i in range(len_data):
            #kondisi jika data ditemukan
            if i+1 == target:
                return curr.data
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

    def hapus(self, target):
        curr = self.head

        while curr:
            if curr.data == target:
                #Jika node yang dihapus adalah head
                if curr == self.head:
                    #Jika hanya ada satu node
                    if curr.next == self.head:
                        self.head = None
                    else:
                        tail = self.head.prev
                        self.head = self.head.next
                        tail.next = self.head
                        self.head.prev = tail
                else:
                    prev_node = curr.prev
                    next_node = curr.next
                    prev_node.next = next_node
                    next_node.prev = prev_node

                return True

            curr = curr.next

            #jika data kembali ke awal
            if curr == self.head:
                break

        return False
