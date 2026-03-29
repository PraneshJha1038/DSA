s1:str = "cmpr"
s2:str = "rmcp"
result:bool = True
# def equalString(s1, s2):
#     for i in range(2):
#         if s1[i] != s2[i]:
#             if s2[i+2] == s1[i]:
#                 pass
#             else:
#                 return False
#     return True

def canBeEqual(first:str, second:str) -> bool:
    for i in range(4):
        if s1[i] == s2[i]:
            pass 
        elif s1[i] != s2[(i + 2) % 4]:
            return False
    return True
