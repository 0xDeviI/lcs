from solution import Solution, ListNode

def print_linked_list(l: ListNode):
    current_iterator = l
    values = []
    while (current_iterator != None):
        values.append(current_iterator.val)
        current_iterator = current_iterator.next
    print(values)

# [2,4,9]
# l2 =
# [5,6,4,9]

solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
print_linked_list(solution.addTwoNumbers(l1, l2))