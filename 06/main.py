class LanternGrowth():
    def __init__(self):
        self.live_fish = self.read_input()
        # self.live_fish = [1, 3, 4, 6, 2, 3]

    def read_input(self):
        fhand = open('input.txt', 'r')
        fish_file = fhand.readline().rstrip().split(',')
        fhand.close()
        fish = {str(i): 0 for i in range(9)}
        for i in fish_file:
            fish[str(i)] += 1
        return fish

    def age_fish(self):
        # print(self.live_fish[fish_index])
        fish = {str(i): 0 for i in range(9)}
        for age in self.live_fish:
            if int(age) == 0:
                fish['6'] = self.live_fish['0'] + self.live_fish['7']
                fish['8'] = self.live_fish[age]
            elif int(age) == 7:
                continue
            else:
                fish[str(int(age) - 1)] = self.live_fish[age]
        self.live_fish = fish

    def part_a(self):
        for i in range(256):
            # self.new_day()
            self.age_fish()

    def count_fish(self):
        total = 0
        for fish in self.live_fish.values():
            total += fish
        print(total)


x = LanternGrowth()
print(x.live_fish)
x.part_a()
print(x.live_fish)
x.count_fish()
