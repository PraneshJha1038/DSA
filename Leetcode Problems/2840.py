s1:str = "bea"
s2:str = "abe"

def hashString(iterable: str):
    mp = {}
    for i in range(len(iterable)):
        if iterable[i] not in mp:
            mp[iterable[i]] = [i]
        else:
            mp[iterable[i]].append(i)
    return mp

def canBeEqual(s1, s2):
    mp = hashString(s2)
    used = set()

    for i in range(len(s1)):
        found = False

        if s1[i] not in mp:
            return(False)

        for j in mp[s1[i]]:
            if j not in used and (j - i) % 2 == 0:
                used.add(j)
                found = True
                break

        if not found:
            return False
    return True

print(canBeEqual(s1, s2))
