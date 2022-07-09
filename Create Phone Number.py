lst = []
for i in range(10):
    lst.append(int(input()))

#Solve 1
def create_phone_number(n):
    s = ""
    for i in range(10):
        s = s + str(n[i])
    return '(' + s[0:3] + ') ' + s[3:6] + '-' + s[6:] 

'''
#Solve 2
def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])
  return '({}) {}-{}'.format(str1, str2, str3)
'''

'''
Solve 3
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
'''
'''
#Solve 4
def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
'''

print(create_phone_number(lst))
