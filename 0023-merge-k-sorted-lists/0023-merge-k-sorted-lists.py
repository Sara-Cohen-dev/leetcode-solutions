# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists):

        heap = []

        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        dummy = ListNode(0)
        curr = dummy

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        return dummy.next