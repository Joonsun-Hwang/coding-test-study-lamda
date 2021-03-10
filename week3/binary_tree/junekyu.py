#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def solution(nodeinfo):

    # preprocessing
    nodeinfo_dict = {}
    for i, node in enumerate(nodeinfo):
        nodeinfo_dict[i + 1] = node
    sorted_nodes = sorted(nodeinfo_dict.items(), key=lambda k: k[1][1], reverse=True)

    tree = make_tree(sorted_nodes)

    priors = prior(tree)

    posts = post(tree)
    answer = [priors, posts]

    return answer


def prior(tree):
    traversal = []
    stack = []
    stack.append(tree.root)
    while stack:
        node = stack.pop()
        traversal.append(node.index)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return traversal


def post(tree):
    traversal = []
    post_stack = []
    stack = []
    stack.append(tree.root)
    while stack:
        peek = stack[-1]
        node = stack.pop()
        post_stack.append(peek.index)
        if peek.left:
            stack.append(peek.left)
        if peek.right:
            stack.append(peek.right)
    while post_stack:
        node = post_stack.pop()
        traversal.append(node)

    return traversal


def make_tree(nodeinfo):

    bt = BinaySearchTree()

    for node in nodeinfo:
        bt.insert(node)

    return bt


class BinaySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, node):
        node = Node(node)
        if self.root == None:
            self.root = node
        else:
            sub_root = self.root
            while sub_root:
                if node.y < sub_root.y:
                    if node.x < sub_root.x:
                        if sub_root.left:
                            sub_root = sub_root.left
                        else:
                            sub_root.left = node
                            sub_root = None
                    else:
                        if sub_root.right:
                            sub_root = sub_root.right
                        else:
                            sub_root.right = node
                            sub_root = None
                else:
                    print("new node have bigger y.")
        return self.root


class Node(object):
    def __init__(self, node):
        self.index = node[0]
        self.x = node[1][0]
        self.y = node[1][1]
        self.left = self.right = None


def main():
    nodeinfo = [
        [5, 3],
        [11, 5],
        [13, 3],
        [3, 5],
        [6, 1],
        [1, 3],
        [8, 6],
        [7, 2],
        [2, 2],
    ]
    answer = solution(nodeinfo)
    print(answer)
    # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]


if __name__ == "__main__":
    main()
