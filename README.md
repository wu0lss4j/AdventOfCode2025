# Advent Of Code 2025
My solutions to Advent of Code 2025 → https://adventofcode.com/2025

## 2025.12.03

[Day 1](https://adventofcode.com/2025/day/1) solved using Excel (maybe the 365 version is needed).

    Steps used:
    1. open input.txt in Excel
    2. add a first line and type R50 or L50 as the start position
    3. on a second column replace the first char from each line, if R then +, else -, and then convert to value (formulas used: LEFT, IF, REPLACE, and VALUE)
    4. on a third column add a rolling sum (formulas used: SUM)
    5. on a fourth column do mod by 100 (formulas used: MOD)
    6. then count the number of 0 in the fourth column (formulas used: COUNTIF)
