s1:str = "abcd"
s2:str = "cdab"
result:bool = True
def equalString(s1, s2):
    for i in range(2):
        if s1[i] != s2[i]:
            if s2[i+2] == s1[i]:
                pass
            else:
                return False
    return True

print(equalString(s1, s2))