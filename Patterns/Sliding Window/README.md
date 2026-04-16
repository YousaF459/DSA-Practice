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

def sliding_window(nums):
    left = 0
    for right in range(len(nums)):
        # expand

        while condition_not_valid:
            left += 1

        # update result


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