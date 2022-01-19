def floyd(graph: list) -> None:
    for k in range(1, 5):
        graph[k][k] = 0

    for k in range(1, 5):
        for i in range(1, 5):
            for j in range(1, 5):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


def printGraph(graph: list) -> None:
    print()
    print("", end="\t")
    for i in range(1, 5):
        print(i, end="\t")
    print()
    print()
    for a in range(1, len(graph)):
        print(a, end="\t")
        for b in range(1, len(graph[0])):
            print(graph[a][b], end="\t")
        print()
    print()


def main():
    graph = [[float("inf") for x in range(5)] for y in range(5)]
    graph[1][4] = 5
    graph[1][2] = 3
    graph[2][1] = 2
    graph[2][4] = 4
    graph[3][2] = 1
    graph[4][3] = 2
    printGraph(graph)

    print()

    floyd(graph)

    printGraph(graph)


if __name__ == '__main__':
    main()
