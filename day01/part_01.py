if __name__ == '__main__':
    with open('input.txt', mode='r') as file:
        numbers = [int(x) for x in file.readlines()]

    numbers.sort()

    i = 0
    j = len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == 2020:
            print(numbers[i] * numbers[j])
            i += 1
            j -= 1
        elif s < 2020:
            i += 1
        else:
            j -= 1
