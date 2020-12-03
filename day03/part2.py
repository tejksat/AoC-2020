import slopes

if __name__ == '__main__':
    with open('input.txt', mode='r') as f:
        slope = [line.strip() for line in f.readlines()]

    configurations = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    result = 1

    for configuration in configurations:
        result *= slopes.count_trees(slope, configuration[0], configuration[1])

    print(result)
