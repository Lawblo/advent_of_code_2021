class Submarine:
    def __init__(self):
        self.horizontal_pos = 0
        self.depth = 0
        self.aim = 0

    def forward(self, amt):
        self.horizontal_pos += amt
        self.depth += self.aim * amt
        print(f'Moved forward {amt}')
        print(self.pos())

    def up(self, amt):
        self.aim -= amt
        print(f'Aimed up {amt}')
        print(self.pos())

    def down(self, amt):
        self.aim += amt
        print(f'Aimed down {amt}')
        print(self.pos())

    def position(self):
        return self.horizontal_pos * self.depth

    def pos(self):
        return (f'Horizontal pos: {self.horizontal_pos}\nDepth: {self.depth}\n\
Aim: {self.aim}\n')

    def pilot_sub(self):
        fhand = open('input.txt', 'r')
        for line in fhand:
            line = line.rstrip().split()
            command = line[0]
            amount = int(line[1])

            if command == 'forward':
                self.forward(amount)
            elif command == 'up':
                self.up(amount)
            elif command == 'down':
                self.down(amount)
        fhand.close()


a = Submarine()
a.pilot_sub()
# a.forward(5)
# a.down(5)
# a.forward(8)
# a.up(3)
# a.down(8)
# a.forward(2)
# print(a.horizontal_pos)
# print(a.depth)
print(a.position())
