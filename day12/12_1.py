dirs = [(0,1), (0,-1), (1,0), (-1,0), 
        (1,1), (1, -1), (-1, 1), (-1,-1)]

from colorama import Fore, Style
from collections import deque

def add_to_graph(graph, a, b):
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

def print_paths(paths):
    for path in paths:
        print(path)

def dfs(graph, path):
    total_paths = 0
    tip = path[-1]
    
    for nod in graph[tip]:
        newpath = path.copy()
        if nod == 'end':
            newpath.append(nod)
            print(newpath)
            total_paths += 1
        elif (nod.islower() and (nod not in path)) or nod.isupper():
            newpath.append(nod)
            total_paths += dfs(graph, newpath)

    return total_paths

def main():
    file = open('12_data.txt', 'r')
    lines = file.readlines()

    # constuct graph as adjacency list
    graph = {}
    for line in lines:
        caves = line.strip().split('-')
        a = caves[0]
        b = caves[1]
        add_to_graph(graph, a, b)
        add_to_graph(graph, b, a)

    print(graph)

    total_paths = dfs(graph, ['start'])
        
    
    print(total_paths)


   

if __name__ == "__main__":
    main()