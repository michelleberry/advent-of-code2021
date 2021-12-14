from collections import Counter

def main():
    # read in input 
    file = open('14_data.txt', 'r')
    lines = file.readlines()

    poly = lines[0].strip()
     
    # Rules for subsitution
    subs = {}
    # Pair: (to Insert)

    for line in lines[2:]:
        ss = line.strip().split(" -> ")
        subs[ss[0]] = ss[1]
    
    steps = 10
    for i in range(steps):
        newpoly = list(poly)
        ins = 0
        for j in range(len(poly)-1):
            pair = poly[j:j+2]
            if pair in subs:
                newpoly.insert(j+1+ins, subs[pair])
                ins += 1
        poly = ''.join(newpoly)
        print("After step {st}: {p}".format(st = i+1, p = poly))

    c = Counter(newpoly)
    cc = c.most_common()
    maxs = cc[0]
    mins = cc[-1]
    print(poly)
    print(cc)
    print(maxs)
    print(mins)
    score = maxs[1] - mins[1]
    print(score)

if __name__ == "__main__":
    main()