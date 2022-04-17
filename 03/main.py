import pprint


def count_bits(input='input.txt'):
    fhand = open(input, "r")
    amt_bits = [
        {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0},
        {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0},
        {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}, {0: 0, 1: 0}
        ]
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
    a = count_bits()
    gamma_binary = find_gamma(a)
    gamma = int(gamma_binary, 2)
    epsilon_binary = find_epsilon(a)
    epsilon = int(epsilon_binary, 2)
    cons = consumption(gamma, epsilon)

    print(f'Gamma: {gamma}, Epsilon: {epsilon}')
    print(f'Consumption: {cons}')


def calculate_lifesupport():
    bits = count_bits()
    pprint.pprint(bits)


calculate_lifesupport()
calculate_energy()
