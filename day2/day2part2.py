# Advent of Code 2025
# Day 2 part 2

print('Let\'s try some string manipulation.')

# input = '111111-116182'

# input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224, \
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659, \
# 824824821-824824827,2121212118-2121212124'

input = '5959566378-5959623425,946263-1041590,7777713106-7777870316,35289387-35394603,400-605,9398763-9592164,74280544-74442206,85684682-85865536,90493-179243,202820-342465,872920-935940,76905692-76973065,822774704-822842541,642605-677786,3759067960-3759239836,1284-3164,755464-833196,52-128,3-14,30481-55388,844722790-844967944,83826709-83860070,9595933151-9595993435,4216-9667,529939-579900,1077949-1151438,394508-486310,794-1154,10159-17642,5471119-5683923,16-36,17797-29079,187-382'

input_list: list = list(input.split(','))

sum_j: int = 0

for i in input_list:
    print(f'\n### Now working on {i}')
    
    interval_adjusted: bool = False

    interval: list = list(i.split('-'))
    interval_s: int = int(interval[0])
    interval_s_len: int = len(str(interval_s))
    interval_f: int = int(interval[1])
    interval_f_len: int = len(str(interval_f))
    interval_size: int = interval_f - interval_s + 1
    
    print(f'{interval_s} to {interval_f}')

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

    print(f'\nThe sum so far... >>> {sum_j}')

print(f'\nThe answer is: {sum_j}')