import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, node, idx):
        self.x = node[0]
        self.y = node[1]
        self.idx = idx
        
        self.left_child = None
        self.right_child = None
        self.parent = None

class BinaryTree(object):
    def __init__(self):
        self.root_idx = -1
    
    def build_tree(self, nodeinfo):
        node_sorted = sorted(nodeinfo, key=lambda l:l[1], reverse=True) # y값 기준 내림차순 정렬
        self.nodes_xtoi = {coord[0]: i+1 for i, coord in enumerate(nodeinfo)}
        self.nodes_iton = {i+1: None for i, coord in enumerate(nodeinfo)}
        self.root_idx = self.nodes_xtoi[node_sorted[0][0]]
        for n in node_sorted:
            i = self.nodes_xtoi[n[0]]
            self.nodes_iton[i] = Node(n, i)
        
        for c_n in node_sorted:
            current_node = self.nodes_iton[self.nodes_xtoi[c_n[0]]]
            parent_node = current_node.parent
            cand_node = node_sorted
            while parent_node is not None:
                cand_node = [n for n in cand_node
                             if n[1] < current_node.y and
                             (current_node.x > parent_node.x and 
                              n[0] > parent_node.x) or
                             (current_node.x < parent_node.x and
                              n[0] < parent_node.x)]
                parent_node = parent_node.parent
            
            left_cand_node, right_cand_node = [], []
            for n in cand_node:
                if n[0] < current_node.x:
                    left_cand_node.append(n)
                if n[0] > current_node.x:
                    right_cand_node.append(n)
            
            if left_cand_node:
                left_node_x = sorted(left_cand_node, key=lambda l:l[1], reverse=True)[0][0]
                left_node = self.nodes_iton[self.nodes_xtoi[left_node_x]]
                current_node.left_child = left_node
                left_node.parent = current_node
            
            if right_cand_node:
                right_node_x = sorted(right_cand_node, key=lambda l:l[1], reverse=True)[0][0]
                right_node = self.nodes_iton[self.nodes_xtoi[right_node_x]]
                current_node.right_child = right_node
                right_node.parent = current_node
            
    def get_preorder(self):
        preorder = []
        root = self.get_root_node()
        
        def _preorder(root):
            if root is None:
                pass
            else:
                preorder.append(root.idx)
                _preorder(root.left_child)
                _preorder(root.right_child)
        _preorder(root)
        
        return preorder
    
    def get_postorder(self):
        postorder = []
        root = self.get_root_node()
        
        def _postorder(root):
            if root is None:
                pass
            else:
                _postorder(root.left_child)
                _postorder(root.right_child)
                postorder.append(root.idx)
        _postorder(root)
        
        return postorder
    
    def get_root_node(self):
        return self.nodes_iton[self.root_idx]
        

def solution(nodeinfo):
    answer = []
    
    bt = BinaryTree()
    bt.build_tree(nodeinfo)
    
    answer.append(bt.get_preorder())
    answer.append(bt.get_postorder())
    
    return answer
