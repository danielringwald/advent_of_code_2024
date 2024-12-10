
def read_file():
    DATA_FILE = "day10_test.txt"
    DATA_FILE = "day10.txt"
    
    with open(DATA_FILE) as file:
        return [line.strip() for line in file.readlines()]
    
def is_inside_grid(x, y):
    return x >= 0 and x < NUMBER_OF_ROWS and y >= 0 and y < NUMBER_OF_COLS

def find_trailheads(topographical_map: list):
    trailheads = []
    for i, row in enumerate(topographical_map):
        for j, c in enumerate(row):
            if c == "0":
                trailheads.append((i,j,c))

    return trailheads

def find_nearest_paths(location: tuple, topographical_map: list):
    location_x, location_y, height = location

    valid_paths = []

    for x_diff in range(-1, 2):
        new_x = location_x + x_diff
        if not is_inside_grid(new_x, location_y):
            continue

        new_height = int(topographical_map[new_x][location_y])

        if new_height == int(height) + 1:
            valid_paths.append((new_x, location_y, new_height))
    for y_diff in range(-1, 2):
        new_y = location_y + y_diff
        if not is_inside_grid(location_x, new_y):
            continue

        new_height = int(topographical_map[location_x][new_y])

        if new_height == int(height) + 1:
            valid_paths.append((location_x, new_y, new_height))

    return valid_paths    

input_file = read_file()

NUMBER_OF_ROWS, NUMBER_OF_COLS = len(input_file), len(input_file[0])

trailheads = find_trailheads(input_file)

part_one = 0
part_two = 0
for trailhead in trailheads:
    current_paths = [trailhead]
    for i in range(9):
        temp_paths = []
        for path in current_paths:
            temp_paths += find_nearest_paths(path, input_file)
        current_paths = temp_paths
    
    part_one += len(set(current_paths))
    part_two += len(current_paths)

print("Part 1:", part_one)
print("Part 2:", part_two)
