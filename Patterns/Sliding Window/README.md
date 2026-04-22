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

### 2. Number_of_Substrings_Containing_All_Three_Characters
- **File:** `Number_of_Substrings_Containing_All_Three_Characters.py`  
- **Difficulty:** Medium  
- **Pattern:** Sliding window With Hashing 
- **Data Structure:** Hashmap  

**💡 Idea:**  
        
- Input - String
- Output - Count of subtring which contain all three a,b,c
- We have to create a sliding window of substrign which contain all three a,b,c
- after that we use formula to add remainign length of strign cause all of them will on auto contain a,b,c
- formula len(s) - right - right is the index where when we get a,b,c in substring
- when we use the formula we shrink from left
- and keep expanding after we get substrign with occurecne of all a,b,c
  

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 3. Longest_Subarray_of_1's_After_Deleting_One_Element
- **File:** `Longest_Subarray_of_1's_After_Deleting_One_Element.py`  
- **Difficulty:** Medium  
- **Pattern:** Sliding window
- **Data Structure:** Hashmap  

**💡 Idea:**  
        
- input - Array of binary Number
 output - find largest substring by deleting 1 number from array if zero del taht else 1
- we have to make a valid sliding window in which we have only 1 zero included
 when sliding window will get invalid measn we reach second zero
- we will have to shrink the window when more than 1 zero in substrin
 we get length of substring with right-left+1
- we decrement 1 from max_len
        

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 4. Count_Number_of_Nice_Subarrays
- **File:** `Count_Number_of_Nice_Subarrays.py`  
- **Difficulty:** Medium  
- **Pattern:** Sliding window
- **Data Structure:** Array  

**💡 Idea:**  
        
- input - Array of integer and a integer k 
- ouput - return count of subarray with k odd number in it
- we will use slidign window using three pointers -left , middle , right
- when we reach k odd number we move forward middle so we get substring with odd numerb from left side
- so now even when we move right we have account of left substring and until we reach next odd number every time we move right we add middle-left+1
- if we reach odd number on right we move left pointer forward until we reach odd number and then also put middle on left pointer
        

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 5. Replace_the_Substring_for_Balanced_String
- **File:** `Replace_the_Substring_for_Balanced_String.py`  
- **Difficulty:** Medium  
- **Pattern:** Sliding window,Hashing
- **Data Structure:** Array  

**💡 Idea:**  
        
- input - String
- output - minmum length substring which we can repalce with substring to make  S balanced
- make a hashmap to check what is extra - hashmap need={}
- window hashmap to check count if current sliding window has extra characters we have in need hashmap
- get the length when current window has all the characters we need
        

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 5. Maximum_Erasure_Value
- **File:** `Maximum_Erasure_Value.py`  
- **Difficulty:** Medium  
- **Pattern:** Sliding window,Hashing
- **Data Structure:** Array  

**💡 Idea:**  
        

- input - integer array
- output - maximum sum of unique substring numbers
- we ahve to maintain a sliding window of unique elemetns
- if sldiign window get a duplicate elemten we have to shrink from left till we remove duplicate element
- formula - we expand till we find a duplicate
- 1-when duplicate is found we expand till we remove duplicate which was already in hashmap
- 2- while array[right] in hashmap : we keep shrinking
- 3- we add array[right] in hashmap after we have shrink from left to reach a valid window
        

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)  

---
