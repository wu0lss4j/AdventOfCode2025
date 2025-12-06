# Advent Of Code 2025
My solutions to Advent of Code 2025 → https://adventofcode.com/2025

## 2025.12.03

[Day 1 Part 1](https://adventofcode.com/2025/day/1) solved using Excel (maybe the 365 version is needed).
    
    Steps used:
    1. open input.txt in Excel
    2. add a first line and type R50 or L50 as the start position
    3. on a second column replace the first char from each line, if R then +, else -, and then convert to value (formulas used: LEFT, IF, REPLACE, and VALUE)
    4. on a third column add a rolling sum (formulas used: SUM)
    5. on a fourth column do mod by 100 (formulas used: MOD)
    6. then count the number of 0 in the fourth column (formulas used: COUNTIF)

## 2025.12.04

[Day 1 Part 2](https://adventofcode.com/2025/day/1) solved using Excel (maybe the 365 version is needed).

    Steps used:
    1. same input data as before
    2. in the fourth column if mod is 0 then display 1, else 0 (formulas used: IF)
    3. update header of fourth column to sum the 1s (formulas used: SUM)
    4. add a fifth column that will compare the start (last position) and end position (current position) and return the number of multiples of 100 exclusively between positions (formulas used MAX, MIN, and FLOOR.MATH)
    5. add header of fifth column to sum the 1s (formulas used: SUM)
    6. add both headers
    math formula: floor[(max(a;b)-1)/100]-floor[(min(a;b))/100]

    Note: FLOOR.MATH considers that the floor of -3.2 is -4

## 2025.12.05

[Day 2 Part 1](https://adventofcode.com/2025/day/2) solved using python (3.14.1)

    Steps used:
    1. Too lazy to read the input.txt file, so instead I hammer that string directly in the code
    2. Parse the string and split at the commas into a list
    3. Each item from the list represents an interval separated by a dash, so parse each item and extract the start and finish
    4. Given the nature of the problem, we are looking for exact duplicates, this means any number that has an odd number of digits can be safely discarded, so some logic was added to adjust the start and finish to the nearest order of magnitude start and finish, i.e.: 999-55555 updates to 1000-9999
    5. Finally, loop each adjusted interval, and split the number in half, take that half of the digits and check if the current index is equal to those digits twice repeated
    6. If True than add to the sum.

[Day 2 Part 2](https://adventofcode.com/2025/day/2) solved using python (3.14.1)
    
    Steps used:
    1. Repeat steps 1-3 as in part 1
    2. Given the nature of the problem, we are looking for patterns, every repeating sequence counts, but only if the number is itself a repeating sequence (aka more than once). So 11111 and 123123 are fine, and 1111 is only counted as 4x 1, and not 2x 11. This is important to break out of the loop
    3. So I will loop each set interval, and then convert each number into a string and loop that, and finally loop with early break as it looks for repeating patterns.
    4. This loop with early break will start at the first digit and check if the current number is composed only of that digit, if yes then add that number and break out of that loop, if not, get the first 2 digits and check if the current number is those two digits repeated N times where N is the string size divided by pattern size
    5. tinse and tepeat

    Note: an X digit number, can only start repeating up to X/2 digits, like if an 8 digit number starts like 1213.... then I don't need to check the pattern 12133... because it's obvious.

## 2025.12.06

[Day 3 Part 1](https://adventofcode.com/2025/day/2) solved using python (3.14.1)

    Steps used:
    1. Again... lazy to read from a file so I just pasted the whole input directly on the code.
    2. Created a function that will return the largest digit in a string of digits accepting the string and a start location
    3. Given the nature of the problem, we're to look for the largest combination of vales always left to right.
    4. Need to search two times, after finding the largest digit in the string, lookup the next largest to the right of this digit (see Note below)
    5. tinse and tepeat

    Note: There could be a special case where the string is long string of 0 except for the last digit, so for this case the answer is the last digit.
