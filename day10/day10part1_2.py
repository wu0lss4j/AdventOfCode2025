# Advent of Code
# Day 10 | 2025.12.19 - ...
#

"""
This is the XOR-tastic challenge. I could be wrong, but it seems that part 2 will have us try to find the cheapest number of button presses. Since I am still on part 1,...

Steps used:
- parse input file as follows, the first field contains between brackets the expected binary combination written left-to-right, so [..#.] is actually 0100, all fields following that one between parethesis are the several binary position that can be flipped in a single move, so (1,3) means it will flip 0101 (note, left-to-right) and finally between chavetas (dunno the word in English right now), contain some kind of cost for turning on each line (there are as many values between chavetas as "positions" in the target) but that can be safely ignored for the first challenge part.
- my idea is more or less, use the XOR operation to combine the available moves to get to the target, i.e.: XOR 1010 0101 = 1111 and XOR 1111 1001 = 0110 which is our goal and cost us 2 moves

Note: after having so much fun converting all to binary, I learn that our friend ^ (xor) only accepts integers. r/fml scratch all this code and work with integers only.
"""

Binary = str


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def total_combinations(req_buttons: int, total_buttons: int) -> int:
    total = factorial(total_buttons) / (
        factorial(req_buttons) * factorial(total_buttons - req_buttons)
    )
    return int(total)


def comb(options: list, choices: int) -> list:
    res = []
    stack = [(0, [])]

    while stack:
        start, path = stack.pop()

        if len(path) == choices:
            res.append(path)
            continue

        for i in range(start, len(options)):
            stack.append((i + 1, path + [options[i]]))

    return res


def find_lights(part: list) -> int:
    print(f"Lights: {part}", end=" ")
    lights_tmp: str = part.strip("[]")
    lights_tmp_len: int = len(lights_tmp)
    lights_found: int = lights_tmp_len
    return lights_found


def convert_target(part: list) -> Binary:  # I changed to integer...
    print(f" Target: {part}", end=" ")
    target_binary: str = ""
    translation_table = str.maketrans({"[": "", ".": "0", "#": "1", "]": ""})
    str_tmp: str = str(part).translate(translation_table)
    target_binary = "0b" + str_tmp[::-1]
    target_integer: int = int(target_binary, 2)
    print(f" >>> {target_binary} >>> {target_integer=}")
    return target_integer


def convert_moves(part: list) -> Binary:  # I changed to integer...
    print(" Moves : ", end="")
    print(f"{part}", end=" ")
    move_binary: str = ""
    move_tmp: list = part.strip("()").split(",")
    bin_tmp: int | str = 0
    for pwr in move_tmp:
        bin_tmp = bin_tmp + 2 ** int(pwr)

    move_binary = bin(bin_tmp)
    move_integer = int(move_binary, 2)
    print(f" >>> {move_binary} {move_integer=}")

    return move_integer


def xor_bin(a: Binary, b: Binary) -> Binary:
    int_a: int = int(a, 2)
    int_b: int = int(b, 2)
    return bin(int_a ^ int_b)


def xor(a: int, b: int) -> int:
    return a ^ b


def xmas() -> None:
    xmas_tree = "\
         1\n\
        *0*\n\
       *****\n\
      *O**#**\n\
     ****O**.*\n\
    *§******@**\n\
        {$}\n\
       _{$}_   (bl)\n"

    print(xmas_tree)


def main() -> None:
    xmas()

    with open("input_day10.txt", "r") as f:
        raw_data = f.read()

    flip_counter: int = 0

    for raw_line in raw_data.splitlines():
        line = raw_line.split(" ")
        line_len = len(line)

        # print("finding target number of lights...")
        # lights: int = 0
        # lights = find_lights(line[0])

        print("converting targets...")
        target: int = 0
        target = convert_target(line[0])

        print("converting moves...")
        moves: list = []
        for part in range(1, line_len - 1):
            moves.append(convert_moves(line[part]))
        moves_len: int = len(moves)
        print(f" Moves : {moves}")

        print(f" Cost  : {line[-1]}")  # d10p1 does nuttin'

        # r/til that python does xor operations with integers
        # sorted_moves = sorted(moves, reverse=True, key=lambda x: int(x, 2))
        # moves = sorted(moves, reverse=True)
        # print(f"{moves=}")

        result: int = 0
        # max_lights_bin: int = 0
        # for l_pwr in range(lights):
        #     max_lights_bin += 2**l_pwr
        # print(f"{bin(max_lights_bin)=} {max_lights_bin=}")

        buttons: int = 1  # Start with at least one button...
        target_found = False
        while buttons <= moves_len and not target_found:
            # print(
            #     f"Any {buttons} from {moves_len} means total space is {total_combinations(buttons, moves_len)}"
            # )
            possible_moves = comb(moves, buttons)
            # print(f"{possible_moves}")
            print(f"Trying with {buttons} buttons.")
            for m in possible_moves:
                # print(f"  testing {m}")
                for button_m in m:
                    # print(f"  flipping button {button_m} {bin(button_m)=}")
                    result = xor(result, button_m)
                if result == target:
                    print(f"  {result=}, {bin(result)=} buttons pressed: {buttons}")
                    flip_counter += buttons
                    target_found = True
                    break
                result: int = 0

            buttons += 1

        print(f"Accumulated {flip_counter=}\n")

        ### IMMA STOP HERE AND DO ALL THIS MEFF IN INTEGER...


if __name__ == "__main__":
    main()
