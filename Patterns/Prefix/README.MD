
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

### 1. Minimum Number of Operations to Move All Balls to Each Box
- **File:** `Minimum_Number_of_Operations_to_Move_All_Balls_to_Each_Box.py`  
- **Difficulty:** Medium  
- **Technique:** Prefix 
- **Data Structure:** String  

**💡 Idea:**  
- input - String og binaries
- ouput - array of number of operations to move balls into that specific index
- loop from left to left keep adding balls adn moves prefix
- loop from right to left keep adding balles from right to left suffix

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)  

---