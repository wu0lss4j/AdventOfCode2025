#
#  DAY OCHO
# 2025.12.14
#


def xmas() -> None:
    xmas_tree = "\
         8\n\
        ***\n\
       ***§*\n\
      *O*****\n\
     ****'****\n\
    **§*****@**\n\
        { }\n\
       _{ }_   (bl)\n"

    print(xmas_tree)


def to_float(a: list) -> None:
    for i, val_i in enumerate(a):
        a[i] = float(val_i)


def dist3D(a: list, b: list) -> float:
    dim = len(a)
    sum: float = 0
    for i in range(dim):
        sum += (a[i] - b[i]) ** 2
    return (sum) ** (0.5)


# MAIN
xmas()

with open("input_day8.txt", "r") as f:
    input_data = f.read()

boxes: dict = {}

for i, row in enumerate(input_data.splitlines()):
    boxes[i] = list(row.split(","))
    to_float(boxes[i])

boxes_len = len(boxes)
print(f"{boxes_len=}")
dist3D_matrix: list = []

for i in range(boxes_len):
    dist3D_matrix.append([0] * (boxes_len))

dist3D_matrix_len = len(dist3D_matrix)

# for i in range(0, dist3D_matrix_len):
#     print(f"{i:^8}", end="")
# print()
# for i in range(0, dist3D_matrix_len):
#     for j in range(0, dist3D_matrix_len):
#         print(f"{dist3D_matrix[i][j]:7.1f}", end=" ")
#     print()


for i in range(0, boxes_len):
    for j in range(i, boxes_len):
        dist3D_matrix[i][j] = dist3D(boxes[i], boxes[j])
        dist3D_matrix[j][i] = dist3D_matrix[i][j]

print("-- DISTANCE MATRIX -- ")

# # for i in range(0, dist3D_matrix_len):
# #     for j in range(0, dist3D_matrix_len):
# #         print(f"{dist3D_matrix[i][j]:7.1f}", end=" ")
# #     print()

# for i in range(1, dist3D_matrix_len):
#     print(f"{i:^8}", end="")
# print()
# for i in range(0, dist3D_matrix_len):
#     for j in range(i + 1, dist3D_matrix_len):
#         print(f"{dist3D_matrix[i][j]:7.1f}", end=" ")
#     print(f"\n{'        ' * (i + 1)}", end="")

# print()

# SORT THE DISTANCE MATRIX

dist3D_matrix_list = []
entry = []
for i in range(0, dist3D_matrix_len):
    for j in range(i + 1, dist3D_matrix_len):
        entry = [dist3D_matrix[i][j], i, j]
        dist3D_matrix_list.append(entry)

dist3D_matrix_list_len = len(dist3D_matrix_list)

dist3D_matrix_list.sort()

# dist3D_matrix_list_sorted = sorted(dist3D_matrix_list)

TOP: int = 19  # demo 19; full 999
print(f"TOP {TOP + 1}")
for i, item in enumerate(dist3D_matrix_list):
    print(f"{i} > {item} ")
    if i > TOP:
        break

circuits: dict = {}

circuits_max: int = 0
assigned_boxes: list = []
connections_made: int = 0
boxes_available: int = boxes_len
distances_processed: int = 0

connections_made = 0

item1_circuit: int | None = None
item2_circuit: int | None = None

for i, item in enumerate(dist3D_matrix_list):
    distances_processed = i
    if i > 999:  # demo i > 9; full i > 999
        break
    if boxes_available == 0:
        break

    item1_circuit = None
    item2_circuit = None
    # for circuit in circuits:
    #     print(f"{circuits[circuit]}")
    # print(f"{circuits}")
    print(f"\nChecking: {item[1]} to {item[2]} | {boxes_available=}")

    for circuit in circuits:
        if item[1] in circuits[circuit]:
            item1_circuit = circuit
            # print(f"{item[1]} found in circuit {circuit}")
        if item[2] in circuits[circuit]:
            item2_circuit = circuit
            # print(f"{item[2]} found in circuit {circuit}")

    if item1_circuit is None and item2_circuit is None:
        # print(f"{item[1]} and {item[2]} to start a new circuit")
        circuits_max += 1
        circuits[circuits_max] = [item[1], item[2]]
        boxes_available -= 2

        connections_made += 1
        continue

    if item1_circuit is not None and item2_circuit is None:
        # print(f"{item[2]} to join circuit {item1_circuit}")
        circuits[item1_circuit].append(item[2])
        connections_made += 1
        boxes_available -= 1
        continue

    if item2_circuit is not None and item1_circuit is None:
        # print(f"{item[1]} to join circuit {item2_circuit}")
        circuits[item2_circuit].append(item[1])
        connections_made += 1
        boxes_available -= 1
        continue

    if item1_circuit != item2_circuit:
        # print(
        #     f"{item[1]} and {item[2]} on different circuits. Merging {item2_circuit} with {item1_circuit} and eliminating {item2_circuit}"
        # )
        # circuits[item1_circuit].append(circuits[item2_circuit])
        for i in circuits[item2_circuit]:
            circuits[item1_circuit].append(i)
        circuits.pop(item2_circuit)
        connections_made += 1
        continue

    if item1_circuit == item2_circuit:
        # print(
        #     f"{item[1]} and {item[2]} on same circuit {item1_circuit} / {item2_circuit}"
        # )
        continue

print(circuits)

circuit_sizes: list = []
for key in circuits:
    circuit_sizes.append(len(circuits[key]))

circuit_sizes.sort(reverse=True)
print(f"{circuit_sizes=}")

print(f"{boxes_available=}")
print(f"{connections_made=}")
print(f"{distances_processed=}")

product: int = 1
for i in range(3):
    product = product * circuit_sizes[i]

print(f"{product} = {circuit_sizes[0]} * {circuit_sizes[1]} * {circuit_sizes[2]}")
