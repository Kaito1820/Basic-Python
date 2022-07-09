text = input()

def pig_it(text):
    text = text.split()
    for i in range(len(text)):
        if len(text[i]) >= 2:
            temp = text[i][1:] + text[i][0] + "ay"
            text[i] = temp
        elif text[i] >= 'a' and text[i] <= 'z' or text[i] >= 'A' and text[i] <= 'Z':
            print(" ".join(text))

pig_it(text)