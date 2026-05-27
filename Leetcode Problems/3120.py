string = "aAbBcC"
lower = set()
upper = set()
for char in string:
    if char.islower():
        lower.add(char)
    else:
        upper.add(char.lower())
print(len(lower & upper))