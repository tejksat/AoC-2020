import re

from common import PATTERN


def is_valid_password(line):
    m = re.search(PATTERN, line)
    min = int(m.group('min'))
    max = int(m.group('max'))
    char = m.group('char')
    password = m.group('password')
    return (password[min - 1] == char) != (password[max - 1] == char)


if __name__ == '__main__':
    valid = 0
    with open('input.txt', mode='r') as f:
        for line in f:
            if is_valid_password(line):
                valid += 1
    print(valid)
