digits = [8,9,9]
def sixty_six(array):
    last_digit = len(array)-1
    while array[last_digit] == 9:
        print('.')
        array[last_digit] = 0
        last_digit -= 1
        if last_digit == -1:
            array.insert(0,1)
            return (array)
        print('.')
    array[last_digit] += 1
    print('.')
    return (array)
print(sixty_six(digits))

