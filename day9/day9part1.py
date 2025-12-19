#
#  DAY NEUN
# 2025.12.15
#


def to_float(a: list) -> None:
    for i, val_i in enumerate(a):
        a[i] = float(val_i)


def area2(a: list, b: list) -> float:
    area: float = 0
    area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
    return area


def xmas() -> None:
    xmas_tree = "\
         9\n\
        ***\n\
       ***§*\n\
      *O*****\n\
     ****'****\n\
    **§*****@**\n\
        { }\n\
       _{ }_   (bl)\n"

    print(xmas_tree)


# MAIN

xmas()

with open("input_day9.txt", "r") as f:
    input_data = f.read()

tiles: dict = {}

for i, row in enumerate(input_data.splitlines()):
    tiles[i] = list(row.split(","))
    to_float(tiles[i])

tiles_len = len(tiles)
print(f"{tiles_len=}")
print(f"{tiles=}")

area2_matrix: list = []

for i in range(tiles_len):
    area2_matrix.append([0] * tiles_len)

area2_matrix_len = len(area2_matrix)

for i in range(0, tiles_len):
    for j in range(i, tiles_len):
        area2_matrix[i][j] = area2(tiles[i], tiles[j])
        area2_matrix[j][i] = area2_matrix[i][j]

print(f"{area2_matrix}")

area2_matrix_list: list = []
entry: float = 0

for i in range(0, area2_matrix_len):
    for j in range(i + i, area2_matrix_len):
        entry = [area2_matrix[i][j], i, j]
        area2_matrix_list.append(entry)

area2_matrix_list.sort(reverse=True)

TOP: int = 3
print(f"TOP {TOP} sorted by area")
for i, item in enumerate(area2_matrix_list):
    print(f"{i:2} : {item}")
    if i > TOP - 2:
        break

result: float = []

result = area2_matrix_list[0][0]

print(f"Largest area {result=}")
