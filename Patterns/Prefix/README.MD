
---

# 🔵 Prefix Sum / Prefix Product Pattern (README.md)

```md
# Prefix Sum / Prefix Product Pattern

## 🧠 When to Use
- Range sum queries
- Subarray sum problems
- Cumulative calculations
- Product except self type problems

## 🚩 Common Signals
- "subarray sum equals K"
- "range sum query"
- "product of array except self"
- "sum between indices"

## ⚙️ Core Idea
- Precompute running sum/product
- Use precomputed values to answer queries in O(1)
- Avoid recalculating ranges

## 🧩 Template Code (Prefix Sum)
```python
def prefix_sum(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix
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