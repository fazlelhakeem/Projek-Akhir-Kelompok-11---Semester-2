class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    #Menambahkan node baru di akhir rantai.
    def tambah(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    #Mengubah struktur Linked List menjadi List biasa bawaan Python ([]).
    def to_list(self):
        result = []
        curr = self.head
        #looping untuk merubah linked list menjadi list
        while curr:
            result.append(curr.data)
            curr = curr.next

        return result
