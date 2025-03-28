# ----- 선언 부분 -----
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order (node) :

    # 루트 노드
    print(node. data, end='')
    
    # 왼쪽에 배치되어있는 노드
    if node. left_node != '.':
        pre_order (tree[node.left_node])
    
    # 오른쪽에 배치되어있는 노드
    if node.right_node != '.':
        pre_order (tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order (node):

    # 왼쪽에 배치되어있는 노드
    if node.left_node != '.':
        in_order (tree[node. left_node])

    # 루트 노드
    print(node. data, end='')

    # 오른쪽에 배치되어있는 노드
    if node. right_node != '.':
        in_order (tree[node. right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):

    # 왼쪽에 배치되어있는 노드
    if node.left_node != '.':
        post_order (tree[node.left_node])

    # 오른쪽에 배치되어있는 노드
    if node.right_node != '.':
        post_order (tree[node.right_node])
    
    # 루트 노드
    print(node.data, end='')


# ----- 문제 해결 부분 -----
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node (data, left_node, right_node)

pre_order (tree['A'])
print()
in_order (tree['A'])
print()
post_order (tree['A'])
print()