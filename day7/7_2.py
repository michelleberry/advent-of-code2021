
def main():
    file = open('7_data.txt', 'r')
    line = file.readline()
    crabs = [int(x) for x in line.split(',')]
    
    fuels = [0, 1]
    for i in range(2, max(crabs)+1):
        fuels.append(fuels[-1] + i)

    total_fuel_at_m = []
    for meeting_pt in range(0, max(crabs)+1):
        fuel = 0
        for c in crabs:
            dist = abs(c - meeting_pt)
            fuel += fuels[dist]

        total_fuel_at_m.append(fuel)
    
    sol = min(total_fuel_at_m)
    print(total_fuel_at_m.index(sol))
    print(sol)

if __name__ == "__main__":
    main()