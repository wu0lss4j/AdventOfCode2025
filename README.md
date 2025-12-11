# Advent Of Code 2025
My solutions to Advent of Code 2025 → https://adventofcode.com/2025

Note: if you find any of these interesting, helpful, or just want to buy me coffee... you can do so here:
[Buy me Café](https://ko-fi.com/T6T2Q57QX)

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

[Day 3 Part 1](https://adventofcode.com/2025/day/3) solved using python (3.14.1)

    Steps used:
    1. Again... lazy to read from a file so I just pasted the whole input directly on the code
    2. Created a function that will return the first occurrence of the largest digit in a string of digits accepting the string and a start location
    3. Given the nature of the problem, we're to look for the largest combination of vales always left to right
    4. Need to search two times, after finding the largest digit in the string, lookup the next largest to the right of this digit (see Note below)
    5. tinse and tepeat

    Note: There could be a special case where the string is long string of 0 except for the last digit, so for this case the answer is the last digit.

[Day 3 Part 2](https://adventofcode.com/2025/day/3) solved using python (3.14.1)

    Steps used:
    1. Again... lazy to read from a file so I just pasted the whole input directly on the code.
    2. Updated the function to get also accept an end location (which could've been easier with a slice)
    3. Given the nature of the problem, we're to look for the largest combination of 12 digits always left to right that yield the largest number
    4. Now we need to search up to 12 times, but not the whole string, the first pass is from 0 up to the 12th from the end, the next pass is from the last max digit till 11th from the end, usw...
    
    Note: If at any time, the length of search space is 1, then all remaining digits in the string until the end must be part of the solution

## 2025.12.07

[Day 4 Part 1](https://adventofcode.com/2025/day/4) solved using python (3.14.1)

    Steps used:
    - Read input.txt into memory, it's a matrix full of . and @, and need to count the @s that have
    - Loop every char in every line until an @ symbol is found
    - When found then loop around that symbol (8 directions and count the number of @ symbol found),
      - for speed, maybe a small 3x3 loop, or -/+ in x, then y, then x&y combination, don't know yet
      - check for error (like out of bounds when close to the edges of the matrix), and continue the loop until finished
      - the number of 
      - importantly a new table is formed on the fly that will hold the number of @ symbols found around each @ symbol including itself
        .@..@         .3..3
        @@.@@         33.44
        ...@. becomes ...6.
        @.@@@         1.454
        ...@.         ...4.
      - then just parse this new table and count the number of 1-4s

    Sounds like a plan, let's do it!  

## 2025.12.08

[Day 4 Part 2](https://adventofcode.com/2025/day/4) solved using python (3.14.2)

    Steps used:
    - ...
    - but for this part 2 of the puzzle, I need to remove the found @ that have less than 4 @s in its perimiter, so a new state needs to be saved
    - then run again on the new state and see how many @ still exist with less than 4 @s in its perimiter and remove those
    - rinse repeat, until all existing @s do NOT have less than 4 @s in its perimiter
    
    Note: for some reasons I made a perimiter function of variable size as I tried to predict that part 2 would go in this direction, alas, it did not :-)

## 2025.12.09

[Day 5 Part 1](https://adventofcode.com/2025/day/5) solved using Excel 365 ~~python (3.14.2)~~

    Steps used:
    - copy-paste transpose the first block (interval classes) into a very long 174-Cell row
    - split every interval class into values (formulas used TEXTSPLIT, and VALUE)
    - copy-paste the second block into a column
    - on every cell in the table created by the row and the column query if the value of the column is found on the row above (formulas used IF, and AND), of found return 1, if not return empty
    - add a second column before the table that will add each row (formulas used SUM)
    - at the top of this last column add the sum of all non zero values in this column (Formulas used COUNTIF)

    Note: super easy barely an inconvinience

    I still want to try and solve it with python thou...
    
## 2025.12.10

[Day 5 Parts 1 and 2](https://adventofcode.com/2025/day/5) solved using python (3.14.2)

    I had technically solved this y-day. I wrote two different merge interval code pieces, the first starting from the end and popping the intervals from the intervals' list as they were being processed, and the second starting from the beginning and adding new elements to a new merged intervals' list. The end result is the same, but for some reason yesterday I may have copied the wrong number... I needed 6 submissions to get Day 5 part 2 right. 

    Steps used:
    - read input.txt
    - input.txt has two blocks separated by a blank line, the first block contains the ruleset, that is, each line specifies classes of numbers, and the second block contains a sequence of numbers that we check against the classes, if the number does not fit any class, it is discarded. Some numbers may fit more than one class. Also, some classes overlap, so there is room for optmization, reducing the number of passes later on.
    - load up the classes form the first block into a list and create a new list of merged classes
    - parse the second block against each of classes in the second block, and break the loop on the first confirmation
    - add the total number of confirmations... to 874
    
    As for part 2...
    - since I had already did the interval class overlap consolidation, now I had only to iterate through all merged classes and sum their respective sizes
    
    Note: I had to design a different demo to catch all edge cases in this merge consolidation code
    
    1-5
    3-12
    4-8
    9-11
    14-21
    20-25
    16-17
    15-18
    13-19
    
    1
    5
    8
    11
    17
    32

[Day 6 Part 1](https://adventofcode.com/2025/day/6) solved using python (3.14.2)

    I figure I could rip thru this one in MSExcel but I believed if I did this in python, I could adapt the code easily for part 2. Spoiler alert, part 2 is basically a whole new problem :(
    
    Steps used:
    - read input file and parse each line into lists using a variable number of empty spaces as dividers
    - there could be any number of lines in the file and thousands of values
    - the last line contains symbols that dictate either the sum or product of the previous lines
    - first I remove all spaces until I have just values which are placed into a list as int
    - then a result vector is created to hold the operation until Σ summations and Π products are carried out
    - the answer to Part 1 is to tally up all operations

## 2025.12.10

[Day 6 Part 2](https://adventofcode.com/2025/day/6) solved using python (3.14.2)

    Steps used:
    
    - of course part 2 had to be completely different to part 1... much code to be trashed, much waste
    - now srlsy, read the same input file
    - the last line contains symbols that dictate either the Σ summations and Π products
    - this time around we have to Σ and Π operations in blocks, each block can have 2 or 3 columns (maybe more?) and is limited by an empty column, non empty columns contain the values which are written vertically
    - my intuition here is "rotate 90deg clockwise" each digit for each column and then execute the operation
    - this time I will over engineer this by working with a transposed list, because, why not
    - the answer to part 2 is to tally up all operations

    _This has been my favorite challenge so far. It was not particularly difficult, but I enjoyed it very much_
