import itertools

def print_progress_bar(iteration, total, length=50):
    percent = 100 * (iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r|{bar}| {percent:.1f}% Complete', end='\r')
    if iteration == total:
        print()  # Move to the next line when done

def read_file():
    DATA_FILE = "day7_test.txt"
    DATA_FILE = "day7.txt"
    
    with open(DATA_FILE) as file:
        return [line.strip() for line in file.readlines()]

def process_lines(input_lines):

    result = 0
    valid_line_indices = []
    for i, line in enumerate(input_lines):
        expected_result, arguments = line.split(":")
        expected_result = int(expected_result)
        
        valid_operator_combinations = validate_line(expected_result, arguments)
        if len(valid_operator_combinations) > 0:
            result += expected_result
            valid_line_indices += [i]

        print_progress_bar(i, len(input_lines))
        
    return result, valid_line_indices

def validate_line(expected_result: str, arguments: str):
    arguments: list = [int(c) for c in arguments.strip().split(" ")]

    number_of_args = len(arguments)
    
    operator_combinations = list(itertools.product(OPERATORS, repeat=number_of_args-1))
   
    valid_operator_combinations = []
    for operator_combination in operator_combinations:
        operators, current_arguments = list(operator_combination).copy(), arguments.copy()
        evaluated_result = current_arguments[0]
        for i, operator in enumerate(operators):
            if operator == "+":
                evaluated_result += current_arguments[i+1]
            if operator == "*":
                evaluated_result *= current_arguments[i+1]
            if operator == "||":
                evaluated_result = int(str(evaluated_result) + str(current_arguments[i+1]))
     
        if evaluated_result == expected_result:
            valid_operator_combinations += [list(operators)]
    
    return valid_operator_combinations

OPERATORS = ["*", "+"]

file_input = read_file()
result_part_one, valid_line_counter = process_lines(file_input)

OPERATORS = ["*", "+", "||"]

non_valid_lines = [line for i, line in enumerate(file_input) if i not in valid_line_counter]

result_part_two, valid_lines_part_two = process_lines(non_valid_lines)
print("Part 1:", result_part_one, valid_line_counter)

print("Part 2:", result_part_two + result_part_one, valid_lines_part_two)
