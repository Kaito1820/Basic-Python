def maxSequence(arr):
    best = -99999
    sum = 0
    countNegative = 0
    if len(arr) == 0:
        return 0
    

    for i in arr:
        if i < 0:
            countNegative += 1
    
    if countNegative == len(arr):
        return 0
    
    for i in range(0, len(arr)):
        sum = max(arr[i], sum + arr[i])
        best = max(best,sum)

    return best

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))