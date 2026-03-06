stri = '1'
def check_String(string):
    if len(string) == 0:
        return(False)
    for i in range(len(string)-1,-1,-1):
        if string[i] == '1':
            continue
        elif string[i] == '2':
            return(int(string[0:i+1]))
    return("")
print(check_String(stri))