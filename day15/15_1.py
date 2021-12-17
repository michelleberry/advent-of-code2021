DIRS = [(0,1), (1,0), (-1,0), (0,-1)]

def get_score(x, y, w, l, rawgrid, scores):
    least = 999
    for a,b in DIRS:
        nx = a + x
        ny = b + y
        if nx > -1 and nx < w and ny > -1 and ny < l:
            least = min(least, rawgrid[ny][nx] + scores[ny][nx])
    return least
        
def print_grid(grid):
    for line in grid:
        for c in line:
            print(c, end=' ')
        print()
    print()

def main():
    # read in input 
    file = open('15_test.txt', 'r')
    lines = file.readlines()

    rawgrid = [[int(x) for x in list(line.strip())] for line in lines]
    l = len(rawgrid)
    w = len(rawgrid[0])

    risk_scores = [[999 for x in range(w)] for x in range(l)]
    risk_scores[l-1][w-1] = 0

    updates = True

    while updates:
        updates = False
        for y in range(l-1, -1, -1):
            for x in range(w-1, -1, -1):
                prev_scr = risk_scores[y][x]
                scr = min(get_score(x, y, w, l, rawgrid, risk_scores), prev_scr)
                
                if scr != prev_scr:
                    risk_scores[y][x] = scr
                    updates = True
        print_grid(risk_scores)               
        

    print(risk_scores[0][0])



if __name__ == "__main__":
    main()