combinations = [[1,3,1],[3,1,1],[2,1,3],[1,3,2],[3,1,2],[2,1,2],[1,2,1],[3,2,1],[2,3,1],[1,2,3],[3,2,3],[2,3,2]]
output = 0
n = 0
while n!= 5000:
    for b in range(0,12):
        counter = 0
        taken = combinations.pop(b)

        for i in range(0,len(combinations)):
            for j in range(0,3):
                if (combinations[i])[j] == taken[j]:
                    break
                elif j == 2:
                    counter +=1
        combinations.insert(b,taken)
        output += counter
    print(output)
    n+=1
"""Wasnt' able to do"""