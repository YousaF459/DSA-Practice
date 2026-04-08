## 🗂️ HashMap - Data Structures & Algorithms
This folder contains my practice and solutions for HashMap (Dictionary) based problems.
I am solving these problems to improve my problem-solving skills, pattern recognition, and efficient data lookup techniques using Python.

---

## 🚀 What I'm Focusing On

Understanding how HashMaps work internally
Using HashMaps for fast lookups (O(1))
Solving problems involving frequency counting & mapping
Writing clean and optimized code
Analyzing time & space complexity

---

## 🧠 Patterns Covered

✅ Frequency Counting
✅ Key-Value Mapping
✅ Lookup Optimization
✅ Handling Duplicates

--- 

## 📂 Problems Solved

---

### 1. Check Valid Anagram
- **File:** `Valid_Anagram.py`  
- **Difficulty:** Easy  
- **Technique:** Frequency Counting
- **Data Structure:** Hashmap

**💡 Idea:**  
- We have two strings contain lowercase characters
- if one contain something in other string we check it has same characters and equal occurence in  - other string
- we can store both in separate dictionary
- loop over and check count of both

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)

### 2. Longest_Substring_Without_Repeating_Characters
- **File:** `Longest_Substring_Without_Repeating_Characters.py`  
- **Difficulty:** Medium  
- **Technique:** Hashing , two Pointer , sliding window
- **Data Structure:** Hashmap

**💡 Idea:**  
- to not have duplicate we use hashing
- two pointer to remember index and check for items not to be duplicate
- shrink or expand the pointers base on condition

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)

### 2. Longest_Repeating_Character_Replacement
- **File:** `Longest_Repeating_Character_Replacement.py`  
- **Difficulty:** Medium  
- **Technique:** Hashing , two Pointer , sliding window
- **Data Structure:** Hashmap

**💡 Idea:**  
- check length of which substring to get using total item - max characters occurence > k
- shrink and expand base on condition

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)