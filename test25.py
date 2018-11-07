class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head, n):
        p = head
        k = n
        nh = None
        while k >= 1 and p:
            k -= 1
            p = p.next

        if k == 0:
            p = head
            np = None
            k = n
            while p and k > 0:
                k -= 1
                if not np:
                    np = p
                    nh = p
                    p = p.next
                else:
                    tmp = p.next
                    p.next = nh
                    nh = p
                    p = tmp
            np.next = self.reverse(p, n)
        return nh if nh else head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        return self.reverse(head, k)

a = [1,2,3,4,5]
k = 2
head = None
p = None
for x in a:
    if not head:
        head = ListNode(x)
        p = head
    else:
        p.next = ListNode(x)
        p = p.next

s= Solution()
res = s.reverseKGroup(head, k)

print('=========')
p = res
while p:
    print(p.val)
    p = p.next


