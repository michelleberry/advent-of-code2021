

def main():
    file1 = open('3_data.txt', 'r')
    lines = file1.readlines()
    slines = [line.strip() for line in lines]
    n = len(slines[0])

    oxy_gen = get_oxygen_generator_rating(slines, n)
    print(oxy_gen)
    c02_scrub = get_c02_scrubber_rating(slines, n)
    print(c02_scrub)

    print(oxy_gen*c02_scrub)

def bin_to_dec(string, n):
    num = 0
    for i in range(n):
        if string[i] == '1':
            num += 2**(n-i-1)
    return num

def get_ones_zeros_counts(things, n):
    ones = [0 for i in range(n)]
    zeros = [0 for i in range(n)]
    
    for line in things:
        for i in range(n):
            if line[i] == '0':
                zeros[i] += 1
            elif line[i] == '1':
                ones[i] += 1
    
    return ones, zeros
            
# things is list of strings
# n is the length of each string
def get_oxygen_generator_rating(things, n):
    ones, zeros = get_ones_zeros_counts(things, n)

    pos = 0
    while len(things) > 1 and pos < n:
        t = '0'
        if ones[pos] >= zeros[pos]:
            t = '1'
        # the lambda function returns True for even numbers 
        filtered_things_iterator = filter(lambda x: (x[pos] == t), things)

        # converting to list
        things = list(filtered_things_iterator)
        pos += 1
        print(things)
        ones, zeros = get_ones_zeros_counts(things, n)

    return bin_to_dec(things[0], n)

# things is list of strings
# n is the length of each string
def get_c02_scrubber_rating(things, n):
    ones, zeros = get_ones_zeros_counts(things, n)

    pos = 0
    while len(things) > 1 and pos < n:
        t = '0'
        if ones[pos] < zeros[pos]:
            t = '1'
        # the lambda function returns True for even numbers 
        filtered_things_iterator = filter(lambda x: (x[pos] == t), things)

        # converting to list
        things = list(filtered_things_iterator)
        pos += 1
        print(things)
        ones, zeros = get_ones_zeros_counts(things, n)

    return bin_to_dec(things[0], n)


if __name__ == "__main__":
    main()
