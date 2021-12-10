def main():

    file1 = open('3_data.txt', 'r')
    lines = file1.readlines()
    slines = [line.strip() for line in lines]
    n = len(slines[0])

    ones = [0 for i in range(n)]
    zeros = [0 for i in range(n)]
    
    for line in slines:
        for i, c in enumerate(line):
            if c == '0':
                zeros[i] += 1
            elif c == '1':
                ones[i] += 1
            
    
    gamma = 0
    epsilon = 0

    for i in range(n):
        p = n-i-1
        if ones[i] > zeros[i]:
            gamma += 2**p
        elif ones[i] < zeros[i]: 
            epsilon += 2**p

    print(gamma*epsilon)
    print("gamma: ", gamma)
    print("epsilon: ", epsilon)


if __name__ == "__main__":
    main()
