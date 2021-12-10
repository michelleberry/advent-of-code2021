def main():

    file1 = open('1_1data.txt', 'r')
    lines = file1.readlines()

    nums = [int(line) for line in lines]
    sums = [0 for num in nums]

    tc = -1
    
    for i in range(2, len(nums)):
        sums[i] = nums[i] + nums[i-1] + nums[i-2]
        if sums[i] > sums[i-1]:
            tc += 1
    
            
    print(tc)


if __name__ == "__main__":
    main()
