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

### 1. Backspace_String_Compare
- **File:** `Backspace_String_Compare.py`  
- **Difficulty:** Easy  
- **Technique:** Two Pointers  
- **Data Structure:** String  

**💡 Idea:**  
- Use Two Pointers
- first make a function which checks if have to skip or not if not send the character which we are cehcking 
- if the characters are equal then good else return False
- if one of them i or j get bigger we return False
 

**⏱️ Complexity:**  
- Time: O(n+m)  
- Space: O(1)  

---