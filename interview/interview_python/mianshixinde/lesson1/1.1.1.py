#链表反转

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def list_reverse(head):
    if head is None or head.next is None:
        return head
    p, q = head, head.next
    head.next = None
    while q:
        tmp = q.next 
        q.next = p  # 调换指针方向
        p = q       # 移动慢指针到下一个节点
        q = tmp     # 移动快指针到下一个节点

    return p

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

new_list = list_reverse(head)
print(new_list.value, new_list.next.value, new_list.next.next.value, new_list.next.next.next.value)