def main():
    file = open('8_data.txt', 'r')
    lines = file.readlines()

    uniq = 0

    for line in lines:
        inputs = line.strip().split(' | ')[1].split(' ')
        for i in inputs:
            l = len(i)
            if l == 2 or l == 3 or l == 4 or l == 7:
                uniq += 1

    print(uniq)

    file.close()
    

if __name__ == "__main__":
    main()