#File untuk fungsi preprocessing (sebelum menghitung similarity)
import implementasi.Single_Linked_List as sll
import implementasi.Double_Linked_List as dll
import implementasi.Circular_Linked_List as cll

#Fungs untuk mengubah semua huruf menjadi huruf kecil
def to_lower(teks):
    current = teks

    if current is None:
        return
    elif "A" <= current.data <= "Z":
        current.data = current.data.lower()
        to_lower(current.next)
    else:
        to_lower(current.next)

#Fungsi untuk menghapus simbol-simbol yang tidak diperlukan
def hapus_simbol(teks):
    simbol = ".,!?;:\"'()[]{}<>-/\\|@#$%^&*_+=~`"

    for i in simbol:
        while teks.search(i):
            teks.hapus(i)

#Fungsi untuk memisahkan antar kata
def tokenize(teks):
    hasil = []
    temp = ""

    #Looping untuk setiap char yang ada di teks
    for char in teks:
        if char == " " or char == "":
            #menambahkan kata yang disimpan sementara ke hasil
            if temp != "":
                hasil.append(temp)
                temp = ""

        #menambahkan char sementara ke temp jika belum akhir kata
        else:
            temp += char

    #menambahkan isi temp ke hasil jika kalimat sudah habis dan tidak ada spasi
    if temp != "":
        hasil.append(temp)

    return hasil

#Fungsi untuk menghapus stopwords
def hapus_stopwords(teks):
    stopwords = ["dan", "di", "ke", "yang", "dari"]
    hasil = []

    #Looping untuk mencari stopword yang ada di teks
    for kata in teks:
        is_stopword = False
        for sw in stopwords:
            if kata == sw:
                is_stopword = True

        if not is_stopword:
            hasil.append(kata)

    return hasil

#Fungsi preprocess (digunakan sebelum menghitung similarity)
def preprocess(teks):
    #mengubah teks menjadi single linked list
    teks_sll = sll.Linked_list()
    for char in teks:
        teks_sll.tambah(char)

    to_lower(teks_sll.head)
    teks_char = teks_sll.to_list() #mengubah single linked list menjadi list biasa

    teks_dll = dll.Double_Linked_list()
    for i in teks_char:
        teks_dll.tambah(i)

    hapus_simbol(teks_dll)
    teks_char = teks_dll.to_list() #mengubah double linked list menjadi list biasa

    teks_lst = tokenize(teks_char)
    teks_akhir = hapus_stopwords(teks_lst)
    
    return teks_akhir
