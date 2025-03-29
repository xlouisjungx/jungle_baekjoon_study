class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # 삽입 (재귀적으로 수행)
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    # 검색
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # 최소값 찾기 (가장 왼쪽 노드)
    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.key if current else None

    # 최대값 찾기 (가장 오른쪽 노드)
    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.key if current else None

    # 중위 순회 (오름차순 정렬)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)