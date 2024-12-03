import re
import sys

data_file = "day3_test.txt"
data_file = "day3.txt"

with open(data_file) as f:
  data_string = " ".join([l.rstrip("\n") for l in f]) 

def part_one():
  reg = re.findall("mul\(\d{1,3},\d{1,3}\)", data_string)

  result = 0
  for r in reg:
    numbers = re.findall("\d{1,3}", r)

    result += int(numbers[0]) * int(numbers[1])

  print("Part 1:", result)

def find_valid_ranges(dos, donts) -> list:
  start_indices_do = [(do.start(), True) for do in dos]
  start_indices_dont = [(dont.start(), False) for dont in donts]

  sorted_do_or_dont_tuples = sorted(start_indices_do + start_indices_dont, key = lambda tup: tup[0])

  cleaned_do_or_dont_tuples = [] + [sorted_do_or_dont_tuples[0]]
  for i in range(len(sorted_do_or_dont_tuples) - 1):
    if not cleaned_do_or_dont_tuples[-1][1] == sorted_do_or_dont_tuples[i+1][1]:
      cleaned_do_or_dont_tuples += [sorted_do_or_dont_tuples[i+1]]

  valid_ranges = [] + [(0, cleaned_do_or_dont_tuples[0][0])]
  for i in range(1, len(cleaned_do_or_dont_tuples) - 1, 2):
    valid_ranges += [(cleaned_do_or_dont_tuples[i][0], cleaned_do_or_dont_tuples[i+1][0])]
  
  # If the operations end in a do() without closing don't
  if cleaned_do_or_dont_tuples[-1][1]:
    valid_ranges += [(cleaned_do_or_dont_tuples[-1][0], 999999999)]

  return valid_ranges

def part_two():
  mul_operations = re.finditer("mul\(\d{1,3},\d{1,3}\)", data_string)
  dos = re.finditer("do\(\)", data_string)
  donts = re.finditer("don't\(\)", data_string)

  valid_ranges = find_valid_ranges(dos, donts)
  
  result = 0
  for mul_operation in mul_operations:
    for range in valid_ranges:
      if mul_operation.start() > range[0] and mul_operation.start() < range[1]:
        mul_numbers = re.findall("\d{1,3}", mul_operation.group())
        result += int(mul_numbers[0]) * int(mul_numbers[1])

  print("Part 2:", result)

part_one()
part_two()