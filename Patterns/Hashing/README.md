
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





### 2. Find_All_Duplicates_in_an_Array
- **File:** `Find_All_Duplicates_in_an_Array.py`  
- **Difficulty:** Medium  
- **Pattern:** Array as hashmap , index marking
- **Data Structure:** Array  

**💡 Idea:**  
- nums[i] is always in range of n - n is length o array
- so we do index marking like index=number - 1 go to that index adn mark it with negative
- by this method we know if this is already visited or not
- if already visited it will be less than 0 measn negatvie else first time visit
- so if already visited append to array

**💡Learning From problem**
- this is index marking problem as no extra space used and nums[items] items are from 1 to n-n is array length
- we can use items to mark the index if index already visited then its duplicate else not
1️⃣ Can values be used as indexes?
2️⃣ Can I store state inside array?
3️⃣ Can I avoid extra memory?
TEMPLATE :-

for num in nums:
    index = abs(num) - 1

    if nums[index] < 0:
        # duplicate / seen before
    else:
        nums[index] *= -1 



**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---



### 3. Missing_Number
- **File:** `Missing_Number.py`  
- **Difficulty:** Medium  
- **Pattern:** Array as hashmap , index marking
- **Data Structure:** Array  

**💡 Idea:**  
- Using XOR technique we have to sove this 

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 4. Find All Numbers Disappeared in an Array
- **File:** `Find_All_Numbers_Disappeared_in_an_Array.py`  
- **Difficulty:** Medium  
- **Pattern:** Array as hashmap , index marking
- **Data Structure:** Array  

**💡 Idea:**  
- index are from 1 to n and values are aslo from 0 to n
- so we mark index like index=abs(num) -1 
- then we mark the index
- as values are not starting from 0 when checking mark index when we store result we do i +1 
**💡Learning From problem**

1️⃣ Can values be used as indexes?
2️⃣ Can I store state inside array?
3️⃣ Can I avoid extra memory?
TEMPLATE :-

for num in nums:
    index = abs(num) - 1

    nums[index] = -abs(nums[index])
    
    if nums[i] > 0:
                result.append(i + 1)



**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---



### 5. Set_Mismatch
- **File:** `Set_Mismatch.py`  
- **Difficulty:** Easy  
- **Pattern:** Array as hashmap , index marking
- **Data Structure:** Array  

**💡 Idea:**  
- we have to chec k missing and duplicate
- for duplicate mark index adn which is < 0 and visited again it is duplciate
- for missin gwhich is greater than 0 then missing=i + 1
**💡Learning From problem**

1️⃣ Can values be used as indexes?
2️⃣ Can I store state inside array?
3️⃣ Can I avoid extra memory?
TEMPLATE :-

for num in nums:
    index = abs(num) - 1

    nums[index] = -abs(nums[index])

    #for duplciate
        if nums[num] > 0
        misiing=num
    

    # for missing
    if nums[i] > 0:
            missing=i+1



**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---

