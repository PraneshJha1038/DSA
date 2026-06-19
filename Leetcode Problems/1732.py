gain = [-4,-3,-2,-1,4,3,2]
maxHeight = 0
currentHeight = 0
for gainedAltitute in gain:
    currentHeight += gainedAltitute
    maxHeight = max(maxHeight,currentHeight)
print(maxHeight)