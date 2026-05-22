def to_lower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char)+32)
        else:
            result += char
    return result

def remove_punctuation(text):
    Punctuation = ".,!?;:\"'()[]{}<>-/\\|@#$%^&*_+=~`"
    result = ""

    for char in text:
        is_punct = False
        for p in Punctuation:
            if char == p:
                is_punct = True
                break
        
        if not is_punct:
            result += char

    return result
    
def tokenize(text):
    words = []
    current = ""

    for char in text:
        if char == " ":
            if current != "":
                words.append(current)
                current = ""
        
        else:
            current += char

    if current != "":
        words.append(current)

    return words

def remove_stopwords(words):
    stopwords = ["dan", "di", "ke", "yang", "dari"]
    result = []

    for w in words:
        is_stopword = False
        for sw in stopwords:
            if w == sw:
                is_stopword = True

        if not is_stopword:
            result.append(w)

    return result

def preprocess(text):
    text = to_lower(text)
    text = remove_punctuation(text)
    words = tokenize(text)
    words = remove_stopwords(words)
    return words
