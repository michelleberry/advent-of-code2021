from collections import Counter

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

def add_to_dict(p, v, prs):
    if p in prs:
        prs[p] += v
    else:
        prs[p] = v

def main():
    # read in input 
    file = open('14_data.txt', 'r')
    lines = file.readlines()

    poly = lines[0].strip()
     
    # Rules for subsitution
    # Pair: (to Insert)
    subs = {}
    pairs = {}
    alpha_ct = Counter({ let:0 for let in alphabet})

    # populate pairs
    for i in range(len(poly)-1):
        add_to_dict(poly[i:i+2], 1, pairs)

    # populate alpha_ct
    for let in poly:
        alpha_ct[let] += 1

    # populate subs
    for line in lines[2:]:
        ss = line.strip().split(" -> ")
        subs[ss[0]] = ss[1]
    
    steps = 40
    for i in range(steps):
        newpairs = pairs.copy()
        for k,v in pairs.items():
            if k in subs: 

                let = list(k)
                ins = subs[k]

                p1 = let[0] + ins
                p2 = ins + let[1]

                alpha_ct[ins] += v 
                newpairs[k] -= v

                add_to_dict(p1, v, newpairs)
                add_to_dict(p2, v, newpairs)

        pairs = newpairs

   
    c = alpha_ct
    cc = list(filter(lambda x: x[1] != 0, c.most_common()))
    maxs = cc[0]
    mins = cc[-1]
    print(pairs)
    print(cc)
    print(maxs)
    print(mins)
    score = maxs[1] - mins[1]
    print(score)

if __name__ == "__main__":
    main()