

def main():
    file = open('6_data.txt', 'r')
    line = file.readline()
    fish = [int(x) for x in line.split(',')]
    days = 80
    sols = [0 for i in range(days)]
    
    d = 0
    while d < days:
        i = 0
        add = 0
        while i < len(fish):
            if fish[i] == 0:
                fish[i] = 6
                add += 1
            else:
                fish[i] -= 1
            i += 1
        for i in range(add):
            fish.append(8)
        sols[d] = len(fish)
        d += 1
    
    print(sols)



if __name__ == "__main__":
    main()