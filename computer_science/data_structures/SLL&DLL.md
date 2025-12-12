# Comparison: Singly Linked List (SLL) vs Doubly Linked List (DLL)

| Feature/Operation           | Singly Linked List (SLL) | Doubly Linked List (DLL) |
|-----------------------------|--------------------------|--------------------------|
| **Nodes structure**          | Each node contains a data value and a reference (pointer) to the next node. | Each node contains a data value, a reference to the next node, and a reference to the previous node. |
| **Memory usage**             | Less memory since each node only has a pointer to the next node. | More memory as each node requires two pointers (to both next and previous nodes). |
| **Traversal**                | Can only traverse in one direction (forward). | Can traverse in both directions (forward and backward). |
| **Insert at beginning**      | O(1) – constant time since only the head pointer needs to be updated. | O(1) – constant time since both pointers of the head and the new node are updated. |
| **Insert at end**            | O(n) – must traverse the entire list to find the end (unless tail pointer is maintained, then O(1)). | O(1) – if the tail pointer is maintained; otherwise, O(n) if traversal is required. |
| **Insert after a given node**| O(n) – must traverse to find the node, then perform the insertion. | O(n) – must traverse to find the node, then perform the insertion, but no need to adjust traversal pointers. |
| **Delete from beginning**    | O(1) – only the head pointer needs to be updated. | O(1) – the head and the head’s next node’s previous pointer need to be updated. |
| **Delete from end**          | O(n) – requires traversal to the second-last node. | O(1) – if a tail pointer is maintained; otherwise, O(n) for traversal. |
| **Delete after a given node**| O(n) – requires traversal to find the node and adjust pointers. | O(n) – requires traversal, but it’s easier to adjust both previous and next pointers. |
| **Search for a value**       | O(n) – must traverse the list to find the element. | O(n) – must traverse the list, but can search in both directions. |
| **Reverse the list**         | O(n) – requires changing the direction of pointers, starting from the head. | O(n) – requires switching the previous and next pointers of every node. Easier due to the presence of two pointers. |

# Common Methods in Doubly Linked Lists (DLL) and Their Time Complexities

1. **Insert at Head (beginning)**:
   - Time Complexity: O(1)
   - Method: Update the previous head's `prev` pointer and the new node's `next` pointer.

2. **Insert at Tail (end)**:
   - Time Complexity: O(1) (if a tail pointer is maintained)
   - Method: Add the new node at the tail, update the current tail's `next` pointer, and the new node's `prev` pointer.

3. **Delete from Head (beginning)**:
   - Time Complexity: O(1)
   - Method: Update the head pointer and the new head’s `prev` pointer to `null`.

4. **Delete from Tail (end)**:
   - Time Complexity: O(1) (if a tail pointer is maintained)
   - Method: Update the previous node's `next` pointer to `null`, and update the tail pointer.

5. **Search for a Node**:
   - Time Complexity: O(n)
   - Method: Traverse from head to tail (or tail to head if necessary).

6. **Traverse Forward**:
   - Time Complexity: O(n)
   - Method: Start from the head and follow the `next` pointers.

7. **Traverse Backward**:
   - Time Complexity: O(n)
   - Method: Start from the tail and follow the `prev` pointers.

8. **Reverse List**:
   - Time Complexity: O(n)
   - Method: Iterate through the list and swap each node’s `next` and `prev` pointers.

## Use cases

1. Hash maps: imagine we have a hash function, which can point different elements to the same hash value. We can store those values as they arrive in a specific value in a list, for example, but using SLL is less memory consuming.