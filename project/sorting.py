#urut sesuai paling banyak muncul
def sort_by_frekuensi(items):
    items = list(items)

    n = len(items)
    #menggunakan Algoritma Bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]: #membandingkan banyak kemunculan
                items[j] , items[j + 1] = items[j + 1] ,items[j]

    return items

#urut sesuai huruf
def sort_by_huruf(items):
    items = list(items)

    n = len(items)
    #menggunakan Algoritma Bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][0] < items[j + 1][0]:#membandingkan kata / key
                items[j] , items[j + 1] = items[j + 1] ,items[j]

    return items