# 🧵 String Problems - DSA Repository

Welcome to the **String** folder of my DSA repository!  
This folder contains solutions to string-related problems, implemented in **Python**, along with explanations and coding patterns used to solve them efficiently.

---

## 🔹 Overview

Strings are one of the most fundamental data structures in programming and appear in almost every coding interview or competitive programming problem.  
Here, you will find a collection of problems ranging from **basic string manipulation** to **advanced string algorithms**.

Key techniques used in this folder:

- Sliding Window  
- Two Pointers  
- Hashing (Rabin-Karp)  
- Prefix/Suffix Arrays  
- Pattern Searching (KMP)  
- String Matching and Substring Problems  
- Palindromes and Anagrams  

---

## 🔹 How To Use

1. Each problem is placed in a separate Python file.  
2. The filename is Given You can cehck the solution.
3. Every solution includes:
   - Problem statement
   - Approach/logic explained with comments
   - Python code implementing the solution
   - Time & space complexity analysis

---

## 📂 Problems Solved

---

### 1. Find The Index Of The First Occurrence In A String
- **File:** `FindTheIndexOfTheFirstOccurrenceInAString.py`  
- **Difficulty:** Easy  
- **Technique:** Sliding Window
- **Data Structure:** String  

**💡 Idea:**  
- First take window of String we want to check in other String
- Move the iterations and move the window 

**⏱️ Complexity:**  
- Time: O(n*m)  
- Space: O(1)


### 2. Find The Longest_Palindromic_Substring
- **File:** `Longest_Palindromic_Substring.py`  
- **Difficulty:** Medium
- **Technique:** Sliding Window,Two Pointers
- **Data Structure:** String  

**💡 Idea:**  
- we have to find longest palindromic string
- Longest Substring which meets the condition can be anywhere
- so we should start from anywhere and expand in both left and right directions
- if left and right pointers are same we can keep expanding
- for odd length string we start left and right pointers from same index
- for even length we ahve to start even and odd pointer from differnt index

**⏱️ Complexity:**  
- Time: O(n²)  
- Space: O(1)


### 3. Valid_Palindrome_II
- **File:** `Valid_Palindrome_II.py`  
- **Difficulty:** Easy
- **Technique:** Two Pointers
- **Data Structure:** String  

**💡 Idea:**  
- Inputs = String with lower case letters and a character change limit
- we have to check if string is a palindrome we can also del one character from string

- technique - two pointers

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)




### 4. Permutation_in_String
- **File:** `Permutation_in_String.py`  
- **Difficulty:** Medium
- **Technique:** Hashing , Sliding Window
- **Data Structure:** String  

**💡 Idea:**  
- we need to check if s1 characters are present in subarray in s2
- characters of s1 frequence in seleceted subarray of s2
- make two hashmap one of s2 counter adn one of s2 subarray
- if window counter length get bigger start shrinking from left

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(1)




### 5. Sort_Characters_By_Frequency
- **File:** `Sort_Characters_By_Frequency.py`  
- **Difficulty:** Medium
- **Technique:** Hashing 
- **Data Structure:** String  

**💡 Idea:**  
- We can store characters frequency in hashmap
- then we can sort it them in decreasing order
- loop over it and multiple key with values
- store it in string

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)


Find_All_Anagrams_in_a_String


### 6. Find_All_Anagrams_in_a_String
- **File:** `Find_All_Anagrams_in_a_String.py`  
- **Difficulty:** Medium
- **Technique:** Sliding Window 
- **Data Structure:** String  

**💡 Idea:**  
- input - Two String s and p
- output array which contain start index of anagram of p in s
- we use slidign window
- we take a window check if occurence is sae as in p we append elft in array
- when sldiign window get bigger we shrink else we expand

**⏱️ Complexity:**  
- Time: O(n)  
- Space: O(n)