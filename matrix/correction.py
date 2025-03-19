def detect_neg (M) :
    l , c = len(M), len(M[0])
    i = 0
    j = c
    while i < l and j == c :
        j = 0
    while j < c and M[i][j] >= 0:
        j = j + 1
        i = i + 1
    return j < c

def build_symetric(M) :
    res = []
    for line in M :
        nline = []
        for el in line :
            nline.append(el)
    res.append(nline)
    c = len (M [0])
    for i in range (len ( M) -1 , -1 , -1) :
        nline = []
        for j in range ( c ) :
            nline.append(M[i][j])
        res.append(nline)
    return res
