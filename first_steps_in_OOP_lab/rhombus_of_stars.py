size = int(input())


def print_pattern_data(space_data, stars_data):
    print(' ' * space_data + '* ' * stars_data)


def get_pattern_data(*data):
    for x in range(size):
        space_data = size - x - 1
        stars_data = x + 1
        print_pattern_data(space_data, stars_data)

    for x in range(size - 2, -1, -1):
        space_data = size - x - 1
        stars_data = x + 1
        print_pattern_data(space_data, stars_data)


get_pattern_data(size)
