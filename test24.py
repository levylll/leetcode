# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def desp(self, head):
        p = head
        out = []
        while p:
            out.append(p.val)
            p = p.next
        print(out)

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        fake_head.next = head
        p = fake_head
        while p.next and p.next.next:
            tmp_p = p.next
            p.next = p.next.next
            tmp_p.next = p.next.next
            p.next.next = tmp_p
            p = p.next.next
        #self.desp(fake_head)

        return fake_head.next

input = [2,1,4,3]

head = None
p = None
for x in input:
    if not head:
        head = ListNode(x)
        p = head
    else:
        p.next = ListNode(x)
        p = p.next

s = Solution()
res =s.swapPairs(head)

p = res
out = []
while p:
    out.append(p.val)
    p = p.next



