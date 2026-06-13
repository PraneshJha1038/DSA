words = ["abcd","def","xyz"]
result = "" 
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
for word in words:
    sum = 0
    for char in str(word):
        sum += weights[ord(char)-97]
    result = result + f"{chr(122-(sum % 26))}"
print(result)