
def read_file():
    DATA_FILE = "day8_test.txt"
    DATA_FILE = "day8.txt"
    
    with open(DATA_FILE) as file:
        return [line.strip() for line in file.readlines()]
    
def find_frequencies(input_grid):
    frequency_locations = dict()
    
    for i, row in enumerate(input_grid):
        for j, c in enumerate(row):
            if c != ".":
                frequency_locations[c] = frequency_locations.get(c, []) + [(i, j)]
              
    return frequency_locations

def calculate_antinode_location(antenna_one_location, antenna_two_location):
    location_diff_x = antenna_one_location[0] - antenna_two_location[0]
    location_diff_y = antenna_one_location[1] - antenna_two_location[1]

    antinode_one_x, antinode_one_y = antenna_one_location[0] + location_diff_x, antenna_one_location[1] + location_diff_y
    antinode_two_x, antinode_two_y = antenna_two_location[0] - location_diff_x, antenna_two_location[1] - location_diff_y
    
    return (antinode_one_x, antinode_one_y), (antinode_two_x, antinode_two_y)

def find_antinodes(frequency_locations: dict):
    unique_antinode_locations = set()

    for frequency in frequency_locations.keys():
        for i, frequency_location_one in enumerate(frequency_locations[frequency]):
            
            for j, frequency_location_two in enumerate(frequency_locations[frequency][i:]):
                if frequency_location_one == frequency_location_two:
                    continue
                antinode_one, antinode_two = calculate_antinode_location(frequency_location_one, frequency_location_two)
                
                if antinode_one[0] < NUMBER_OF_ROWS and antinode_one[1] < NUMBER_OF_COLS \
                   and antinode_one[0] >= 0 and antinode_one[1] >= 0:
                    unique_antinode_locations.add(antinode_one)
                if antinode_two[0] < NUMBER_OF_ROWS and antinode_two[1] < NUMBER_OF_COLS\
                   and antinode_two[0] >= 0 and antinode_two[1] >= 0:
                    unique_antinode_locations.add(antinode_two)

    return unique_antinode_locations

data_grid = read_file()

NUMBER_OF_ROWS, NUMBER_OF_COLS = len(data_grid), len(data_grid[0])

frequency_locations = find_frequencies(data_grid)

antinode_locations = find_antinodes(frequency_locations)

print(antinode_locations)
print("Part 1:", len(antinode_locations))
#for i in range(NUMBER_OF_ROWS):
#    print(["#" if (i,j) in antinode_locations else "." for j in range(NUMBER_OF_COLS)])
