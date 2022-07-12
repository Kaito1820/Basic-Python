# Given an array of integers, find the one that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for i in range(0,len(seq)):
        if seq.count(seq[i]) % 2:
            return seq[i]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([0,1,0,1,0]))
print(find_it([1,1,2]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it([0]))
print(find_it([10,10,10]))