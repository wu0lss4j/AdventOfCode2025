# 2025.12.14
# Trying Day 7 Part 2 (for the 3rd time)

"""
Great scots... this one is like an inverse filter.

read the input file as a list of lists and call it a world
parse each line of the world from the end
have a temp vector to hold the line total
reset that vector to a series of 1s
each time a "^" is found, add the values of the two adjacent positions in the vector
rinse repeat
when reaching the top, get the value from the vector that matches the position of the S
"""

from datetime import datetime


def xmas() -> None:
    xmas_tree = "\
         7\n\
        ***\n\
       ***§*\n\
      *O*****\n\
     ****'****\n\
    **§*****@**\n\
        { }\n\
       _{_}_\n"

    print(xmas_tree)


# MAIN

xmas()

timer_start = datetime.now().timestamp()
print(f"Started : {datetime.now()}")

with open("input_day7.txt", "r") as f:
    input_data = f.read()

world: list = []

for row in input_data.splitlines():
    world.append(list(row))

row_calc: list = [1] * len(world[0])

for i in range(len(world) - 1, -1, -1):
    for j, v in enumerate(world[i]):
        if v == "^":
            row_calc[j] = row_calc[j - 1] + row_calc[j + 1]

S_loc: int = world[0].index("S")

timer_finished = datetime.now().timestamp()
print(f"Finished: {datetime.now()}")
print(f"\n {row_calc[S_loc]:,} rows in {timer_finished - timer_start} seconds")
