# Day 5
#

"""
Steps used:
- read input.txt
- input.txt has two blocks separated by a blank line, the first block contains the ruleset, that is, each line specifies classes of numbers, and the second block contains a sequence of numbers that we check against the classes, if the number does not fit any class, it is discarded. Some numbers may fit more than one class. Also, some classes overlap, so there is room for optmization, reducing the number of passes later on.
- load up the classes form the first block into a list and create a new list of merged classes
- parse the second block against each of classes in the second block, and break the loop on the first confirmation
- add the total number of confirmations... to 874

As for part 2...
- since I had already did the interval class overlap consolidation, now I had only to iterate through all merged classes and sum their respective sizes

Note: I had to design a different demo to catch all edge cases in this merge consolidation code

###
1-5
3-12
4-8
9-11
14-21
20-25
16-17
15-18
13-19

1
5
8
11
17
32
###

"""

ii: int = 0  # counter for recursion (and sanity check...)


def convert_all_to_int(src) -> int:
    global ii
    ii += 1
    # print(ii, end="-")
    if isinstance(src, list):
        return [convert_all_to_int(item) for item in src]
    else:
        return int(src)


fresh: int = 0
spoil: int = 0

with open("input_day5.txt", "r") as f:
    data = f.read()

data_lines: str = data.splitlines()
data_block: list = []

# print(f"{data_lines=}")
print(f"{len(data_lines)=}")

last_i: int = 0
for i in range(len(data_lines)):
    if data_lines[i] == "" or i == len(data_lines) - 1:
        # print(f"S from {last_i} to {i} || {data_lines[last_i:i]=}")
        end_i = i + 1 if i == len(data_lines) - 1 else i
        data_block.append(data_lines[last_i:end_i])
        last_i = i + 1  # skip the blank line
    # else:
    #     print(f"R from {last_i} to {i} || {data_lines[last_i:i]=}")

print(f"{len(data_block[0])=} {len(data_block[1])=}")

# Split interval classes
for i in range(len(data_block[0])):
    data_block[0][i] = data_block[0][i].split("-")

# Convert all entries to int using recursion
data_block = convert_all_to_int(data_block)

# sort the intervals' block
# print(f"...unsorted {data_block[0]=}")
data_block[0].sort()
# print(f".....sorted {data_block[0]=}")

# alternative sort using lambda (good to know)
# data_block[0] = sorted(data_block[0], key=lambda x: (x[0], x[1]), reverse=False)
# print(f".....sorted {data_block[0]=}")

# make a new list for the UNMERGED intervals' classes
classes_u: list = data_block[0].copy()

print(f"...unmerged {len(classes_u)=}")

num_merged_classes_before = len(classes_u)

# MERGE from start to finish of list using for loop

classes_m: list = []
classes_m.append(classes_u[0])
j: int = 0
for i in range(1, len(classes_u), 1):
    if classes_m[j][1] >= classes_u[i][0]:
        if classes_m[j][1] <= classes_u[i][1]:
            classes_m[j][1] = classes_u[i][1]
    else:
        classes_m.append(classes_u[i])
        j += 1

print(f".....merged {len(classes_m)=}")

####################################################
### DAY 5 PART 2 SPECIFIC ##########################
####################################################

total_classes_len: int = 0
for classe in classes_m:
    # print(f"{classe=} size: \t {classe[1] - classe[0] + 1:_>20,}")
    total_classes_len += classe[1] - classe[0] + 1
print(f"{total_classes_len=:_>20,} w00t")

####################################################
####################################################
####################################################

numbers: list = sorted(data_block[1]).copy()

for num in numbers:
    for classe in classes_m:
        if num >= classe[0] and num <= classe[1]:
            fresh = fresh + 1
            break

spoil = len(numbers) - fresh

print(f"{fresh=:_>20,} ({spoil=})")
