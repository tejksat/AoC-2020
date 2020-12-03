def count_trees(slope, right, down):
    x = 0
    y = 0
    count = 0
    while y < len(slope):
        row = slope[y]
        if row[x] == '#':
            count += 1
        x = (x + right) % len(row)
        y += down
    return count
