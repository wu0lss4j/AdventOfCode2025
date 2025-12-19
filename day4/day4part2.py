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

  - but for this part 2 of the puzzle, I need to remove the found @ that have less than 4 @s in its perimiter, so a new state needs to be saved
  - then run again on the new state and see how many @ still exist with less than 4 @s in its perimiter and remove those
  - rinse repeat, until all existing @s do NOT have less than 4 @s in its perimiter

  Note: for some reasons I made a perimiter function of variable size as I tried to predict that part 2 would go in this direction, alas, it did not :-)

Sounds like a plan, let's do it!  
"""

import copy     # I need deepcopy for some matrix manipulation



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
    #print(f"{targets_found = }")    

    return str(targets_found)

done = False
count_ats = 0
count_ops = 0

while not done:

    try:
        with open("warehouse_tmp.txt") as f:
            data = f.read()
    except Exception as e:
        print(f"whaaaat? >>> {e}")
        with open("input_day4.txt") as f:
            data = f.read()

    warehouse: list = [] # source data
    warehouse_tmp: list = [] # source data temp (after a batch of @s are removed)
    targets: list = [] # num of targets at each @ location
    count_ats_tmp = 0

    line:list = []
    for line in data.splitlines():
        warehouse.append(list(line))

    row_M: int = len(warehouse)
    col_M: int = len(line)
    print(f"Warehouse is {row_M} by {col_M} and looks like this now:")
    print(f"{data}")

    for _ in range(row_M):
        targets.append([""] * (col_M))

    warehouse_tmp = copy.deepcopy(targets) # make an empty copy of the targets (same size as the warehouse)

    for row_i, row_v in enumerate(warehouse):
        # print(f"{row_i = } | {row_v = }")
        for col_i, col_v in enumerate(row_v):
            if col_v == "." or col_v == "x":
                targets[row_i][col_i] = "."
                warehouse_tmp[row_i][col_i] = "."
                continue

            # print(f"{row_i:_>3},{col_i:_>3} = {warehouse[row_i][col_i]}")  
            find_ats = perimiter_check(row_i, col_i, 1)
            targets[row_i][col_i] = find_ats
            if int(find_ats) <= 4:                  # if there are 4 or less @ (incl. cur position)
                warehouse_tmp[row_i][col_i] = "x"   # that @ is removed
                count_ats += 1
                count_ats_tmp += 1                      # and count that removed @
            else:
                warehouse_tmp[row_i][col_i] = warehouse[row_i][col_i]

    with open("warehouse_tmp.txt", "w") as f:
        for i in range(0, len(warehouse_tmp)):
            # write to disk the new warehouse configuration
            f.write("".join(list(warehouse_tmp[i])) + "\n")
        count_ops += 1

    # for i in range(0, len(targets)):
    #     print("".join(list(targets[i])))

    print(f"{count_ops} warehouse states (incl. initial) and we have moved {count_ats = } @s")
    
    if count_ats_tmp == 0:
        done = True