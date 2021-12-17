# lazy hex conversion
hex = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

# convert binary to decimal
def bin_to_dec(string, n):
    num = 0
    for i in range(n):
        if string[i] == '1':
            num += 2**(n-i-1)
    return num

# dont make fun of the name of this i couldnt think of one okay
def munch(str, num):
    # cut off and return first num chars
    ret = str[:num]
    str = str[num:]
    return str, ret

# recursive function
def parse_bits(binstr):
    if len(binstr) < 11 and bin_to_dec(binstr, len(binstr)) == 0:
        binstr = ''
        return binstr, None

    binstr, version = munch(binstr, 3)
    binstr, typestr = munch(binstr, 3)
    
    t = bin_to_dec(typestr, 3)

    if t == 4:
        # parse numeric number and return it
        binstr, more = munch(binstr, 1)
        total = ''
        while more == '1':
            binstr, x = munch(binstr, 4)
            total += x
            binstr, more = munch(binstr, 1)
        binstr, x = munch(binstr, 4)
        total += x

        num = bin_to_dec(total, len(total))
        return binstr, num
    else:
        binstr, id = munch(binstr, 1)
        nums = []
        # get the numbers with which to operate on s
        if id == '0':
            # we know exactly how much bits is the subpacket
            binstr, subpkts = munch(binstr, 15)
            spks = bin_to_dec(subpkts, 15)

            binstr, subbinstr = munch(binstr, spks)

            while len(subbinstr) != 0:
                subbinstr, num = parse_bits(subbinstr)
                if num != None:
                    nums.append(num)
        elif id == '1':
            # we know how many packets are subpackets of this
            binstr, numsubpkt = munch(binstr, 11)
            n = bin_to_dec(numsubpkt, 11)
            for i in range(n):
                binstr, num = parse_bits(binstr)
                if num != None:
                    nums.append(num)
        
        if t == 0:
            #sum packet
            return binstr, sum(nums)
        elif t == 1:
            #product packet
            prod = 1
            for num in nums:
                prod *= num
            return binstr, prod
        elif t == 2:
            # minimum
            return binstr, min(nums)
        elif t == 3:
            # maximum
            return binstr, max(nums)
        elif t == 5:
            # greater than
            if nums[0] > nums[1]:
                return binstr, 1
            return binstr, 0
        elif t == 6:
            # less than
            if nums[0] < nums[1]:
                return binstr, 1
            return binstr, 0
        elif t == 7:
            if nums[0] == nums[1]:
                return binstr, 1
            return binstr, 0

def main():
    # read in input 
    file = open('16_data.txt', 'r')
    lines = file.readlines()

    hexstr = list(lines[0].strip())

    binstr = ''
    for c in hexstr:
        binstr += hex[c]

    print("this string evaluates to: {}".format(parse_bits(binstr)[1]))


if __name__ == "__main__":
    main()