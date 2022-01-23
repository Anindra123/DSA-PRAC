class Node:
    def __init__(self, data) -> None:
        self.data: int = data
        self.left_child: Node = None
        self.rigth_child: Node = None


def inorder(n: Node):
    if n is None:
        return
    inorder(n.left_child)
    print(n.data)
    inorder(n.rigth_child)


def preorder(n: Node):
    if n is None:
        return
    print(n.data)
    preorder(n.left_child)
    preorder(n.rigth_child)


def postorder(n: Node):
    if n is None:
        return
    postorder(n.left_child)
    postorder(n.rigth_child)
    print(n.data)


def main():
    n1 = Node(1)
    n1.left_child = Node(12)
    n1.rigth_child = Node(9)
    n1.left_child.left_child = Node(5)
    n1.left_child.rigth_child = Node(6)
    print("Inorder---------------------")
    inorder(n1)
    print("Preorder---------------------")
    preorder(n1)
    print("Postorder---------------------")
    postorder(n1)


if __name__ == '__main__':
    main()
