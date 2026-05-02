n = 25
t = 0
original = n
while n > 0:
    t = t * 10 + (n % 10)
    n //= 10
print(abs(original - t))