import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, val, x, y, left=None, right=None):
        self.val = val
        self.x = x
        self.y = y
        self.left = None
        self.right = None


preorder_list = []
postorder_list = []
r_root = None


def make_tree(node_list):
    if node_list:
        root = node_list.pop(0)
        if node_list and (root.x > node_list[0].x) and (root.y > node_list[0].y):
            root.left = make_tree(node_list)
        if node_list and (root.x < node_list[0]):
            root.right = make_tree(node_list)
        return root


def preorder(root):
    if root:
        preorder_list.append(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        postorder_list.append(root.val)


def solution(nodeinfo):
    node_num = 0
    node_list = []
    for n in nodeinfo:
        node_num += 1
        node = Node(node_num, n[0], n[1])  # 노드 번호, x좌표, y좌표
        node_list.append(node)

    node_list.sort(
        key=lambda x: (x.y, -x.x), reverse=True
    )  # y값이 제일 큰게 루트 그다음 차례대로 left,right

    root = None
    for node in node_list:
        if not root:
            root = node
        else:
            current = root
            while True:
                if node.x < current.x:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = node
                        break
                if node.x > current.x:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = node
                        break
                break

    preorder(root)
    postorder(root)

    answer = []
    answer.append(preorder_list)
    answer.append(postorder_list)

    return answer
