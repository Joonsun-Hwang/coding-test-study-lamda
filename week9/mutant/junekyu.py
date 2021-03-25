
from collections import deque


class Node:
    def __init__(self, value, size, is_root=False):
        self.value = value
        self.children = [None] * size
        self.is_root = is_root
        self.leaf = False
        self.fail = None
        self.out = None

    def __setitem__(self, i, item):
        self.children[i] = item

    def __getitem__(self, i):
        return self.children[i]


def struct_trie(markers):
    size = 4
    root = Node(None, size, is_root=True)
    for marker in markers:
        node = root
        for c in marker:
            i = "ACGT".find(c)
            if not node[i]:
                node[i] = Node(c, size)
            node = node[i]
        node.leaf = True

    # parse backward edges
    q = deque()
    q.append(root)
    while q:
        item = q.popleft()
        for i in range(len(item.children)):
            if not item[i]:
                continue
            prev_item = item
            cur_item = item[i]

            while 1:
                if prev_item.is_root:
                    cur_item.fail = prev_item
                    break
                if prev_item.fail[i]:
                    cur_item.fail = prev_item.fail[i]
                    break
                prev_item = prev_item.fail
            q.append(cur_item)
        if item.is_root:
            continue
        elif item.leaf:
            item.out = item
        elif item.fail.out:
            item.out = item.fail.out

    return root


def get_markers(m, marker):
    markers = set()
    for right in range(m):
        for left in range(right + 1):
            left_marker = marker[0:left]
            mid_marker = marker[left:right + 1]
            right_marker = marker[right + 1:m]
            markers.add(left_marker + mid_marker[::-1] + right_marker)

    return list(markers)


def solution(n, m, DNA, marker):

    #  answer = 0
    markers = get_markers(m, marker)
    trie = struct_trie(markers)

    index = 0
    count = 0
    while index <= len(DNA):
        if trie.out:
            count += 1
        if index == len(DNA):
            break
        c = "ACGT".find(DNA[index])
        if trie[c]:
            trie = trie[c]
            index += 1
            continue
        if trie.is_root:
            index += 1
            continue
        else:
            trie = trie.fail
    return count


def main():

    T = input()
    for _ in range(int(T)):
        n_m = input()
        n, m = n_m.split(' ')
        DNA = input()
        marker = input()
        print(solution(int(n), int(m), DNA, marker))


if __name__ == "__main__":
    main()

