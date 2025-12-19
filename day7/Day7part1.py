# Day 7 part 1
#

"""
Steps used:
- import the file into a base state
- find the starting point on the first line, S and note the position (this is the first pipe "|" )
- proceed to loop through all entries in the state, but jump directly to the "|" known positions
- if on the "|" known position there is a "." then change to "|", update the "I" known positions
- if on the "|" known position there is a "^" then remove that position from the known positions and add two new positions at +1/-1 from the "^" position, and increment the split counter
- rinse and repeat
"""


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


def update_print_conf(pipe_loc: list, row: int) -> None:
    for i in pipe_loc:
        # print(f"dentro da func {i=} {row=}")
        print_conf[row][i] = "|"


def split_pipe_tmp(index: int) -> None:
    # print(f"\n    splitting at {index} w/ value {pipe_list[index]}")
    val = pipe_list[index]

    # remove item from updated pipe list
    # pipe_list_tmp.pop(index)

    # add two new items / splits
    if val - 1 not in pipe_list_tmp:
        pipe_list_tmp.append(val - 1)
    if val + 1 not in pipe_list_tmp:
        pipe_list_tmp.append(val + 1)

    # print(f"!!! New pipe List is currently: {pipe_list_tmp=}")
    # print(f"!!!             to remove item: {pipe_list[index]=}")
    pipe_list_tmp.remove(val)
    # print(f"!!!           to be updated to: {pipe_list_tmp=}")


def show_print_conf() -> None:
    print("        012345678901234567890")
    for i, line in enumerate(print_conf):
        print(f"{i:3} ->- {''.join(line)}")


# MAIN LOOP
xmas()

with open("input_day7.txt", "r") as f:
    input_data = f.read()

splitcounter: int = 0
start_conf: dict = {}

start_conf = {i: v for i, v in enumerate(input_data.splitlines())}
start_conf_len = len(start_conf)
pipe_list: int = []
pipe_list_tmp: int = []
print_conf: list = []

for i in range(start_conf_len):
    print_conf.append(["."] * len(start_conf[0]))


# print(f"{len(start_conf)=} {start_conf=}")

# Find the starting point
pipe_list = [i for i, _ in enumerate(start_conf[0]) if start_conf[0][i] == "S"]
pipe_list_tmp = pipe_list.copy()
# print(f"Pipe List updated: {pipe_list=}")
# print(f"                   {pipe_list_tmp=}")
print_conf[0][pipe_list[0]] = "S"


for line in range(1, start_conf_len):
    print(f">>> {line=} started <<<")
    for entry_i, entry_v in enumerate(pipe_list):
        # print(f"on {entry_i=} containing {entry_v=}")
        match start_conf[line][entry_v]:
            # case ".":
            #     print(f"just propagating beam @ {entry_v=} (index {entry_i})")
            #     # update_print_conf(pipe_list, line)
            case "^":
                # print(f"!!! mirror found @ {entry_v=} (index {entry_i})")
                splitcounter += 1
                # print(f"{print_conf[line][entry_v]=} <<< {start_conf[line][entry_v]=}")
                print_conf[line][entry_v] = start_conf[line][entry_v]
                # print(f"Current Pipe List: {pipe_list=}")
                split_pipe_tmp(entry_i)
                # print(f"Updated Pipe List: {pipe_list_tmp=}")

    print(f">>> {line=} completed <<<")
    pipe_list.clear()
    pipe_list = pipe_list_tmp.copy()
    pipe_list.sort()
    # print(f"Current Pipe List {pipe_list=}")
    update_print_conf(pipe_list_tmp, line)

    # done = False
    # while not done:
    #     show_print_conf()
    #     input_user = input("...enter any key...")
    #     if input_user is not None:
    #         done = True

    # pipe_list_tmp.clear()
    # for j in start_conf[i]
    # update_print_conf(pipe_list, 1)


show_print_conf()

print(f"{splitcounter=}")
