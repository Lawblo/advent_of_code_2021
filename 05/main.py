class Day5():

    def __init__(self):
        self.coords = self.import_input()
        self.sub_map = self.create_map()

    def import_input(self):
        fhand = open('input.txt', 'r')
        inp = fhand.read()
        fhand.close()

        inp = inp.split('\n')
        store = []
        coords = [i.split(' -> ') for i in inp if len(i) > 1]
        for line in coords:
            x1, y1 = (line[0].split(','))
            x2, y2 = (line[1].split(','))
            store.append({
                'x1': int(x1),
                'y1': int(y1),
                'x2': int(x2),
                'y2': int(y2)
                })

        return store

    def create_map(self):
        sub_map = [[0]*1000 for i in range(1000)]
        return sub_map

    def fill_map(self):
        for coord in self.coords:
            # sub_map = self.create_map()
            sub_map = self.sub_map
            if self.check_coord_a(coord):
                self.draw_map_a(
                    coord['x1'],
                    coord['y1'],
                    coord['x2'],
                    coord['y2'],
                    sub_map
                    )
            elif self.check_coord_b(coord):
                self.draw_map_b(
                    coord['x1'],
                    coord['y1'],
                    coord['x2'],
                    coord['y2'],
                    sub_map
                    )
            else:
                continue

            # print('_________________')
            # print(coord)
            # print('')
            # self.display_map(sub_map)
            # print('_________________')

    def display_map(self, show_map):
        for i in show_map:
            print(''.join([str(j) if j != 0 else '.' for j in i]))

    def check_coord_a(self, coord):
        if (coord['x1'] == coord['x2']) or (coord['y1'] == coord['y2']):
            return True

    def check_coord_b(self, coord):
        x1, x2, y1, y2 = coord['x1'], coord['x2'], coord['y1'], coord['y2']
        x_change = x1 - x2
        y_change = y1 - y2
        if x_change == y_change or x_change == y_change * -1:
            return True

    def draw_map_a(self, x1, y1, x2, y2, sub_map):
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                sub_map[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                sub_map[y1][j] += 1
        else:
            return

    def draw_map_b(self, x1, y1, x2, y2, sub_map):
        x_list = [i for i in range(x1, (x2 + 1 if x1 < x2 else x2 - 1),
                                       (-1 if x1 > x2 else 1))]
        y_list = [j for j in range(y1, (y2 + 1 if y1 < y2 else y2 - 1),
                                       (-1 if y1 > y2 else 1))]
        for x, y in zip(x_list, y_list):
            sub_map[y][x] += 1

    def two_plus(self):
        total = 0
        for x, line in enumerate(self.sub_map):
            for y, coord in enumerate(line):
                if coord > 1:
                    # print(x, y)
                    total += 1
        return total


part_a = Day5()
part_a.fill_map()
print(part_a.two_plus())



