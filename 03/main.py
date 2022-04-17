from re import I


def count_bits(input='input.txt'):
    fhand = open(input, "r")
    # amt_bits = [
    #     {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0},
    #     {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0},
    #     {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}
    #     ]
    amt_bits = [{0: 0, 1: 0} for i in range(12)]
    for line in fhand:
        line = line.rstrip()
        counter = 0
        for bit in line:
            amt_bits[counter][int(bit)] += 1
            counter += 1

    return amt_bits


def find_gamma(amt_bits):
    gamma = []
    for bit in amt_bits:
        if bit[0] > bit[1]:
            gamma.append('0')
        else:
            gamma.append('1')
    return ''.join(gamma)


def find_epsilon(amt_bits):
    epsilon = []
    for bit in amt_bits:
        if bit[0] < bit[1]:
            epsilon.append('0')
        else:
            epsilon.append('1')
    return ''.join(epsilon)


def consumption(gamma, epsilon):
    return gamma * epsilon


def calculate_energy():
    bits = count_bits()
    gamma_binary = find_gamma(bits)
    gamma = int(gamma_binary, 2)
    epsilon_binary = find_epsilon(bits)
    epsilon = int(epsilon_binary, 2)
    cons = consumption(gamma, epsilon)

    print(f'Gamma: {gamma}, Epsilon: {epsilon}')
    print(f'Consumption: {cons}')

# PART 2


def input_to_list():
    fhand = open('input.txt', 'r')
    to_list = [line.rstrip() for line in fhand]
    fhand.close()
    return to_list


def find_most(items, index):
    bits = {0: 0, 1: 0}
    for number in items:
        bits[int(number[index])] += 1

    return 1 if bits[1] >= bits[0] else 0


def find_least(items, index):
    bits = {0: 0, 1: 0}
    for number in items:
        bits[int(number[index])] += 1

    return 0 if bits[0] <= bits[1] else 1


def find_oxygen(report, index):
    most = str(find_most(report, index))
    keep = [x for x in report if x[index] == most]
    return keep


def find_co2(report, index):
    least = str(find_least(report, index))
    keep = [x for x in report if x[index] == least]
    return keep


def calculate_lifesupport():
    report = input_to_list()
    counter = 0
    while len(report) > 1:

        report = find_oxygen(report, counter)
        counter += 1

    oxygen = int(report[0], 2)

    report = input_to_list()
    counter = 0
    while len(report) > 1:

        report = find_co2(report, counter)
        counter += 1

    co2 = int(report[0], 2)

    print(oxygen * co2)



calculate_lifesupport()
# calculate_energy()
