# from ..AdventOfCodeCommon import *

def print_progress_bar(iteration, total, length=50):
    percent = 100 * (iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r|{bar}| {percent:.1f}% Complete', end='\r')
    if iteration == total:
        print()  # Move to the next line when done

def read_file():

    DATA_FILE = "day9_test.txt"
    DATA_FILE = "day9.txt"

    with open(DATA_FILE) as file:
        return file.readlines()[0].strip()
    
def expand_file_string(input_string: str):
    current_id = 0
    resulting_expansion = []
    
    free_space = False
    for digit in input_string:
        if not free_space:
            for i in range(int(digit)):
                resulting_expansion += [(current_id)]
            current_id += 1
            free_space = True
        else:
            for i in range(int(digit)):
                resulting_expansion += [(".")]
            free_space = False
    
    return resulting_expansion

def compact_file(uncompact_file: str):
    reversed_digits_queue = [t for t in uncompact_file if not t == "."]
    resulting_reorder = []
    dot_counter = 0
    
    for i, value_tuple in enumerate(uncompact_file):
        if value_tuple == ".":
            resulting_reorder += [reversed_digits_queue.pop()]
            dot_counter += 1
        else:
            resulting_reorder += [value_tuple]

    resulting_reorder = resulting_reorder[:len(uncompact_file) - dot_counter]
    resulting_reorder = resulting_reorder + [(".")] * (len(uncompact_file) - len(resulting_reorder))

    return resulting_reorder

input_string = read_file()

expanded_string = expand_file_string(input_string)

compacted_file = compact_file(expanded_string)

result = 0
filtered_file = compacted_file[:compacted_file.index(".")]
for i, d in enumerate(filtered_file):
    current_id = 0
    
    result += i * int(d)
    
#correct_value = "0099811188827773336446555566.............."
#print(correct_value == compacted_file)

print("Part 1:", result)

##########################################################################

def expand_file_string_segments(input_string: str):
    current_id = 0
    resulting_expansion = []
    
    free_space = False
    for digit in input_string:
        if not free_space:
            resulting_expansion += [(current_id, int(digit))]
            current_id += 1
            free_space = True
        else:
            resulting_expansion += [(".", int(digit))]
            free_space = False
    
    return resulting_expansion

def rearrange_files(memory_layout: list):
    reorder_file_queue = [file_segment for file_segment in memory_layout[::-1] if file_segment[0] != "."]
    #print(reorder_file_queue)

    for i, moved_file in enumerate(reorder_file_queue):

        size_of_file = moved_file[1]
        for l, v in enumerate(memory_layout):
            if v[0] == moved_file[0]:
                current_pos_of_file = l
        found_space = False
        for j, segment in enumerate(memory_layout): 
            if segment[0] == ".":
                empty_space = segment[1]

                if empty_space < size_of_file:
                    continue
                elif current_pos_of_file < j:
                    continue
                else:
                    found_space = True
                    break
        
        if found_space:
            if empty_space - size_of_file > 0:
                memory_layout.insert(j+1, (".", empty_space - size_of_file))
            elif empty_space - size_of_file < 0:
                raise Exception
            
            for k, removing in enumerate(memory_layout):
                if removing[0] == moved_file[0]:
                    memory_layout[k] = (".", removing[1])

            memory_layout[j] = moved_file
        print_progress_bar(i, len(reorder_file_queue))

    return memory_layout
        
expanded_segments = expand_file_string_segments(input_string)

rearranged_memory = rearrange_files(expanded_segments)

result = 0
current_index = 0
for i, file in enumerate(rearranged_memory):
    for j in range(file[1]):
        if file[0] != ".":
            result += current_index * file[0]
        current_index += 1

    print_progress_bar(i, len(rearranged_memory))

print()
print("Part 2:", result)