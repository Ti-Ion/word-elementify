elements = ""


# Given a lowercase string and a list of element symbols returns all possible elemental compositions
def recursive_decompose(w,e):
    if len(w) == 0:
        return []
    if len(w) == 1:
        if w in e:
            return [w.upper()]
        else:
            return []
    if len(w) == 2:
        ret = []
        if w[0] in e and w[1] in e:
            ret.append(w[0].upper()+w[1].upper())
        if w in e:
            ret.append(w[0].upper()+w[1])
        return ret

    res = []

    if w[0] in e:
        poss1 = recursive_decompose(w[1:], e)
        for f in poss1:
            res.append(w[0].upper()+f)
    if w[0:2] in e:
        poss2 = recursive_decompose(w[2:], e)
        #print(poss2)
        for f in poss2:
            res.append(w[0].upper()+w[1]+f)
    return res


# Reads a text file for element symbols and asks for a word to be input before running recursive_decompose
if __name__ == '__main__':
    with open('element_symbols.txt') as f:
        elements = f.read().lower().splitlines()
    word = input("Type a word\n")
    result = recursive_decompose(word,elements)
    print(result)
    print("end")
