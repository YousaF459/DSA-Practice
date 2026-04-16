
---

# 🟡 Hashing Pattern (README.md)

```md
# Hashing Pattern

## 🧠 When to Use
- Frequency counting
- Fast lookup needed
- Duplicate detection
- Subarray sum problems
- Anagram / grouping problems

## 🚩 Common Signals
- "frequency"
- "first unique"
- "anagram"
- "subarray sum"
- "contains duplicate"

## ⚙️ Core Idea
- Use HashMap / Set
- Store frequency or visited states
- Trade space for speed

## 🧩 Template Code
```python
def hashing(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return freq
```

---


## 📂 Problems Solved

---

### 1. Intersection of Two Arrays II
- **File:** `Intersection_of_Two_Arrays_II.py`  
- **Difficulty:** Easy  
- **Pattern:** Hashing
- **Data Structure:** Array  

**💡 Idea:**  
- input - Two Arrays
- Ouput - Array whihc contain common items from both arrays 
- we make hashmap with occurence of from one array
- we loop on secodn array adn check if it is in hashmap adn if yes we remove its count 
- we chcek if count[num] > 0

**⏱️ Complexity:**  
- Time: O(n+m)  
- Space: O(n)  

---