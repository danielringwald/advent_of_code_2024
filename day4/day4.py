import re

DATA_FILE = "day4_test.txt"
DATA_FILE = "day4.txt"

data_matrix = []
with open(DATA_FILE, 'r', encoding="utf8") as file:
    for line in file:
        data_matrix += [list(line.strip())]

RESULT_STRING = ""

NUMBER_OR_ROWS = len(data_matrix)
NUMBER_OF_COLS = len(data_matrix[0])

# Horizontal
for row in data_matrix:
    r = ""
    for letter in row:
        r += letter

    RESULT_STRING += r
    RESULT_STRING += ","
    RESULT_STRING += r[::-1]
    RESULT_STRING += ","

# Vertical
for c_i in range(NUMBER_OF_COLS):
    column = ""
    for r_i, value in enumerate(data_matrix):
        column += value[c_i]

    reversed_column = column[::-1]
    
    RESULT_STRING += column
    RESULT_STRING += ","
    
    RESULT_STRING += reversed_column
    RESULT_STRING += ","

def find_diagonal(result_string, d_m):

    # Diagonal
    for c_i in range(NUMBER_OF_COLS):
        diagonal_string = ""
        for r_i in range(NUMBER_OR_ROWS - c_i):
            diagonal_string += d_m[r_i][c_i + r_i]

        result_string += diagonal_string
        result_string += ","
        result_string += diagonal_string[::-1]
        result_string += ","

    for r_i in range(1, NUMBER_OR_ROWS):
        diagonal_string = ""
        for c_i in range(NUMBER_OF_COLS - r_i):
            diagonal_string += d_m[r_i + c_i][c_i]

        result_string += diagonal_string
        result_string += ","
        result_string += diagonal_string[::-1]
        result_string += ","

    return result_string

def find_diagonal_with_index(d_m, reverse=False):
    #diagonal_list = []
    middle_indices = []
    perturb = 1

    # Diagonal
    for c_i in range(NUMBER_OF_COLS):
        diagonal_string = ""
        for r_i in range(NUMBER_OR_ROWS - c_i):
            diagonal_string += d_m[r_i][c_i + r_i]

        regex = re.finditer("(?=SAM|MAS)", diagonal_string)
        
        for r in regex:
            col_number = c_i + r.start() + perturb
            mapped_col = col_number if not reverse else NUMBER_OF_COLS - col_number -1
            middle_indices += [(r.start() + perturb, mapped_col)]
           
    for r_i in range(1, NUMBER_OR_ROWS):
        diagonal_string = ""
        for c_i in range(NUMBER_OF_COLS - r_i):
            diagonal_string += d_m[r_i + c_i][c_i]

        regex = re.finditer("(?=SAM|MAS)", diagonal_string)

        print(diagonal_string)
        for r in regex:
            col_number = r.start() + perturb
            mapped_col = col_number if not reverse else NUMBER_OF_COLS - col_number - 1
            middle_indices += [(r_i + r.start() + perturb, mapped_col)]
            print(middle_indices[-1])

    return middle_indices

RESULT_STRING = find_diagonal(RESULT_STRING, data_matrix)
reversed_data_matrix = [row[::-1] for row in data_matrix]
RESULT_STRING = find_diagonal(RESULT_STRING, reversed_data_matrix)

#for row in data_matrix:
#    print(row)
#print(RESULT_STRING)
#
print("Part 1:", len(re.findall("XMAS", RESULT_STRING)))

###### PART 2

left_to_right_diag = find_diagonal_with_index(data_matrix)
right_to_left_diag = find_diagonal_with_index(reversed_data_matrix, True)

left_to_right_diag.sort()
right_to_left_diag.sort()

for r in data_matrix:
    print(r)

count = 0
for i, val in enumerate(left_to_right_diag):
    if right_to_left_diag.__contains__(val):
        count += 1

print(left_to_right_diag)
print(right_to_left_diag)
print(count)