from collections import deque

def print_grid(grid):
    for line in grid:
        print(line)

def bfs(grid, x, y, w, l, visited):
    size = 0

    queu = deque()
    queu.appendleft([x,y])

    while queu:
        pp = queu.popleft()
        x = pp[0]
        y = pp[1]
        
        if grid[y][x] != 9 and pp not in visited:
            size += 1
            if y < l-1:
                queu.appendleft([x,y+1])
            if y > 0:
                queu.appendleft([x,y-1])
            if x < w-1:
                queu.appendleft([x+1,y])
            if x > 0:
                queu.appendleft([x-1,y])
            visited.append(pp)
    return size

def  main():
    file = open('9_data.txt', 'r')
    lines = file.readlines()
    grid = [[int(x) for x in list(line.strip())] for line in lines]

    print_grid(grid)

    w = len(grid[0])
    l = len(grid)

    # basically u gonna count areas bordered by 9's
    # we store the size of each basin in this array
    basins = []
    visited = []
    
    for y in range(l):
        for x in range(w):
            basin = bfs(grid, x, y, w, l, visited)
            if basin != 0:
                basins.append(basin)
                
    basins.sort()
    score = 1
    for b in basins[-3:]:
        score = score * b

    print(score)
    

if __name__ == "__main__":
    main()