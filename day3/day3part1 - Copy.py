# 2025.12.06
# Day Zree because Ze Germanz

xmas_tree = "\
     3\n\
    ***\n\
   ***§*\n\
  *O*****\n\
 ****'****\n\
**§*****@**\n\
    { }\n\
   _{_}_\n"

print(xmas_tree)
print(".:. another string parsing challenge, or? .:. \n")

input = """987654321111111
811111111111119
234234234234278
818181911112111"""

# print(input)

input = """
"""


def find_max(number_str: str, start: int) -> tuple[str, int]:
    number_str_new = number_str[start:]
    number_max_val: str = max(number_str_new)
    number_max_loc: int = number_str_new.find(number_max_val)
    return number_max_val, number_max_loc


input_list: list[str] = input.splitlines()

print(input_list)

joltage: int = 0
sum_joltage: int = 0
max_val1: int = 0
max_val2: int = 0
max_loc1: int = 0
max_loc2: int = 0

for item in input_list:
    item_len: int = len(item)
    print(f"\n{item} | {item_len}")

    max_val1, max_loc1 = find_max(item, 0)

    if max_loc1 == item_len - 1:  # just in case, check if all other digits are 0
        if int(item[:-1] == 0):
            max_val2 = max_val1
            max_val1 = 0
            continue
        else:
            max_val2 = max_val1
            max_val1, max_loc1 = find_max(item[:-1], 0)

        print(f"found largest: {max_val1}{max_val2}")
        joltage = int(max_val1) * 10 + int(max_val2)
        sum_joltage += joltage
        continue

    print(f">>> 1: {max_val1} at {max_loc1}")

    max_val2, max_loc2 = find_max(item, max_loc1 + 1)
    print(f">>> 2: {max_val2} at {max_loc2}")

    print(f"found largest: {max_val1}{max_val2}")
    joltage = int(max_val1) * 10 + int(max_val2)
    sum_joltage += joltage

print(f">>> Sum of all joltage is: {sum_joltage}")
