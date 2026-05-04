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


### 5. Is_Subsequence
- **File:** `Is_Subsequence.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers  
- **Formula:** if s[i] == t[j] then j+=1 then check j == len(subsequence)

**💡 Idea:**  

- Solutions:-
- we define and initilize two vraible i and j
- i scan main string
- j scan subsequecne string
- i increment every time adn j increment when match happens
- check j if its equal to len(subsequnce) then is subsequence else not

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---




### 6. Longest_Word_in_Dictionary_through_Deleting
- **File:** `Longest_Word_in_Dictionary_through_Deleting.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers  
- **Formula:** if s[i] == t[j] then j+=1 then check j == len(subsequence)  if word < longest word then longest word =word

**💡 Idea:**  

- Solutions:-
- we define and initilize two vraible i and j
- i scan main string
- j scan subsequecne string
- i increment every time adn j increment when match happens
- check j if its equal to len(subsequnce) then is subsequence else not

**⏱️ Complexity:**  
- Time: O(n*m)  
- Space: O(1)  

---

### 7. Append_Characters_to_String_to_Make_Subsequencepy
- **File:** `Append_Characters_to_String_to_Make_Subsequencepy.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers  
- **Formula:** if s[i] == t[j] then j+=1 then check len(t)-j

**💡 Idea:**  

- Solutions:-
- we define and initilize two variable i and j
- i scan main string
- j scan subsequecne string
- i increment every time adn j increment when match happens
- check len(t)-j

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  

---


### 8. Long_Pressed_Name
- **File:** `Long_Pressed_Name.py`  
- **Difficulty:** Medium  
- **Technique:** Two Pointers  
- **Formula:** while j < len(typed) we check if both are euqal then i and j +=1 elif check if j == j -1 then j+=1

**💡 Idea:**  

- Solutions:-
- we define and initilize two variable i and j
- i scan name string
- j scan typed string
- while j < len(typed) we check if both are euqal then i and j +=1 elif check if j == j -1 then j+=1

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)  