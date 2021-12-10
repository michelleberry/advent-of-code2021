
from collections import Counter

def main():
    file = open('6_test.txt', 'r')
    line = file.readline()
    feeesh = [int(x) for x in line.split(',')]
    # keep track of each number of fishes in different states since you know there is only like digits 0-9 and this removes repeated work 
    fish = [feeesh.count(i) for i in range(9)]
    days = 256
    
    for i in range(days):
        # rotate the list
        fish.append(fish.pop(0))
        fish[6] += fish[8]

    
    print(sum(fish))



if __name__ == "__main__":
    main()