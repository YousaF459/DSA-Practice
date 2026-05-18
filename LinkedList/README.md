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


### 1. Linked List Cycle
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







