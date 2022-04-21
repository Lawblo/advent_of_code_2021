class LanternGrowth():
    def __init__(self):
        self.live_fish = self.read_input()
        # self.live_fish = [1, 3, 4, 6, 2, 3]

    def read_input(self):
        fhand = open('input.txt', 'r')
        fish = fhand.readline().rstrip().split(',')
        fhand.close()
        fish = [int(x) for x in fish]
        return fish

    def age_fish(self, fish_index):
        # print(self.live_fish[fish_index])
        if self.live_fish[fish_index] == 0:
            self.new_fish()
            self.live_fish[fish_index] = 6
        else:
            self.live_fish[fish_index] -= 1

    def new_fish(self):
        self.live_fish.append(8)

    def new_day(self):
        for fish_index in range(len(self.live_fish)):
            self.age_fish(fish_index)

    def part_a(self):
        for i in range(256):
            self.new_day()
        print(len(self.live_fish))



x = LanternGrowth()
x.part_a()
