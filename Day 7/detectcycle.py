    def hasCycle(self, head) -> bool:
        if head is None : return False
        slow = head
        fast = head.next
        if fast is None: return False
        fast = fast.next
        while slow is not None and fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next        
            if fast is None:
                return False
            fast = fast.next
        return False

##Ref
#https://leetcode.com/problems/linked-list-cycle/submissions/
#https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/