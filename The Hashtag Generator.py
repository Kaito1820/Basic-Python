s = str(input())

def generate_hashtag(s):
    lst = []
    lst = list(s.split())
    if not len(lst): 
        return False
    for i in range(len(lst)):
        if len(lst[i][0]) >= 140:
            return False

        lst[i] = lst[i][0].upper() + lst[i][1:].lower()
    
    return '#' + ''.join(lst)
    

print(generate_hashtag(s))