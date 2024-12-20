def second_stone(first_stone):
    numbers = []
    for i in range(1, 11):
        for j in range(i+1, 21):
            if first_stone < (i + j):
                break
            else:
                if first_stone % (i + j) == 0:
                    numbers.extend([i, j])
    return(numbers)

s = second_stone(int(input('Введите число на первом камне:\n')))
print(*s)