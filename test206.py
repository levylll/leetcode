#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-06-10 19:43:33

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        new_head = None
        while head is not None:
            if new_head:
                print 'AA'
                p = head.next
                head.next = new_head
                new_head = head
            else:
                print 'BB'
                new_head = head
                p = head.next
                new_head.next = None
            head = p
        return new_head


def gen_list_node(in_list):
    head = None
    for i in in_list:
        if head is None:
            head = ListNode(i)
            p = head
        else:
            # print i
            p.next = ListNode(i)
            p = p.next
    return head

def show_list(l_node):
    # print l_node
    while l_node:
        print l_node.val,
        l_node = l_node.next


in_list = [1,2,3,4,5]
head = gen_list_node(in_list)
# show_list(head)
# print '==========='
sol = Solution()
# show_list(head)
res = sol.reverseList(head)
show_list(res)
# print res
