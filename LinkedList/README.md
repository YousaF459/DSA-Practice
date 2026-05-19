# Linked List - Data Structures

This folder contains my implementations and practice problems related to **Linked List**, one of the fundamental linear data structures used in problem solving and interviews.

---

## What is a Linked List?

A Linked List is a linear data structure where elements (nodes) are stored in separate objects, and each node points to the next node using a pointer/reference.

Unlike arrays, linked lists do not store elements in contiguous memory.

---

## Types Covered

- Singly Linked List
- (Future) Doubly Linked List
- (Future) Circular Linked List

---

## Core Operations Implemented

### Basic Operations
- Create Linked List
- Insert at Head
- Insert at Tail
- Insert at Position
- Delete Node
- Traverse / Print List

### Important Problems
- Reverse Linked List
- Find Middle of Linked List
- Detect Cycle in Linked List
- Remove Cycle
- Merge Two Sorted Linked Lists
- Remove Duplicates

---

## Concepts Practiced

- Pointer manipulation
- Iteration vs recursion
- Edge cases handling (empty list, single node)
- Time and space optimization

---

## Patterns Used (inside Linked List problems)

- Fast & Slow Pointers
- Two Pointers
- In-place reversal technique

---

## Goal

To build strong understanding of linked list operations and prepare for coding interviews by mastering both basic operations and common interview problems.

---

## Notes

- Each problem is solved in Python.
- Focus is on understanding logic, not just memorization.
- Solutions are written in a clean and interview-friendly way.

---


## 📂 Problems Solved

---


### 1. Middle_of_the_Linked_List
- **File:** `Middle_of_the_Linked_List.py`  
- **Difficulty:** Easy  
- **Pattern:** Linked List
- **Pattern:**  TWO pointers - Fast and Slow

**💡 Idea:**  
- Two Pointer Will be iterating slow and fast
- move fast two step adn slow one step 
- when fast will reach end slow will be in middle


**💡Template**

TEMPLATE :-

slow=head
fast=head

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next




**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 2. Linked List Cycle
- **File:** `Linked List Cycle.py`  
- **Difficulty:** Easy  
- **Pattern:** Linked List
- **Pattern:**  TWO pointers - Fast and Slow

**💡 Idea:**  
- Two Pointer Will be iterating slow and fast
- move fast two step adn slow one step 
- like in a track one runner is running slow and other is running fast so eventualy fast will meet slower again
- so fast will meet slow again if slow==fast then True


**💡Template**

TEMPLATE :-

slow=head
fast=head

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next




**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---



### 3. Merge Two Sorted Lists
- **File:** `Merge_Two_Sorted_Lists.py`  
- **Difficulty:** Easy  
- **Pattern:** Linked List
- **Pattern:**  two Pointer

**💡 Idea:**  
- we initilize a dummy node and a tail pointer from where we start so we can point to head.
- we compare both value which one is smaller we point tail to that.
- at last tail will be pointing to end
- if some elemtnet of one list remain we connect tail to that.


**💡Template**

TEMPLATE :-

while list1 and list2:
            if list1.val <= list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        
        if list1:
            tail.next=list1


        else:
            tail.next=list2




**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 4. Remove Duplicates from Sorted List
- **File:** `Remove_Duplicates_from_Sorted_List.py`  
- **Difficulty:** Easy  
- **Pattern:** Linked List
- **Pattern:**  two Pointer

**💡 Idea:**  
- we initilize a pointer to head named currentPointer
- we check currentNode.val with curentNode.next.val
- if val is same just remove the link between them


**💡Template**

TEMPLATE :-

 currentNode=head

        while currentNode and currentNode.next:

            if currentNode.val==currentNode.next.val:
                currentNode.next=currentNode.next.next
            else:
                currentNode=currentNode.next



**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---



### 5. Palindrome_Linked_List
- **File:** `234_Palindrome_Linked_List.py`  
- **Difficulty:** Easy  
- **Pattern:** Linked List
- **Pattern:**  Fast adn Slow Pointer and Reverse Linked List

**💡 Idea:**  
- First we have to fidn the middle of linked List using Fast and slow pointer
- then we reverse the linked from middle till end
- now we can iterate and compare


**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 6. Remove_Nth_Node_From_End _of_List
- **File:** `Remove_Nth_Node_From_End _of_List.py`  
- **Difficulty:** Medium  
- **Data Strucutre:** Linked List
- **Pattern:**  Fast adn Slow Pointer and create a gap with fast additional move at n+1

**💡 Idea:**  
- we have to create a gap between fast and slow pointer with fast additionaly placing at n+1
- then when fast will reach end slow will be exactl at before deleting node 


**💡Template**

TEMPLATE :-

for _ in range(n+1):
            fast=fast.next



**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---











