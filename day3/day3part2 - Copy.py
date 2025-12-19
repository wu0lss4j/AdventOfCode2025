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
print(".:. yet another string parsing challenge, or? .:. \n")

input1 = """987654321111111
811111111111119
234234234234278
818181911112111"""

# print(input)

input2 = """
"""


def find_max(number_str: str, start: int, end: int) -> tuple[str, int]:
    number_str_new = number_str[start:end]
    number_max_val: str = max(number_str_new)
    number_max_loc: int = number_str_new.find(number_max_val)
    # print(f">>> {number_str} >> {number_str_new} > {number_max_val} @ {number_max_loc + start}")
    return (
        number_max_val,
        start + number_max_loc,
    )  # return the location from the start of the whole string


# yeah... that huge ass list is input2, for testing I will use input1.splitlines()
input_list: list[str] = input2.splitlines()

# print(input_list)

joltage: int = 0
sum_joltage: int = 0
max12_val: str = [""] * 12
max12_loc: int = [0] * 12
max12: list[str, int] = [max12_val, max12_loc]  # value, location

for item in input_list:
    item_len: int = len(item)
    print(f"\n{item} | {item_len}")

    last_found = 0
    for i in range(0, 12, 1):
        max12[0][i], max12[1][i] = find_max(item, last_found, item_len - (11 - i))
        last_found = max12[1][i] + 1  # next time around start one digit to the right
        print(
            f"{i=:2} {max12[1][i]:2} {item_len - (11 - i):2} | {max12[0][i]} found at {max12[1][i]}"
        )

        # don't forget to early break out of the loop when there the search space is 0
        b = item_len - (11 - i) - max12[1][i]
        # print(f"!!! {b} is this 1")
        if b == 1:
            print("we can skip the rest")
            c: str = ""
            c = c.join(max12[0][0:i])
            print(f" 0 to {i - 1:2} is {c}")
            d = item[max12[1][i] : item_len + 1]
            print(f"{i:2} to 12 is {d}")
            max12_val = list(c + d)
            print(f"{max12_val = }")
            max12[0] = max12_val
            break

    a = ""
    for i in max12_val:
        a = a + i
    joltage = int(a)
    print(f"{joltage = }")
    sum_joltage += joltage

print(f"\n>>> Sum of all joltage is: {sum_joltage}")
