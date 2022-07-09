# n = int(input())
# arr = input()


def move_zeros(array):
    zero = []
    num = []
    if len(array) == 0:
        return array
    for i in range(len(array)):
        if array[i] != 0:
            num.append(array[i])
        else:
            zero.append(array[i])

    return num + zero

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))