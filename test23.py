# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.heap = []

    def insert(self, pos):
        if pos != 0:
            parent_pos = (pos-1)//2
            val = self.heap[pos]
            if self.heap[parent_pos] > val:
                t = self.heap[parent_pos]
                self.heap[parent_pos] = val
                self.heap[pos] = t
                self.insert(parent_pos)

    def adjust(self, pos):

        left = pos * 2 + 1
        right = pos * 2 + 2

        if left >= len(self.heap):
            return
        max_pos = left if right >= len(self.heap) or self.heap[left] < self.heap[right] else right
        if self.heap[pos] > self.heap[max_pos]:
            t = self.heap[max_pos]
            self.heap[max_pos] = self.heap[pos]
            self.heap[pos] = t
            self.adjust(max_pos)

    def delete(self, pos):
        if len(self.heap) == 1:
            return self.heap.pop(0)
        if pos < len(self.heap):
            res = self.heap[0]
            val = self.heap.pop(-1)
            self.heap[0] = val
            self.adjust(0)
            return res

    def init_heap(self, lists):
        for line in lists:
            # for x in line:
            #     self.heap.append(x)
            #     if len(self.heap) != 1:
            #         self.insert(len(self.heap) - 1)

            p = line
            while p:
                val = p.val
                self.heap.append(val)
                if len(self.heap) != 1:
                    self.insert(len(self.heap) - 1)
                p = p.next
            #print(self.heap)

    @classmethod
    def list2link(cls, nums):
        head = None
        p = None
        for x in nums:
            if not head:
                head = ListNode(x)
                p = head
            else:
                p.next = ListNode(x)
                p = p.next
        return head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.init_heap(lists)
        head = None
        p = None
        while self.heap:
            val = self.delete(0)
            if not head:
                head = ListNode(val)
                p = head
            else:
                p.next = ListNode(val)
                p = p.next
        return head


lists = [[1,4,5],[1,3,4],[2,6]]
s = Solution()
tmp = []
for elem in lists:
    nodes = Solution.list2link(elem)
    tmp.append(nodes)
#head = s.mergeKLists(lists)
head = s.mergeKLists(tmp)

p = head
while p:
    print(p.val)
    p = p.next


