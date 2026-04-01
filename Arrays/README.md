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