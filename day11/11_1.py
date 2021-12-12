dirs = [(0,1), (0,-1), (1,0), (-1,0), 
        (1,1), (1, -1), (-1, 1), (-1,-1)]

from colorama import Fore, Style

def print_grid(grid):
    for line in grid:
        for c in line:
            if c == 0:
                print(f'{Style.BRIGHT}{Fore.GREEN}0{Style.RESET_ALL}', end='')
            else:
                print(c, end='')
        print()
    print()


def flash(grid, x, y, w, l, flashed):
    flashed.append((x,y))
    grid[y][x] = 0
    for a, b, in dirs:
        a += x
        b += y
        # if is within the boundaries of the grid
        if a > -1 and b > -1 and a < w and b < l:
            grid[b][a] += 1
            if grid[b][a] > 9:
                flash(grid, a, b, w, l, flashed)
    grid[y][x] = 0
    
def main():
    file = open('11_data.txt', 'r')
    lines = file.readlines()
    grid = [[int(x) for x in list(line.strip())] for line in lines]

    print("Before any steps:")
    print_grid(grid)
    steps = 100
    total_flashes = 0

    w = len(grid[0])
    l = len(grid)

    for i in range(steps):
        flashed = []
        for y in range(l):
            for x in range(w):
                grid[y][x] += 1
                point = grid[y][x] 
                if point > 9:
                    flash(grid, x, y, w, l, flashed)
        for x,y in flashed:
            grid[y][x] = 0
        total_flashes += len(set(flashed))
        print("After step {}:".format(i+1))
        print_grid(grid)
    
    print("Total flashes: {}".format(total_flashes))

            

if __name__ == "__main__":
    main()