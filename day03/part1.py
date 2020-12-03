import slopes

if __name__ == '__main__':
    with open('input.txt', mode='r') as f:
        slope = [line.strip() for line in f.readlines()]

    print(slopes.count_trees(slope, right=3, down=1))
