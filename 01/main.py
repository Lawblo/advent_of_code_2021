# ownerproof-2130897-1648670716-ca47c9f8c616

def amt_increases(prev, next_val):
    if prev and next_val > prev:
        return True
    return False


def part_one():
    fhand = open('input.txt')
    prev = None
    increases = 0
    for line in fhand:
        line = int(line.rstrip())

        if amt_increases(prev, line):
            increases += 1

        prev = line
    print(increases)


def three_measures():
    fhand = open('input.txt')

    prev = None
    increases = 0
    values = []
    next_val = None
    for line in fhand:
        line = int(line.rstrip())

        if len(values) < 3:
            values.append(line)
            continue

        next_val = sum(values)
        print(next_val)

        if amt_increases(prev, next_val):
            increases += 1

        prev = next_val
        values.pop(0)
        values.append(line)

    next_val = sum(values)

    if amt_increases(prev, next_val):
        increases += 1
    return increases


print(three_measures())

