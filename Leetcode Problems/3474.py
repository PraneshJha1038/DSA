first:str = "TFTF"
second:str = "ab"

def lexo(str1, str2):
    n = len(str1)
    m = len(str2)
    word = ["a"] * (n + m - 1) 
    fixed = [False] * (n + m - 1)
    for i in range(len(str1)):
        if str1[i] == "T":
            j = i
            while j <= i + m - 1:
                if not fixed[j]:
                    word[j] = str2[j%m]
                    fixed[j] = True
                if fixed[j] and str2[j%m] != word[j]:
                    return ""
                j += 1
        elif str1[i] == "F":
            j = i
            isEqual = True
            while j <= i + m - 1:
                if word[j] != str2[j%m]:
                    isEqual = False
                    break
            if isEqual:
                return ""
        return "".join(word)

print(lexo(first, second))
