from collections import deque
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

pairs = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

def main():
    file = open('10_data.txt', 'r')
    lines = file.readlines()
    slines = [[c for c in line.strip()] for line in lines]

    scores = []
    
    # find first illegal character in each line
    for line in slines:
        dq = deque()
        corrupt = False
        for c in line:
            if c in pairs.keys():
                dq.appendleft(c)
            elif c in pairs.values() and pairs[dq.popleft()] != c:
                corrupt = True
        
        # find missing chars needed to complete incomplete lines
        if not corrupt and dq:
            completer = []
            score = 0
            while(dq):
                score *= 5
                toAdd = pairs[dq.popleft()]
                completer.append(toAdd)
                score += points[toAdd]
                
            scores.append(score)

    scores.sort()
    mid = len(scores)//2
    print(scores[mid])
                
            



if __name__ == "__main__":
    main()
