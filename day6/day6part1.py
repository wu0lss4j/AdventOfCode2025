# 2025.12.10
# Advent of Code 2025 | Day 6

"""
Steps used:

- read input file and parse each line into lists using a variable number of empty spaces as dividers
- there could be any number of lines in the file and thousands of values
- the last line contains symbols that dictate either the sum or product of the previous lines
- first I remove all spaces until I have just values which are placed into a list as int
- then a result vector is created to hold the operation until Σ summations and Π products are carried out
- the answer to Part 1 is to tally up all operations

"""

ii: int = 0  # counter for recursion (and sanity check...)


def convert_all_to_int(src) -> int:
    global ii
    ii += 1
    # print(ii, end="-")
    if isinstance(src, list):
        return [convert_all_to_int(item) for item in src]
    else:
        try:
            return int(src)
        except ValueError:
            return src


def strip_extra_spaces(str_i: str) -> str:
    str_t: list = []
    str_o: list = []

    for c in str_i:
        # print(f"processing {c=} Flag {is_space=} \t {str_i=} \t {str_t=} \t {str_o=}")
        if c == " ":
            if len(str_t) != 0:
                str_o.append("".join(str_t))
                str_t.clear()
            continue
        else:
            str_t.append(c)

    if len(str_t) != 0:
        str_o.append("".join(str_t))
        str_t.clear()

    return str_o


def calc(a: int, b: int, ops: str) -> int:
    # print(f"{a=} {b=}")
    match ops:
        case "+":
            return a + b
        case "*":
            return a * b


with open("input_day6.txt", "r") as f:
    input_data = f.read()

table: list = []

for line in input_data.splitlines():
    table.append(strip_extra_spaces(line))

table = convert_all_to_int(table)

table_rows = len(table)
table_cols = len(table[0])

print(f"Table contains {table_rows} rows and {table_cols} cols")
# print(f"Values     {table[0 : table_rows - 1]}")
# print(f"Operations {table[table_rows - 1]}")

result_vector: list = [0] * table_cols
# print(f"{result_vector=}")

for i in range(0, table_cols):
    # print(f"{i=}")
    result_vector[i] = calc(result_vector[i], table[0][i], "+")
    for j in range(1, table_rows - 1):
        # print(f"{i=} {j=}")
        # print(f"{table[j][i]=} {table[-1][i]=} {table[j - 1][i]=}")

        # table[j][i] = calc(table[j][i], table[j - 1][i], table[-1][i])
        result_vector[i] = calc(table[j][i], result_vector[i], table[-1][i])

# print(f"{result_vector=}")

sum: int = 0
for result in result_vector:
    sum += result

print(f"{sum=}")
