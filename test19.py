class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = None
        target = None
        remain = 0
        p = head
        while p:
            if remain >= n-1:
                if target:
                    pre = target
                    target = target.next
                else:
                    target = head
            p = p.next
            remain += 1
        if not pre:
            return head.next
        else:
            pre.next = target.next
            return head

a = [1,2,3,4,5]
n = 2

head = None
p = None
for x in a:
    if head:
        p.next = ListNode(x)
        p = p.next

    else:
        head = ListNode(x)
        p = head

s = Solution()
res = s.removeNthFromEnd(head, n)
while res:
    print(res.val)
    res = res.next



