
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



### 2. Longest_Word_in_Dictionary
- **File:** `Longest_Word_in_Dictionary.py`  
- **Difficulty:** Medium  
- **Technique:** Prefix  
- **Tools:**  Set 
- **Formula** currnetitem[:-1] already exist in set then its valid

**💡 Idea:**  
- Input - A Arrays of Strings
- OUTPUT- Return longest word from string that can be made up by one character at a time from left to right
- Solution - Prefix and Set
- 1- First we sort array then We have to check if prefix of each word exist before it 
- 2- For checking 1- condition we use formula like if we not take one last cahracter from current string is it equal to previou string
- 3- if condition 2- is true then keep adding it to set and also change result cause new string length is larger


- What I Learned From it
"""
1- in this problem where we ahve to cehck if next is valid base on previos we are basiccly building from smaller valid states
Like in this problem word is valid only is its samller prefix is already valid - So core Pattern is incremental construction base
on previous valid state -> must build step by step and smaller version determines bigger version so we can use:-
Hashset , dynamiic programming style growth or trie sometimes
2-When bigger string depends on smaller prefix existing:
Use set of valid words + process shortest first
"""


**⏱️ Complexity:**  
- Time: O(n log n)  
- Space: O(n)  

---