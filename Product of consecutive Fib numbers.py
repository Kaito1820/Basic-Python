n = int(input())

#sovle 1
def productFib(prod):
    fi = []
    fi.append(0)
    fi.append(1)

    ans = 0;
    if fi[0] * fi[1] == prod:
        return [fi[0], fi[1], True]
    
    for i in range(2,200):
        fi.append(fi[i-2] + fi[i-1])
        if fi[i-1] * fi[i] == prod:
            return [fi[i-1], fi[i], True]
        elif fi[i-1] * fi[i] > prod:
            return [fi[i-1], fi[i], False]

'''
#solve 2
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
'''

print(productFib(n))