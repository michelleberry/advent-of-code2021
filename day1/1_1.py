def main():

    file1 = open('1_1data.txt', 'r')
    lines = file1.readlines()

    nums = [int(line) for line in lines]
    tc = 0
    
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            tc += 1
            
    print(tc)


if __name__ == "__main__":
    main()
