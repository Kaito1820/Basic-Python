def unique_in_order(iterable):
    queue = []
    if len(iterable) != 0:
        n = 0
        queue.append(iterable[0])
        for i in range(1,len(iterable)):
            if queue[n] != iterable[i]:
                queue.append(iterable[i])
                n += 1
    return queue

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1,2,2,3,3]))  