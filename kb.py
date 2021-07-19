#kb

#input : apple,banana,grape,apple,banana
#output : apple 2 banana 2

#input : apple,banana,grape,strawberry,peach
#output : Complete

from collections import Counter


fruits = list(map(str,input('').split(',')))

counter = Counter(fruits)

chk = 0
for i in counter:
    if counter[i] != 1:
        chk += 1
        break

if chk == 0:
    print('Complete')
else:
    for i in counter:
        print(i,counter[i],end=' ')

