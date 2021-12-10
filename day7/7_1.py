
def main():
    file = open('7_data.txt', 'r')
    line = file.readline()
    crabs = [int(x) for x in line.split(',')]
    
    crabs.sort()
    mid = crabs[len(crabs)//2]

    fuel = 0
    for c in crabs:
        fuel += abs(c - mid)

    print(mid)
    print(fuel)

if __name__ == "__main__":
    main()