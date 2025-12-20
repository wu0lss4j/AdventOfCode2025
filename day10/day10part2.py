# Advent of Code
# Day 10 | 2025.12.19 - ...
#     P2

"""
Now... part 2... so I need to find the minimum number of button presses so that I get the values on the {3, 4, 5, 7} levels... hmmm
"""

from solver_pulp import pulp_my_ride


def find_lights(part: list) -> int:
    # print(f" Lights : {part}", end=" ")
    lights_tmp: str = part.strip("[]")
    lights_tmp_len: int = len(lights_tmp)
    lights_found: int = lights_tmp_len
    return lights_found


def coef_matrix(part: list, max_num_var: int) -> list:  # I changed to integer...
    # print(" Coefs  : ", end="")
    # print(f"{part}", end=" ")
    coef: list = part.strip("()").split(",")
    coef_vector: list = [0] * max_num_var
    for c in coef:
        coef_vector[int(c)] = 1
    # print(f"\t{coef_vector}")
    return coef_vector


def transpose_matrix(matrix: list) -> list:
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    transposed_matrix: list = []

    for _ in range(total_cols):
        transposed_matrix.append([0] * total_rows)
    for i in range(total_rows):
        for j in range(total_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def convert_all_to_int(src) -> int:
    if isinstance(src, list):
        return [convert_all_to_int(item) for item in src]
    else:
        try:
            return int(src)
        except ValueError:
            return src


def convert_vector(vector: list) -> list:
    # print(" Vector : ", end="")
    vector: list = vector.strip("{}").split(",")
    solution_vector: list = []
    solution_vector = list(convert_all_to_int(vector))
    return solution_vector


### bruteforcing my way...
def product(*args, repeat=1):
    # If called with repeat, expand the arguments
    if len(args) == 1 and repeat > 1:
        args = args * repeat
    # print(f"{args=}")

    # Convert all inputs to lists (so we can iterate multiple times)
    pools = [list(pool) for pool in args]
    # Start with one empty tuple
    result = [()]

    # Iteratively build the Cartesian product
    for pool in pools:
        new_result = []
        for prefix in result:
            for item in pool:
                new_result.append(prefix + (item,))
        result = new_result
        print(len(result))

    return result


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

    total_sum: int = 0

    for raw_line in raw_data.splitlines():
        line = raw_line.split(" ")
        line_len = len(line)
        print(f"\n\n > there are {line_len - 2} buttons")

        # print("finding target number of lights...")
        lights: int = 0
        lights = find_lights(line[0])
        # print(f"{lights=}")

        # Coeficient Matrix
        # print("building button (coef) matrix...")
        button_matrix: list = []
        for part in range(1, line_len - 1):
            button_matrix.append(coef_matrix(line[part], lights))
        # print("transposing button (coef) matrix...")
        button_matrix = transpose_matrix(button_matrix)
        print(f"CMatrix={button_matrix}")

        # Vector Solution
        # print("build solution vector...")
        vector: list = []
        vector = convert_vector(line[-1])
        print(f"Vector={vector}")

        print("determine minimum button presses...")
        print("...courtesy of PuLP!")

        total_sum += pulp_my_ride(button_matrix, vector)

        # # THIS IS MY BRUTE FORCE CODE WHICH WOULD TAKE BILLIONS OF YEARS
        # # TO REACH A SOLUTION...
        # # the answer for the number of button presses must lie between
        # # 0 and the largest value in the solution vector,... actually
        # # an optimization could be to limit the variable to minimum of
        # # the solution vector part that variable contributes to
        # max_answer: int = max(vector) + 1
        # answer_interval = range(0, max_answer)

        # rows = len(button_matrix)
        # cols = len(button_matrix[0])
        # print(f"{answer_interval=} {rows=} {cols=}")

        # best = None
        # for x in product(answer_interval, repeat=cols):
        #     if all(
        #         sum(button_matrix[i][j] * x[j] for j in range(cols)) == vector[i]
        #         for i in range(rows)
        #     ):
        #         s = sum(x)
        #         if best is None or s < best[0]:
        #             best = (s, x)

        # print("Best solution:", best[1])
        # print("Minimum sum:", best[0])

        # total_sum += best[0]
    print(f"\n\t{total_sum=}")


if __name__ == "__main__":
    main()
