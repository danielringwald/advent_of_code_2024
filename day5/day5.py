def map_to_int(array):
    return [int(c) for c in array.split(",")]

def test_rules(value, line: list, rule_dict: dict):
    return all([number not in rule_dict.get(value, []) for number in line])

def find_middle_number(array):
    return array[int((len(array) - 1) / 2)]

def parse_rules_to_dict(rules_input):
    rule_dict = {}
    for rule in rules:
        numbers = rule.split("|")
        first_number = int(numbers[0])
        second_number = int(numbers[1])
        rule_dict[first_number] = rule_dict.get(first_number, []) + [second_number]

    return rule_dict

def get_incorrect_numbers(integer_line) -> list:
    incorrect_numbers = []
    for i, val in enumerate(integer_line[::-1]):
        if not test_rules(val, integer_line[:len(integer_line) - i], rule_dict):
            incorrect_numbers += [val]
    return incorrect_numbers

def find_correct_lines(lines, rule_dict) -> list:
    correct_lines = []
    incorrect_lines = []
    for line in lines:
        integer_line = map_to_int(line)
        
        incorrect_numbers = get_incorrect_numbers(integer_line)

        if len(incorrect_numbers) == 0:
            correct_lines += [integer_line]
        else:
            incorrect_lines += [integer_line]

    return correct_lines, incorrect_lines

DATA_FILE = "day5_test.txt"
DATA_FILE = "day5.txt"

data = []
with open(DATA_FILE, 'r', encoding="utf8") as file:
    for line in file.readlines():
        data += [line.strip()]

split_index = data.index('')
rules = data[:split_index]
lines = data[split_index + 1:]

rule_dict = parse_rules_to_dict(rules)

correct_lines, incorrect_lines = find_correct_lines(lines, rule_dict)

result = 0
for valid_line in correct_lines:
    result += find_middle_number(valid_line)

print("Part 1:", result)

def find_rule_violations(val: int, line: list, rule_dict: dict) -> list:
    faults = []
    sub_line = line[:line.index(val)]
    rule = rule_dict.get(val)
    
    for number in sub_line:
        if number in rule:
            faults += [number]
    
    return faults

for incorrect_line in incorrect_lines:
    is_valid = False
    while not is_valid:
        faulty_numbers = get_incorrect_numbers(incorrect_line)
        
        if len(faulty_numbers) == 0:
            is_valid = True

        for faulty_number in faulty_numbers:
            violations = find_rule_violations(faulty_number, incorrect_line, rule_dict)
            for violation in violations:
                faulty_index = incorrect_line.index(faulty_number)
                violation_index = incorrect_line.index(violation)
                incorrect_line[faulty_index] = violation
                incorrect_line[violation_index] = faulty_number
        
result = 0
for line in incorrect_lines:
    result += find_middle_number(line)

print("Part 2:", result)