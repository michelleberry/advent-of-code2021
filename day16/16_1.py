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

def bin_to_dec(string, n):
    num = 0
    for i in range(n):
        if string[i] == '1':
            num += 2**(n-i-1)
    return num

def munch(str, num):
    # cut off and return first num chars
    ret = str[:num]
    str = str[num:]
    return str, ret

def main():
    # read in input 
    file = open('16_data.txt', 'r')
    lines = file.readlines()

    hexstr = list(lines[0].strip())
    print(hexstr)

    binstr = ''
    for c in hexstr:
        binstr += hex[c]

    version_sum = 0

    while len(binstr) != 0:
        if len(binstr) < 5 and bin_to_dec(binstr, len(binstr)) == 0:
            binstr = ''
            break
        print(binstr)
        binstr, version = munch(binstr, 3)
        binstr, typestr = munch(binstr, 3)
        v = bin_to_dec(version, 3)
        t = bin_to_dec(typestr, 3)
        version_sum += v
        le = 3+3+1
        if t == 4:
            binstr, more = munch(binstr, 1)
            while more == '1':
                le += 5
                binstr, x = munch(binstr, 4)
                binstr, more = munch(binstr, 1)
            binstr, x = munch(binstr, 4)
        else:
            binstr, id = munch(binstr, 1)
            if id == '0':
                binstr, rem = munch(binstr, 15)
                r = bin_to_dec(rem, 15)
            elif id == '1':
                binstr, numsubpkt = munch(binstr, 11)
        



    print(version_sum)


if __name__ == "__main__":
    main()