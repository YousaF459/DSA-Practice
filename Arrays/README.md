📊 Arrays - Data Structures & Algorithms

This folder contains my practice and solutions for Array-based problems.
I am solving problems to improve my problem-solving skills, pattern recognition, and coding efficiency using Python.

---


🚀 What I’m Focusing On
Understanding core array concepts
Learning problem-solving patterns
Writing clean and optimized code
Analyzing time & space complexity

---

🧠 Patterns Covered

✅ Two Pointer Technique

---


## 📂 Problems Solved

---

### 1. Container With Most Water
- **File:** `ContainerWithMostWater.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers  
- **Data Structure:** Array  

**💡 Idea:**  
- Use two pointers (start & end)  
- Calculate width using the difference of indices  
- Height is determined by the **minimum of the two lines**  
- Move the pointer pointing to the **smaller height**  

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---

### 2. Remove Duplicates from Sorted Array
- **File:** `RemoveDuplicatesfromSortedArray.py`  
- **Difficulty:** Easy  
- **Technique:** Two Pointers  
- **Data Structure:** Array  

**💡 Idea:**  
- Use one pointer to **read values**  
- Use another pointer to **place unique values**  
- Overwrite duplicates **in-place**  

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1) (in-place solution)  


### 3. 3Sum
- **File:** `3Sum.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers ,Sorting
- **Data Structure:** Array  

**💡 Idea:**  
- Fix one pointer and use two pointers to find pairs that sum to target  
- Skip duplicates to avoid repeating triplets  
- Return all unique triplets

**⏱️ Complexity:**  
- Time: O(n²)  
- Space: O(n)

### 4. MinimumSizeSubarraySum
- **File:** `MinimumSizeSubarraySum.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers ,Sliding Window
- **Data Structure:** Array  

**💡 Idea:**  
- two Pointer left and right
- left pointer will make window shrink when sum is >= target
- right pointer will move forward if sum <= target 
- we are use two pointer to make a sliding window shrink or expand

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)

### 5.  Single Number
- **File:** `Single_Number.py`  
- **Difficulty:** Easy  
- **Technique:** Two Pointers ,Sliding Window
- **Data Structure:** Array  

**💡 Idea:**  
- we have to sort the array then apply two pointers
- Make a sliding window usign pointers
- when array will be sorted we have to check two contagious elements

**⏱️ Complexity:**  
- Time: O(n log n)  
- Space: O(1)

### 6.  Single Number
- **File:** `Maximum_Average_Subarray_I.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers ,Sliding Window
- **Data Structure:** Array  

**💡 Idea:**  
- we make a sliding window
- to make time complexity we just add next item and remove previous item when slide is moved


**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)



### 7.  Subarray_Sum_Equals_K
- **File:** `Subarray_Sum_Equals_K.py`  
- **Difficulty:** Medium  
- **Technique:**  Hashing
- **Data Structure:** Array  , Hashmap

**💡 Idea:**  
- get the prefix sum first
- use formula prefixSum -k to check if that exist in hashmap
- if it exist then increase count by value of hashmap prefixSum
- if same value occurs twice increase count by +1 whatever value is there


**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)





### 8.  Fruit_Into_Baskets
- **File:** `Fruit_Into_Baskets.py`  
- **Difficulty:** Medium  
- **Technique:**  Hashing, Two Pointers , Sliding Window
- **Data Structure:** Array  , Hashmap

**💡 Idea:**  
- input - Array
- output will be max subarray that contains only two fruits
- technique used sliding window , hashing and two pointers
- when more than 2 elements in hashmap start shrinking from left 
- when we shrink from left we shrink until one elements count become 0
- as there are only 2 elements before so only 2 unique will remain


**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)



### 9.  Two_Sum_II-Input_Array_Is_Sorted
- **File:** `Two_Sum_II-Input_Array_Is_Sorted.py`  
- **Difficulty:** Medium  
- **Technique:**  Two Pointers
- **Data Structure:** Array  

**💡 Idea:**  
- Technique = Two pointer
- place left pointer at index 0 and right at alst index
- calculate their sum
- if sum == targer retunr index
- if sum > target - decrement right pointer
- if sum < target - increment left pointer


**⏱️ Complexity:**  
- Time Complexity - BigO(n)
- Space Complexity - BigO(1)
