
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