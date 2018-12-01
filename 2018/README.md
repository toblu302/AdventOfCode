## AoC 2018
These solutions for Advent of Code 2018 are written in X86-64 assembly, with help from the C standard library.

### Structure
Each day has its own folder, with the solutions for part 1 and 2 placed in the files part1.s and part2.s. My input for any given day is located in the file named "input". Each solution read from standard input and print out the answer to standard output. Use pipes to pass the input to the program, i.e "./part1 < input".

### Compile and run
* nasm -felf64 part1.s && gcc part1.o -o part1
* nasm -felf64 part2.s && gcc part2.o -o part2

### Benchmarks
TBA
