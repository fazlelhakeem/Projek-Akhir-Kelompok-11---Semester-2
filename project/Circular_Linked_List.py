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
            new_node.next = self.head
            new_node.prev = self.head
            return
        
        tail = self.head.prev 

        tail.next = new_node
        new_node.prev = tail

        new_node.next = self.head
        self.head.prev = new_node
    
    #Mencari apakah suatu data (target) ada di dalam list.
    def search(self, target):
        curr = self.head

        while curr:
            if curr.data == target:
                return True
            curr = curr.next

            if curr == self.head:
                break

        return False
    
    #Mengubah struktur Linked List menjadi List biasa bawaan Python ([]).
    def to_list(self):
        result = []
        curr = self.head
        #looping untuk merubah linked list menjadi list
        while curr:
            result.append(curr.data)
            curr = curr.next

            if curr == self.head:
                break

        return result


