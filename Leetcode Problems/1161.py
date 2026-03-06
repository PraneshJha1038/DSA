root = [989,None,10250,98693,-89388,None,None,None,-32127]
i = 0
j = i + 1
n = 0
total = 0
while j < len(root):
    curr = 0
    zero = 0
    for k in range(i,j):
        if root[k] == int and root[k] != 0:
            curr += root[k]
        if root[k] == 0 or root[k] == None:
            zero += 1
    if curr > total:
            total = 0
            total = curr
            n += 1
    temp = j
    j = 2*j + 1 - 2*zero
    i = temp
    if j > len(root):
         j = j - len(root)
print(n)
