elements = ""

def recursive_decompose(w,e,r):
    return_list = []



if __name__ == '__main__':

    with open('element_symbols.txt') as f:
        elements = f.read().splitlines()
    word = input("Type a word\n")
    recursive_decompose(word,elements, [])
    print("end")
