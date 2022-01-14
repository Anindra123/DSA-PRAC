# dijkstra algorithm

def dijkstra(graph, start, end):
    queue = []
    visited = []
    distance = {x: float('inf') for x in graph}
    came_from = {}
    distance[start] = 0
    queue.append([start, distance[start]])
    came_from[start] = None
    while queue:
        curr_node = queue.pop(0)
        visited.append(curr_node[0])
        if curr_node[0] is end:
            break
        for neigh in graph[curr_node[0]]:
            if neigh[0] not in visited:
                temp_dist = curr_node[1] + neigh[1]
                if temp_dist < distance[neigh[0]]:
                    distance[neigh[0]] = temp_dist
                    queue.append([neigh[0], distance[neigh[0]]])
                    queue.sort(key=lambda x: x[1])
                    came_from[neigh[0]] = curr_node[0]

    node_in_order = []
    node_in_order.append(end)
    prev_node = came_from[end]
    while prev_node is not None:
        node_in_order.append(prev_node)
        prev_node = came_from[prev_node]

    node_in_order.reverse()
    for node in node_in_order:
        if node is end:
            print(node, end="=>None")
            break
        print(node, end="=>")
    # print(distance)


def main():
    graph = {
        'A': [['B', 4], ['C', 4]],
        'B': [['A', 4], ['C', 2]],
        'C': [['A', 4], ['B', 2], ['D', 3], ['E', 1], ['F', 6]],
        'D': [['C', 3], ['F', 2]],
        'E': [['C', 1], ['F', 3]],
        'F': [['C', 6], ['D', 2], ['E', 3]]
    }
    dijkstra(graph, 'A', 'F')
    # q = []
    # q.append(['1', 5])
    # q.append(['2', 10])
    # q.append(['3', 2])
    # q.append(['4', 1])
    # q.sort(key=lambda x: x[1])
    # print(q)


if __name__ == '__main__':
    main()
