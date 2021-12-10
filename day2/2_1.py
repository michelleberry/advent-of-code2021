def main():

    file1 = open('2_data.txt', 'r')
    lines = file1.readlines()

    hor = 0
    ver = 0
    
    for line in lines:
        d = line.split(" ")
        dir = d[0]
        num = int(d[1])

        if dir == "forward":
            hor += num
        elif dir == "backward":
            hor -= num
        elif dir == "up":
            ver -= num
        elif dir == "down":
            ver += num
            
    print(hor, " ", ver)
    print(hor*ver)


if __name__ == "__main__":
    main()
