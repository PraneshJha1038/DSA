moves = "L_RL__R"
countL = 0
countR = 0
for chr in moves:
    if chr == 'L':
        countL += 1
    elif chr == 'R':
        countR += 1
countEm = len(moves) - countL - countR
result = 0
if countL >= countR:
    result = abs(countL + countEm - countR)
else:
    result =  abs(countR + countEm - countL)
print(result)