# breadth first search algorithm

def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        curr_node = queue.pop(0)
        print(curr_node, end=" ")
        for neighbours in graph[curr_node]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)


def main():
    graph = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '4', '7'],
        '4': ['1', '3', '5'],
        '5': ['2', '4', '6'],
        '6': ['5', '7'],
        '7': ['3', '5']
    }
    bfs(graph, '1')


if __name__ == '__main__':
    main()
