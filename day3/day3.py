import re

data_file = "day3_test.txt"
data_file = "day3.txt"

with open(data_file) as f:
  data_string = " ".join([l.rstrip("\n") for l in f]) 

reg = re.findall("mul\(\d{1,3},\d{1,3}\)", data_string)

result = 0
for r in reg:
  numbers = re.findall("\d{1,3}", r)

  result += int(numbers[0]) * int(numbers[1])

print(result)