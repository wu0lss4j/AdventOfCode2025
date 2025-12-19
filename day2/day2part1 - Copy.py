# Advent of Code 2025
# Day 2

print("Let's try some string manipulation.")

input = ""

input_list: list = list(input.split(","))
# print(input_list)

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

    # determine useful interval, i.e. if the number of digits is odd drop those
    if interval_s_len % 2 != 0:  # go up until even
        interval_s = 10 ** (interval_s_len)
        print(f"  adjusted _s {interval_s}")
        interval_adjusted = True

    if interval_f_len % 2 != 0:  # go down until even
        interval_f = 10 ** (interval_s_len) - 1
        print(f"  adjusted _f {interval_f}")
        interval_adjusted = True

    if interval_adjusted:
        print(f"{interval_s} to {interval_f}")

    for j in range(interval_s, interval_f + 1, 1):
        j_str: str = str(j)
        j_str_len: int = len(j_str)
        j_half: str = j_str[0 : int(j_str_len / 2)]
        j_whole: str = j_half * 2
        if j == int(j_whole):
            print(j, end=" ")
            sum_j += j
    print(f"\nThe sum so far... >>> {sum_j}")

print(f"\nThe answer is: {sum_j}")
