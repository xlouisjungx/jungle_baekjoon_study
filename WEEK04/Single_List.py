# 노드 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 연결리스트 생성
# 보통 헤더를 선언하여 연결리스트를 생성하고,
# 헤더를 통해 다른 모든 노드를 탐색하고 참조할 수 있다.
# 따라서, head를 직접 이동시키지 않고, node=head로 head주소를 참조하여 사용한다.
# (원래 헤더는 data를 포함하고 있지 않으며, 헤더의 다음 노드부터 데이터를 가지나 편의상 임의의 값을 넣고 다음 노드부터 사용해도 되고, head노드 부터 사용해도 된다.)

head = ListNode(0)

# 노드 추가(삽입)
#add new_node
curr_node = head

new_node = ListNode(1)
curr_node.next = new_node
curr_node=curr_node.next

curr_node.next = ListNode(2)
curr_node=curr_node.next

curr_node.next = ListNode(3)
curr_node=curr_node.next

curr_node.next = ListNode(4)
curr_node=curr_node.next

# 전체 연결리스트 출력 (탐색)
#print all node
node=head
while node:
    print(node.val)
    node=node.next
''' 출력결과 : 0,1,2,3,4 '''

# 노드 탐색하여 삭제
#delete node by value
node=head
while node.next:
    if node.next.val==2:
        next_node=node.next.next
        node.next=next_node
        break
    node=node.next
    
node=head
while node:
    print(node.val)
    node=node.next
''' 출력결과 : 0,1,3,4 '''