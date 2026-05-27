def baca_file(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text

def ubah_isi_file(path,isi):
    file = open(path, 'w')
    file.write(isi)
    file.close()

def tambah_file(path,isi):
    file = open(path, 'a')
    file.write(isi)
    file.close()

def kosongkan_isi(path):
    file = open(path, 'w')
    file.write("")
    file.close()