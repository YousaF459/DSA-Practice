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



### 2. Ransom_Note
- **File:** `Ransom_Note.py`  
- **Difficulty:** Easy  
- **Technique:** Two Pointers  
- **Data Structure:** String  

**💡 Idea:**  

- Two String inputs - ransomNote "aa" adn magazine  "aab"
- ouput we have to cehck if we can make ransomNote string from magazine Letters
- we can just make a frequencey hashmap of magazine
- then make a loop on ransomNote to check if all characters are available in magazine hashmap
 

**⏱️ Complexity:**  
- Time: O(n+m)  
- Space: O(1)  

---


### 3. Sort_Array_By_Parity
- **File:** `Sort_Array_By_Parity.py`  
- **Difficulty:** Easy  
- **Technique:** Two Pointers  
- **Data Structure:** String  

**💡 Idea:**  
- input - Array of integers
- ouput - put all even on start and odd at end their order does not matter
- initilaize two pointers left adn right
- left pointer is use to write the even numbers at start
- Start a loop 
- if number is even swap left and right pointer values
 

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---




### 4. Number_of_Matching_Subsequences
- **File:** `Number_of_Matching_Subsequences.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers  
- **Formula:** if s[i] == word[j] then j+=1 

**💡 Idea:**  

- Input a String and an array of strings
- Ouput - number of words in array that are subsequence of string
- solution Steps
- we have to check for every array word if its subsequnece of string S.
- so we initialize variable j if word character and string s character amtch we increment varaible j.
- then we cehck if len varaible j is equal to length of word then its a subsequence.
- so we are using formula if s[i] == word[j] increment j

**⏱️ Complexity:**  
- Time: O(n*m)  
- Space: O(1)  

---
