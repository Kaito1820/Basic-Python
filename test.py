n = str(input())

def spin_words(sentence):
    lst = []
    lst = list(sentence.split(" "))
    k = 0
    for i in lst:
        if(len(i) >= 5):
            s = ""
            for j in range(len(i)):
                s = i[j] + s
            lst[k] = s
        k += 1
    return " ".join(lst)

print(spin_words(n))