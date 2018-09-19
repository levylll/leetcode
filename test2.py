# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        p = None
        flag = 0
        while(l1 and l2):
            tmp = l1.val + l2.val + flag
            flag = 0
            if p == None:
                p = res
            else:
                p.next = ListNode(0)
                p = p.next
            if tmp >= 10:
                p.val = tmp - 10
                flag = 1
            else:
                p.val = tmp
            l1 = l1.next
            l2 = l2.next

        while l1:
            tmp = l1.val + flag
            if p == None:
                p = res
            else:
                p.next = ListNode(0)
                p = p.next
            if tmp == 0:
                break
            elif tmp >= 10:
                p.val = tmp - 10
                flag = 1
            else:
                p.val = tmp
                flag = 0
            l1 = l1.next
        while l2:
            tmp = l2.val + flag
            if p == None:
                p = res
            else:
                p.next = ListNode(0)
                p = p.next
            if tmp == 0:
                break
            elif tmp >= 10:
                p.val = tmp - 10
                flag = 1
            else:
                p.val = tmp
                flag = 0
            l2 = l2.next
        if flag:
            p.next = ListNode(flag)
        return res

def gen_num_ListNode(num):
    num = str(num)
    p = None
    for x in range(len(num),0, -1):
        if p:
            p.next = ListNode(int(num[x-1]))
            p = p.next
        else:
            l = ListNode(int(num[x-1]))
            p = l
    return l

def gen_res(l):
    print '============'
    while l:
        print l.val
        l = l.next

if __name__ == '__main__':
    l1 = gen_num_ListNode(1)
    l2 = gen_num_ListNode(99)
    gen_res(l1)
    gen_res(l2)
    s = Solution()
    s.addTwoNumbers(l1, l2)
    gen_res(s)

