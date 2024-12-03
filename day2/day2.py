import pandas as pd
import numpy as np

def is_faulty(row):
    if not (all(row > 0) or all(row < 0)):
        return True

    row = abs(row)

    if any(row > 3) or any(row < 1):
        return True

    return False

def is_faulty_after_removed_level(row):
    diff = row[0:-1] - row[1:]
    
    if not is_faulty(diff):
        return False

    for i in range(len(row)):
        new_row = np.delete(row, i, 0)
        new_diff = new_row[0:-1] - new_row[1:]

        if not is_faulty(new_diff):
            return False

    return True

data_file = "day2.csv"
largest_column_count = 0
with open(data_file, 'r') as temp_f:
    # Read the lines
    lines = temp_f.readlines()

    for l in lines:
        # Count the column count for the current line
        column_count = len(l.split(",")) + 1

        largest_column_count = column_count if largest_column_count < column_count else largest_column_count

df = pd.read_csv("day2_test.csv", header=None)
df = pd.read_csv(data_file, names=[i for i in range(largest_column_count)])

correct_reports = 0
faulty_reports = 0

correct_reports_2 = 0
faulty_reports_2 = 0
for row in df.iloc[:,:].to_numpy():
    #print(row, ":", row[:-1], ":", row[1:], ":", row[:-1] - row[1:])
    row = row[np.isfinite(row)]
    row_diff = row[:-1] - row[1:]

    if is_faulty(row_diff):
        faulty_reports += 1
    else:
        correct_reports += 1
 
    if is_faulty_after_removed_level(row):
        faulty_reports_2 += 1
    else:
        correct_reports_2 += 1

print("Correct reports:", correct_reports)
print("Faulty reports:", faulty_reports)

print("Correct reports 2:", correct_reports_2)
print("Faulty reports 2:", faulty_reports_2)