# Sliding Window Pattern

## 🧠 When to Use
- Subarray / substring problems
- Contiguous elements
- Max / min / count

## 🚩 Common Signals
- "Longest substring"
- "Minimum size subarray"
- "At most K"
- "Continuous / contiguous"

## ⚙️ Core Idea
- Use two pointers (left & right)
- Expand window by moving right
- Shrink window when condition breaks

## 🧩 Template Code

```python
def sliding_window(nums):
    left = 0
    for right in range(len(nums)):
        # expand

        while condition_not_valid:
            left += 1

        # update result

```
---

## 📂 Problems Solved

---

### 1. Maximum Number of Vowels in a Substring of Given Length
- **File:** `Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length.py`  
- **Difficulty:** Medium  
- **Pattern:** Sliding window With Hashing 
- **Data Structure:** Hashmap  

**💡 Idea:**  
- Input - A String and a Integer K
- Output- From String get substring of length k adn find the max number of vowel occurence in substring length k
- We will Use Sliding Window
- We will keep sliding window of length K
- when sliding window length get bigger than k we shrink window from left
- when we shrink window we will remove occurence of Left Pointer
- when we expand we increase occurence of right pointer
- we will keep max varaible to detect the max occurence in a substring
- for each iteration we can check if s[right] is a vowel increment in counter
- when condition will reach just check if s[left] is a vowl if yes decrement counter
- when sldiig widnow will be of length k check the Counter
  

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---