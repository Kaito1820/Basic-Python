text = str(input())

def alphabet_position(text):
    text = text.lower()
    lst = []
    for i in range(len(text)):    
        if text[i] >= 'a' and text[i] <= 'z':
            temp = ord(text[i]) - 96
            lst.append(str(temp))
            # lst.append(ord(text[i]))
            # pass
    print(" ".join(lst))

alphabet_position(text)
# print(type(ord(text[0])))