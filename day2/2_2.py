def main():

    file1 = open('2_data.txt', 'r')
    lines = file1.readlines()

    hor = 0
    dep = 0
    aim = 0
    
    for line in lines:
        d = line.split(" ")
        dir = d[0]
        num = int(d[1])

#         down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

        if dir == "forward":
            hor += num
            dep += aim*num
        elif dir == "backward":
            hor -= num
        elif dir == "up":
            aim -= num
        elif dir == "down":
            aim += num
            
    print(hor, " ", dep)
    print(hor*dep)


if __name__ == "__main__":
    main()
