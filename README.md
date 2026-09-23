# 🚀 Daily LeetCode & DSA Journey

A dedicated repository tracking my daily Data Structures & Algorithms practice, problem-solving intuition, and runtime analysis. Synced directly from [LeetCode](https://leetcode.com).

---

## 🎯 Goals & Practice Strategy
- **Consistency:** 1+ problem solved daily.
- **Complexity First:** Analyze time and space complexity before coding; optimize from brute force to optimal patterns.
- **Pattern Mastery:** Focus on core paradigms: Prefix/Suffix Products, Hash Maps, Two Pointers, Sliding Window, Monotonic Stacks, and Trees.

---

## 📊 Solved Problems Index

| Day | # | Problem | Topic | Difficulty | Optimal Approach | Time | Space |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: | :---: |
| 01 | 0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Arrays & Hashing | Easy | Hash Set Membership | $O(N)$ | $O(N)$ |
| 02 | 0242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Arrays & Hashing | Easy | Frequency Array / Map | $O(N)$ | $O(1)$ |
| 03 | 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays & Hashing | Easy | One-Pass Hash Map | $O(N)$ | $O(N)$ |
| 04 | 0049 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Arrays & Hashing | Medium | Categorize by Sorted Str / Char Count Tuple | $O(N \cdot K \log K)$ | $O(N \cdot K)$ |
| 05 | 0347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Arrays & Hashing | Medium | Bucket Sort / Min-Heap | $O(N)$ | $O(N)$ |
| 06 | 0238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Arrays & Hashing | Medium | Prefix & Postfix Running Products | $O(N)$ | $O(1)^*$ |

> *\*Note on #238: The output array does not count as extra space for complexity analysis.*

---

## 📂 Repository Organization

Solutions are synced automatically upon receiving an **Accepted** verdict:

```text
leetcode-solutions/
├── README.md
├── .gitignore
├── 0217-contains-duplicate/
│   ├── README.md                          # Problem statement & constraints
│   └── contains-duplicate.py              # Accepted implementation
├── 0242-valid-anagram/
│   ├── README.md
│   └── valid-anagram.py
├── 0001-two-sum/
│   ├── README.md
│   └── two-sum.py
├── 0049-group-anagrams/
│   ├── README.md
│   └── group-anagrams.py
├── 0347-top-k-frequent-elements/
│   ├── README.md
│   └── top-k-frequent-elements.py
└── 0238-product-of-array-except-self/
    ├── README.md
    └── product-of-array-except-self.py
