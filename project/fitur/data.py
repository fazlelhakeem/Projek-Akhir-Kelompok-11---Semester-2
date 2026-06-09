# file untuk menyimpan data / variabel global yang bisa dipakai di semua file
import implementasi.OOP as dd
from implementasi.stack import Stack
from implementasi.graph import Graph

daftar_dokumen  = dd.DaftarDocument.init_daftar_document()
log_menu = Stack()
similarity_graph = Graph.load_from_file('data file.txt')
