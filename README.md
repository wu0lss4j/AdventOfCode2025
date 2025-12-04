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
    
