from collections import Counter 

global_nums = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

def decode(lets):
    # letter as it appears : true letter
    mapp = {}

    # facts
    # b shows up 6 times in 0-9
    # e shows up 4 times in 0-9
    # f shows up 9 times in 0-9
    # a and c show up 8 times in 0-9
    # d and g show up 7 times in 0-9
    count_map = Counter(''.join(lets))
    for c, v in count_map.items():
        if v == 4:
            mapp[c] = 'e'
        elif v == 6:
            mapp[c] = 'b'
        elif v == 9:
            mapp[c] = 'f'
    
    # so now we know what e, b, f are and we can use this to find the rest of the letters
    # get 1
    onestr = filter(lambda x: len(x) == 2, lets)
    for l in onestr[0]:
        if l not in mapp:
             mapp[l] = 'c'

    # we now have e, b, f, c. we can get a and d in a similar fashion from 4 and 7.
    fourstr = filter(lambda x: len(x) == 4, lets)
    for l in fourstr[0]:
        if l not in  mapp:
             mapp[l] = 'd'

    sevenstr = filter(lambda x: len(x) == 3, lets)
    for l in sevenstr[0]:
        if l not in mapp:
             mapp[l] = 'a'

    # one letter left, Whatever isn't in the mapping already is g.
    for c in ''.join(lets):
        if c not in  mapp:
            mapp[c] = 'g'
            return mapp

def convert_to_nums(lets, maps):
    num = ''
    for s in lets:
        ms = ''
        for c in s:
            ms += maps[c]
        mss = ''.join(sorted(ms))
        num += global_nums[mss]
    print(num)
    return int(num)

def main():
    file = open('8_data.txt', 'r')
    lines = file.readlines()

    summ = 0

    for line in lines:
        s = line.strip().split(' | ')
        ri = s[0].split(' ')
        le = s[1].split(' ')
        
        mappings = decode(ri)
        print(mappings)
        number = convert_to_nums(le, mappings)
        summ += number



    print(summ)

    file.close()
    

if __name__ == "__main__":
    main()