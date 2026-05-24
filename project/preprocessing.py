def to_lower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char)+32)
        else:
            result += char
    return result

def hapus_simbol(text):
    simbol = ".,!?;:\"'()[]{}<>-/\\|@#$%^&*_+=~`"
    result = ""

    #Looping untuk setiap char apakah ada simbol atau tidak
    for char in text:
        is_punct = False
        for p in simbol:
            if char == p:
                is_punct = True
                break
        
        #mengembalikan char jika tidak ada simbol
        if not is_punct:
            result += char

    return result
    
#Memisahkan antar kata
def tokenize(text):
    words = []
    current = ""

    #Looping untuk setiap char yang ada di text
    for char in text:
        #jika sudah di akhir kata yang ditandai spasi
        if char == " ":
            #menambahkan kata yang disimpan sementara ke words
            if current != "":
                words.append(current)
                current = ""

        #menambahkan char sementara ke current jika belum akhir kata
        else:
            current += char

    # menambahkan isi current ke words jika kalimat sudah habis dan tidak ada spasi
    if current != "":
        words.append(current)

    return words

#hapus stopwords
def hapus_stopwords(words):
    stopwords = ["dan", "di", "ke", "yang", "dari"]
    result = []

    #Looping untuk mencari stepword yang ada pada words
    for kata in words:
        is_stopword = False
        for sw in stopwords:
            if kata == sw:
                is_stopword = True

        if not is_stopword:
            result.append(kata)

    return result

def preprocess(text):
    text = to_lower(text)
    text = hapus_simbol(text)
    words = tokenize(text)
    words = hapus_stopwords(words)
    return words
