class CrabAdventure():

    def __init__(self):
        self.crab_positions = self.read_input()

    def read_input(self):
        fhand = open('input.txt', 'r')
        inp = fhand.readline().rstrip().split(',')
        inp = [int(i) for i in inp]
        return inp

    def find_min_distance(self):
        min_fuel = None
        for i in range(max(self.crab_positions)):
            total = 0
            for crab in self.crab_positions:
                crab_steps = max(crab, i) - min(crab, i)
                crab_move = 0
                move_cost = 1
                for step in range(crab_steps):
                    crab_move += move_cost
                    move_cost += 1
                total += crab_move

            if not min_fuel:
                min_fuel = total
                continue
            min_fuel = total if total < min_fuel else min_fuel
        print(min_fuel)





a = CrabAdventure()
a.find_min_distance()