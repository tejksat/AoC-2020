def find_sum(lines, sum_to_find):
    i = 0
    j = len(lines) - 1
    while i < j:
        s = lines[i] + lines[j]
        if s == sum_to_find:
            return lines[i], lines[j]
        elif s < sum_to_find:
            i += 1
        else:
            j -= 1
    return None


if __name__ == '__main__':
    with open('input.txt', mode='r') as file:
        numbers = [int(x) for x in file.readlines()]

    numbers.sort()

    for i in range(len(numbers)):
        result = find_sum(numbers, 2020 - numbers[i])
        if result is not None:
            print(numbers[i] * result[0] * result[1])
            break
