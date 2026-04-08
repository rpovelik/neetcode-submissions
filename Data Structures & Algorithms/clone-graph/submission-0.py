"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stack = []
        old_to_new = {}
        old_to_new[node] = Node(node.val, [])
        stack.append(node)

        while stack:
            current = stack.pop()
            copy = old_to_new[current]

            for nei in current.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val, [])
                    stack.append(nei)

                copy.neighbors.append(old_to_new[nei])
        
        return old_to_new[node]
