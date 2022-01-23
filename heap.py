

def heapify(arr, n, idx):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr, n, largest)


def extractMax(arr: list):

    size = len(arr)
    # max element is the root
    max = arr[0]

    # replace root element with the last leaf node
    arr[0], arr[size-1] = arr[size-1], arr[0]

    # remove the swapped element
    arr.remove(arr[size-1])

    # heapify to retain the order of heap
    heapify(arr, len(arr), 0)

    # return the max element
    return max


def shiftUp(arr: list, idx):
    # if current node is greater than zero
    # and the element of current node is greater then parent node
    # swap parent node with current node
    # here parent node = (array index -1) / 2
    while idx > 0 and arr[(idx-1)//2] < arr[idx]:
        arr[(idx-1)//2], arr[idx] = arr[idx], arr[(idx-1)//2]
        idx = (idx-1)//2


def insert(arr: list, num):

    # check whether there is no element to insert
    # if yes insert the element
    if len(arr) == 0:
        arr.append(num)
    else:
        arr.append(num)
        shiftUp(arr, len(arr)-1)


def main():
    # arr = [3, 9, 2, 1, 4, 5]
    # for i in range((len(arr)//2)-1, -1, -1):
    #     heapify(arr, len(arr), i)
    arr = []
    insert(arr, 3)
    insert(arr, 9)
    insert(arr, 2)
    insert(arr, 1)
    insert(arr, 4)
    insert(arr, 5)
    print(arr)
    e1 = extractMax(arr)
    e2 = extractMax(arr)
    print(arr)
    print(e1)
    print(e2)


if __name__ == '__main__':
    main()
