
def print_grid(grid):
    for line in grid:
        print(line)

def  main():
    file = open('9_data.txt', 'r')
    lines = file.readlines()
    grid = [[int(x) for x in list(line.strip())] for line in lines]

    print_grid(grid)

    w = len(grid[0])
    l = len(grid)

    low_pts = []
    for y in range(l):
        for x in range(w):
            check = []
            if x > 0:
                check.append(grid[y][x-1])
            if x < w-1:
                check.append(grid[y][x+1])
            if y > 0:
                check.append(grid[y-1][x])
            if y < l-1:
                check.append(grid[y+1][x])

            point = grid[y][x]
            yes = True
            # you need to ensure all nums in check are higher than the point.
            for a in check:
                if a <= point:
                    yes = False
            
            if yes:
                low_pts.append(point)


    print(low_pts)
    print(sum(low_pts) + len(low_pts))

if __name__ == "__main__":
    main()