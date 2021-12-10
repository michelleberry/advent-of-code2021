from collections import deque

def print_board(board):
    print("----------------------")
    for line in board:
        print(line)
    print("----------------------")

def place_horiz_line(a, b, board):
    
    j = 1 if a[1] < b[1] else -1

    for i in range(a[1], b[1] + j, j):
        board[i][a[0]] += 1

def place_vert_line(a, b, board):
    j = 1 if a[0] < b[0] else -1

    for i in range(a[0], b[0] + j, j):
        board[a[1]][i] += 1


def main():
    # read in vectors
    file = open('5_data.txt', 'r')
    lines = file.readlines()

    a_points = deque()
    b_points = deque()
    max_x = 0
    max_y = 0

    # find board dimensions
    for line in lines:
        pts = line.strip().split(" -> ")
        a = [int(x) for x in pts[0].split(",")]
        b = [int(x) for x in pts[1].split(",")]
        a_points.append(a)
        b_points.append(b)
        max_x = max(max_x, a[0], b[0])
        max_y = max(max_y, a[1], b[1])
    
    board = [[0 for i in range(max_x + 1)] for i in range(max_y + 1)]

    while a_points and b_points:
        a = a_points.popleft()
        b = b_points.popleft()
        # y1 == y2
        if a[1] == b[1]:
            # place vert line
            place_vert_line(a, b, board)
        # x1 == x2
        elif a[0] == b[0]:
            # place horiz line
            place_horiz_line(a, b, board)

    print_board(board)

    danger = 0
    # count numbers in board that are 2 or greater
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if board[i][j] >= 2:
                danger += 1

    print("Dangerous areas: {}".format(danger))
    file.close()

if __name__ == "__main__":
    main()