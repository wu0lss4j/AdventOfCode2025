# 2025.12.11
# Advent of Code 2025 | Day 6 part 2

"""
Steps used:

- of course part 2 had to be completely different to part 1... much code to be trashed, much waste
- now srlsy, read the same input file
- the last line contains symbols that dictate either the Σ summations and Π products
- this time around we have to Σ and Π operations in blocks, each block can have 2 or 3 columns (maybe more?) and is limited by an empty column, non empty columns contain the values which are written vertically
- my intuition here is "rotate 90deg clockwise" each digit for each column and then execute the operation
- this time I will over engineer this by working with a transposed list, because, why not
- the answer to part 2 is to tally up all operations

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


def transpose(src_h: list) -> list:
    rows_src_h: int = len(src_h)
    cols_src_h: int = len(src_h[0])

    # print(f"{rows_src_h=} x {cols_src_h=}")

    src_v: list = []
    for i in range(cols_src_h):
        src_v.append([""] * rows_src_h)

    for i, row_v in enumerate(src_h):
        for j, col_v in enumerate(row_v):
            src_v[j][i] = col_v

    return src_v


def calc(a: int, b: int, ops: str) -> int:
    # print(f"{a=} {b=}")
    match ops:
        case "+":
            return a + b
        case "*":
            return a * b


with open("input_day6.txt", "r") as f:
    input_data = f.read()

table_h: list = []
table_v: list = []

for line in input_data.splitlines():
    table_h.append(line)

# Show me the imported table (horizontal)
# for line in table_h:
#     print(line)

table_v = transpose(table_h)
# table_v = convert_all_to_int(table_v)

# Show me the transposed table (vertical)
# for line in table_v:
#     print(line)

table_v_rows = len(table_v)
table_v_cols = len(table_v[0])

print(f"Table contains {table_v_rows} rows and {table_v_cols} cols")

result_vector: list = [0]

for i in range(0, table_v_rows):
    val = "".join((table_v[i][0 : table_v_cols - 1]))
    if val != " " * (table_v_cols - 1):
        num = int(val)
        if table_v[i][table_v_cols - 1] != " ":
            ops = table_v[i][table_v_cols - 1]
            result_vector[-1] = num
        else:
            result_vector[-1] = calc(result_vector[-1], num, ops)
        print(f"{i=:_>4} | {ops} | {num:3} -- ", end="")
        print(result_vector[-1])
    else:
        print(f"\nNEXT BLOCK {len(result_vector) + 1}\n")
        result_vector.append(0)

sum: int = 0
for result in result_vector:
    sum += result

print(f"SUM = {sum:,} \t\t\t\t\t {sum=}")
