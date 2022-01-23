def main():
    graph = [[0 for x in range(4)] for y in range(4)]
    graph[0][0] = 1
    graph[2][1] = 1
    graph[3][2] = 1
    graph[1][3] = 1
    for x in graph:
        for y in x:
            print('{:4}'.format(y), end=" ")
        print()


if __name__ == '__main__':
    main()
