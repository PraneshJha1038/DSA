colors = [1,1,1,6,1,1,1]
i = 0
n = len(colors)
j = n-1
difference = float('-inf')
while i < n:
    if colors[i] != colors[n-1]:
        difference = max(n-i-1,difference)
    i += 1
    if colors[j] != colors[0]:
        difference = max(difference,j)
    j -= 1
print(difference)