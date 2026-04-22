# words within two edits of dictionary
queries = ["word", "wood", "ants", "note"]
n = len(queries[0])
dictionary = ['wood', 'joke', 'moat']
final = list()
for query in queries:
    for word in dictionary:
        mismatch = 0
        for i in range(n):
            if query[i] != word[i]:
                mismatch += 1
            if mismatch > 2 :
                break
        if mismatch <= 2:
            final.append(query)
            break
print(final)