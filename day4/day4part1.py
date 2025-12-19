# 2025.12.07 Day 4
#

"""
- Read input.txt into memory, it's a matrix full of . and @, and need to count the @s that have
- Loop every char in every line until an @ symbol is found
- When found then loop around that symbol (8 directions and count the number of @ symbol found),
  - for speed, maybe a small 3x3 loop, or -/+ in x, then y, then x&y combination, don't know yet
  - check for error (like out of bounds when close to the edges of the matrix), and continue the loop until finished
  - the number of 
  - importantly a new table is formed on the fly that will hold the number of @ symbols found around each @ symbol including itself
    .@..@         .3..3
    @@.@@         33.44
    ...@. becomes ...6.
    @.@@@         1.454
    ...@.         ...4.
  - then just parse this new table and count the number of 1-4s

Sounds like a plan, let's do it!  
"""

def perimiter_check(x: int, y:int, dist:int) -> str:
    target_area: list[int] = []
    target_size: int = (2 * dist +1)
    for _ in range(target_size):
        target_area.append([0] * (target_size)) # generates an empty (2 * dist + 1) square matrix

    for i in range(0, target_size):
        for j in range(0, target_size):
            a = x + i - dist
            b = y + j - dist
            if a < 0 or a >= col_M:
                target_area[i][j] = "~"
                continue
            if b < 0 or b >= row_M:
                target_area[i][j] = "~"
                continue
            
            #print(f"{a=} of {col_M=},{b=} of {row_M=}")
            target_area[i][j] = warehouse[a][b]
    # print(target_area)
    targets_found: str = str(target_area).count("@")
    print(f"{targets_found = }")    

    return str(targets_found)

with open("input_day4.txt") as f:
    data = f.read()

# data = data.splitlines()
warehouse: list = [] # source data
targets: list = [] # num of targets at each @ location

line:list = []
for line in data.splitlines():
    warehouse.append(list(line)) 

row_M: int = len(warehouse)
col_M: int = len(line)
print(f"Warehouse is {row_M} by {col_M}")
print(f"{data}")

for _ in range(row_M):
    targets.append([""] * (col_M))

count_ats = 0
for row_i, row_v in enumerate(warehouse):
    # print(f"{row_i = } | {row_v = }")
    for col_i, col_v in enumerate(row_v):
        if col_v == ".":
            targets[row_i][col_i] = col_v
            continue

        #print(f"{row_i:_>3},{col_i:_>3} = {warehouse[row_i][col_i]}")  
        find_ats = perimiter_check(row_i, col_i, 1)
        targets[row_i][col_i] = find_ats
        if int(find_ats) <= 4:
            count_ats += 1

# for _ in targets:

for i in range(0, len(targets)):
    # print(targets[i])
    print("".join(list(targets[i])))

print(f"{count_ats = }")
