# Advent of Code 2025
# Day 2 part 2

print("Let's try some string manipulation.")

input = ""

input_list: list = list(input.split(","))

sum_j: int = 0

for i in input_list:
    print(f"\n### Now working on {i}")

    interval_adjusted: bool = False

    interval: list = list(i.split("-"))
    interval_s: int = int(interval[0])
    interval_s_len: int = len(str(interval_s))
    interval_f: int = int(interval[1])
    interval_f_len: int = len(str(interval_f))
    interval_size: int = interval_f - interval_s + 1

    print(f"{interval_s} to {interval_f}")

    for j in range(interval_s, interval_f + 1, 1):
        j_str: str = str(j)
        j_str_len: int = len(j_str)

        for k in range(1, j_str_len // 2 + 1):
            j_pat = j_str[:k]
            j_str_rept = j_pat * ((j_str_len) // k)
            if j == int(j_str_rept):
                print(k, j_pat, j_str_rept)
                sum_j += j
                break

    print(f"\nThe sum so far... >>> {sum_j}")

print(f"\nThe answer is: {sum_j}")
