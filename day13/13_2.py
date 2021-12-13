from colorama import Fore, Style
from collections import deque
from collections import Counter
import re

def print_paper(grid):
    for row in grid:
        for ch in row:
            print(ch, end='')
        print()
    print()

def fold_left(cord, grid, w, l):
    new_grid = [line[:cord] for line in grid]

    for i in range(l):
        for j in range(cord, w):
            mirror_x = cord - (j - cord)
            if grid[i][j] == '#':
                new_grid[i][mirror_x] = '#'
    
    return new_grid

def fold_up(cord, grid, w, l):
    new_grid = grid[:cord].copy()

    for i in range(cord, l):
        mirror_y = cord - (i - cord)
        for j in range(w):
            if grid[i][j] == '#':
                new_grid[mirror_y][j] = '#'
    
    return new_grid

def fold(dir, cord, grid, w, l):
    if dir == 'y':
        return fold_up(cord, grid, w, l)
    elif dir == 'x':
        return fold_left(cord, grid, w, l)

def main():
    # read in input 
    file = open('13_data.txt', 'r')
    lines = file.readlines()

    xes = []
    yes = []

    instructions = []

    for line in lines:
        xy = line.strip().split(',')
        if len(xy) == 2:
            x = int(xy[0])
            y = int(xy[1])
            xes.append(x)
            yes.append(y)
        elif line != '\n':
            instructions.append(line.strip())

    w = max(xes) + 1
    l = max(yes) + 1

    # place hashes and dots on the paper 
    grid = [['.' for j in range(w)] for i in range(l)]
    for i in range(len(xes)):
        x = xes[i]
        y = yes[i]
        grid[y][x] = '#'

    # print initial paper 
    print_paper(grid)

    # fold
    inst1 = instructions[0]
    # part one was just do the first fold. so you can just break at the end and that would be the difference btween the first question solution and this one
    for inst1 in instructions:
        print("{}:".format(inst1))
        cord = inst1.split('fold along ')[1].split('=')
        dir = cord[0]
        cd = int(cord[1])
        new_paper = fold(dir, cd, grid, w, l)
        print_paper(new_paper)

        # count the dots left 
        dots = 0
        for line in new_paper:
            for char in line:
                if char == '#':
                    dots += 1

        print("{} dots are visible".format(dots))
        grid = new_paper
        l = len(grid)
        w = len(grid[0])

if __name__ == "__main__":
    main()