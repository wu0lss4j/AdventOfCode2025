# Advent of Code 2025
# Day 1 part 1 | 2026.01.14 Python rewrite

def xmas() -> None:
    xmas_tree = "\
         1\n\
        ***\n\
       *****\n\
      *O**#**\n\
     ****O**.*\n\
    *§******@**\n\
        {$}\n\
       _{$}_   (bl)\n"

    print(xmas_tree)

def direction_to_sign(dir:str) -> int:
    match dir:
        case "R":
            return 1
        case "L":
            return -1
        case _:
            return 0 # actually I should just raise an error

def turn(position: int, direction: int, amount: int) -> int:
    position += direction * amount
    return position

def main():
    xmas()

    with open("input_day1.txt", "r") as f:
        raw_data = f.read()

    # Starting conditions
    direction: int = 1
    amount: int = 50
    position: int = direction * amount
    counter: int = 0

    print(f"Starting position is {position}")

    for row in raw_data.splitlines():
        direction = direction_to_sign(row[0])
        row_len:int = len(row)
        amount = int(row[1:row_len])
        #print(f"{row=} {direction} {amount}")
        position = turn(position, direction, amount)
        #print(f"{position}")

        # basically is the dial position a multiple of 100
        if position % 100 == 0:
            counter += 1
        # input("press any key")

    print(f"Number of times dial ended at 0: {counter}")
    
if __name__ == "__main__":
    main()