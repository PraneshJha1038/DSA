from collections import Counter
import collections
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7,8]
for num in b:
    if num in a:
        a.remove(num)
    else:
        print(False)
        break
print(True)