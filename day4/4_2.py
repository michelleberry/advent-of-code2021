from collections import deque
# which bingo board will win LAST?
# what will the final score be for that board?
def main():
    # read in bingo numbers
    file = open('4_data.txt', 'r')
    lines = file.readlines()

    nums = [int(x) for x in lines[0].strip().split(',')]
    nums = deque(nums)

    # read in each bingo board
    b = -1
    r = 0
    boards = []

    n = len(lines)
    for i in range(1, n):
        if lines[i].isspace():
            curBoard = [[] for i in range(5)]
            boards.append(curBoard)
            b += 1
            r = 0
        else:
            boards[b][r] = [int(x) for x in list(filter(lambda x: (x != ''), lines[i].strip().split(' ')))]
            r += 1
    
    print(nums)
    print(boards)
    winning_boards = []
    winning_nums = []
    # loop pulling bingo numbers off of the front of the queue, 
    while nums:
        num = nums.popleft()
        
        # for each board,
        b = 0
        while b < len(boards) - 1:
            for i in range(5):
                for j in range(5):
                    # if the board has the number then mark it,
                    if boards[b][i][j] == num:
                        boards[b][i][j] = 'X'
                        # if you marked it on the board then check if you won
                        if winner(boards[b]):
                            winning_boards.append(boards[b])
                            winning_nums.append(num)
                            del boards[b]
                            b -= 1
            b += 1

    last_win = winning_boards[-1]
    print("Last board to win is ", last_win)
    print("With a score of ", score(last_win, winning_nums[-1]))

def score(board, num):
    sum = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != 'X':
                sum += board[i][j]
    return sum*num

def winner(board):
    # loop through matrix
    for i in range(5):
        rct = 0
        cct = 0
        for j in range(5):
            # check rows
            if board[j][i] == 'X':
                rct += 1
            # check cols
            if board[i][j] == 'X':
                cct += 1
        if rct == 5 or cct == 5:
            return True
    return False
           

if __name__ == "__main__":
    main()