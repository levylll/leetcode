class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        p = None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    if not res:
                        res = l1
                        p = res
                    else:
                        p.next = l1
                        p = p.next
                    l1 = l1.next
                else:
                    if not res:
                        res = l2
                        p = res
                    else:
                        p.next = l2
                        p = p.next
                    l2 = l2.next
            elif l1:
                if not res:
                    res = l1
                    p = res
                else:
                    p.next = l1
                    p = p.next
                l1 = l1.next
            elif l2:
                if not res:
                    res = l2
                    p = res
                else:
                    p.next = l2
                    p = p.next
                l2 = l2.next

        return res




