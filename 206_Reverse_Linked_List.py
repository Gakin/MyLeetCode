#Solution is taken from the leetcode itself because of its easy to understand way of build
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
