#两个链表的第一个公共节点
#思路：先计算两个链表长度，然后算差值k，长的链表先走k步

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def GetLength(l):
    if l == None:
        return 0

    cur, cout = l, 0
    while cur:
        cout += 1
        cur = cur.next
    return cout

def FindCommonNode(l1, l2):
    if l1 == None or l2 == None:
        return None
    
    length1 = GetLength(l1)
    length2 = GetLength(l2)
    diff = length1 - length2
    if diff > 0 :
        for _ in range(0, diff):
            l1 = l1.next
    elif diff < 0:
        for _ in range(0, diff):
            l2 = l2.next
    #else 一样长

    #同时遍历
    while l1 != None and l2 != None:
        if l1 == l2:
            return l1
        
        l1 = l1.next
        l2 = l2.next 
    return None


a, b, c, d, e, f, g, h = Node(1), Node(2), Node(
    3), Node(4), Node(5), Node(6), Node(7), Node(8)
l2 = a
l2.next = c
l2.next.next = e
l2.next.next.next = g
l2.next.next.next.next = h

l1 = b
l1.next = d
l1.next.next = f
l1.next.next.next = g
l1.next.next.next.next = h

re = FindCommonNode(l1, l2)
print(re.value)
