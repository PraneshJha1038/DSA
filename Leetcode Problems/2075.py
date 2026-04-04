encodedText = "iveo    eed   l te   olc"
rows = 4

if rows == 1:
    print(encodedText)

n = len(encodedText)
cols = n // rows
res = []

for c in range(cols):
    r, j = 0, c
    while r < rows and j < cols:
        res.append(encodedText[r * cols + j])
        r += 1
        j += 1

print("".join(res).rstrip())