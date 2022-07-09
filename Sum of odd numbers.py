n = int(input())

def row_sum_odd_numbers(n):
    start_num = 0
    sum = 0
    for i in range(0,n):
        if start_num <= 1:
            start_num += 1
        else:
            start_num += i
                
    for i in range(start_num, start_num+n):
        sum += 2*i-1
    
    return sum

print(row_sum_odd_numbers(n))

