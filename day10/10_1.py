from collections import deque
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
    for line in slines:
        print(line)

    
    score = 0
    # find first illegal character in each line
    for line in slines:
        dq = deque()
        for c in line:
            if c in pairs:
                dq.appendleft(c)
            elif pairs[dq.popleft()] != c:
                    # get score for illegal char
                    score += points[c]
                    break
    print(score)



if __name__ == "__main__":
    main()