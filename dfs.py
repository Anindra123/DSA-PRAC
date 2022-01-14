# depth first search algorithm

def dfs(graph, node):
    visited = []
    stack = []
    visited.append(node)
    stack.append(node)

    while stack:
        curr_node = stack.pop()
        print(curr_node, end=" ")
        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


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

    dfs(graph, '1')


if __name__ == '__main__':
    main()
