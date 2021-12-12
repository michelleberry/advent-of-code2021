dirs = [(0,1), (0,-1), (1,0), (-1,0), 
        (1,1), (1, -1), (-1, 1), (-1,-1)]

from colorama import Fore, Style
from collections import deque
from collections import Counter

def add_to_graph(graph, a, b):
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

def print_path(path):
    strpath = ','.join(path)
    print(strpath)

def condition(node, path):
    if node == 'start':
        return False
    if node.isupper():
        return True

    path.append(node)
    path = list(filter(lambda x: x.islower(), path))
    before = len(path)
    after = len(set(path))

    if before > (after+1):
        return False
    return True

def dfs(graph, path):
    total_paths = 0
    tip = path[-1]
    
    for nod in graph[tip]:
        newpath = path.copy()
        if nod == 'end':
            newpath.append(nod)
            print_path(newpath)
            total_paths += 1
        elif condition(nod, path.copy()):
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