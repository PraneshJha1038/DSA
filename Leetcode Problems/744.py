letters = ['c', 'f', 'j']
target = 'a'
def largest_after_target(array:list, check:str):
    for element in array:
        if element > check:
            return element
    return array[0]
print(largest_after_target(letters, target))