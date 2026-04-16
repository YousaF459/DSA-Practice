# Two Pointers Pattern

## 🧠 When to Use
- Sorted arrays
- Pair or triplet problems
- Searching from both ends
- In-place array operations


## 🚩 Common Signals
- "pair sum"
- "sorted array"
- "remove duplicates"
- "reverse array / string"
- "closest / min / max pair"


## ⚙️ Core Idea
- Use two pointers (left and right)
- Move pointers based on condition
- Reduce O(n²) brute force to O(n)



## 🧩 Template Code
```python
def two_pointers(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if condition_is_met:
            # process answer
            left += 1
            right -= 1

        elif need_larger_value:
            left += 1

        else:
            right -= 1
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