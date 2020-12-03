import re

PATTERN = re.compile('(?P<min>\\d+)-(?P<max>\\d+) (?P<char>\\w): (?P<password>\\w+)')
