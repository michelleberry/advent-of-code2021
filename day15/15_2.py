DIRS = [(0,1), (1,0), (-1,0), (0,-1)]

def get_score(x, y, w, l, rawgrid, scores):
    least = 99999
    # check the risk to go in either direction, and find which direction is least risky
    for a,b in DIRS:
        nx = a + x
        ny = b + y
        if nx > -1 and nx < w and ny > -1 and ny < l:
            # the addition is the risk to enter the node in that direction plus the total risk in the path 
            least = min(least, rawgrid[ny][nx] + scores[ny][nx])
    return least
        
def print_grid(grid):
    for line in grid:
        for c in line:
            print(c, end='')
        print()
    print()

def main():
    # read in input 
    file = open('15_data.txt', 'r')
    lines = file.readlines()

    rawgrid = [[int(x) for x in list(line.strip())] for line in lines]
    l = len(rawgrid)
    w = len(rawgrid[0])

    el = l*5
    ew = w*5
    expandedgrid = [[0 for x in range(ew)] for y in range(el)]
    # expand grid right first 
    for y in range(l):
        for x in range(ew):
            if x < w:
                expandedgrid[y][x] = rawgrid[y][x]
            else: 
                new = expandedgrid[y][x-w] + 1 
                expandedgrid[y][x] = new if new < 10 else 1
    
    # expand grid down
    for y in range(l, el):
        for x in range(ew):
            new = expandedgrid[y-l][x] + 1
            expandedgrid[y][x] = new if new < 10 else 1

    #print_grid(expandedgrid)

    risk_scores = [[99999 for x in range(ew)] for x in range(el)]
    risk_scores[el-1][ew-1] = 0

    updates = True

    # the risk score at each location is the total risk of the least risky path from bottom right corner to that location
    while updates:
        # if the risk scores were updated we should loop through again and check if we can update other risk scores as a result
        updates = False
        for y in range(el-1, -1, -1):
            for x in range(ew-1, -1, -1):
                prev_scr = risk_scores[y][x]
                scr = min(get_score(x, y, ew, el, expandedgrid, risk_scores), prev_scr)
                
                if scr != prev_scr:
                    risk_scores[y][x] = scr
                    updates = True              
        

    print(risk_scores[0][0])

if __name__ == "__main__":
    main()