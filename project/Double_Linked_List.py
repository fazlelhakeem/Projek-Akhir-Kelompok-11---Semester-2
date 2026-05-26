class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Double_Linked_list:
    def __init__(self):
        self.head = None

    #Menambahkan node baru di akhir rantai.
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        #Menambah data baru ke paling akhir
        curr.next = new_node
        new_node.prev = curr #menghubungkan kembali data baru ke data sebelumnya
    
    #Mencari apakah suatu data (target) ada di dalam list.
    def search(self, target):
        curr = self.head

        while curr:
            #kondisi jika data ditemukan
            if curr.data == target:
                return True #mengembalikan nilai true jika data ditemukan
            curr = curr.next #lanjut ke data selanjutnya

        return False
    
    #Mengubah struktur Double Linked List menjadi List biasa bawaan Python ([]).
    def to_list(self):
        result = []
        curr = self.head
        #looping untuk merubah linked list menjadi list
        while curr:
            result.append(curr.data)
            curr = curr.next

        return result


