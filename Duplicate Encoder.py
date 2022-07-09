word = input()

def duplicate_encode(word):
    lst = []
    word = word.lower()
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            lst.append(')')
        else:
            lst.append('(')
    return ''.join(lst)

print(duplicate_encode(word))