from collections import deque

class LRUCache:
    class Node:
        def __init__(self, key, val, n, p):
            self.val = val
            self.key = key
            self.prev = p
            self.next = n

    def __init__(self, capacity: int):
        self.cap = capacity
        self.k_to_node = {}
        self.head = self.Node(-1, -1, None, None)
        self.tail = self.Node(-1, -1, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_mru(self, node: Node) -> None:
        mru = self.head.next
        mru.prev = node
        node.next = mru
        node.prev = self.head
        self.head.next = node

    def _pop_lru(self) -> Node:
        lru = self.tail.prev
        self._remove(self.tail.prev)
        return lru


    def get(self, key: int) -> int:
        val = -1

        if key in self.k_to_node:
            node = self.k_to_node[key]
            self._remove(node)
            self._insert_mru(node)
            val = node.val

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.k_to_node:
            node = self.k_to_node[key]
            node.val = value
            self._remove(node)
            self._insert_mru(node)
        else:
            if len(self.k_to_node) == self.cap:
                lru = self._pop_lru()
                del self.k_to_node[lru.key]
            mru = self.Node(key, value, None, None)
            self._insert_mru(mru)
            self.k_to_node[key] = mru

