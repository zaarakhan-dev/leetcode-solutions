# Daily LeetCode & DSA Journey

A dedicated repository tracking my daily Data Structures & Algorithms practice, problem-solving intuition, and runtime analysis. Synced directly from [LeetCode](https://leetcode.com).

---

## Goals & Practice Strategy

- **Consistency:** 1+ problem solved daily.
- **Complexity First:** Analyze time and space complexity before coding; optimize from brute force to optimal patterns.
- **Pattern Mastery:** Focus on core paradigms: Prefix/Suffix Products, Hash Maps, Two Pointers, Sliding Window, Monotonic Stacks, and Trees.

---

## Solved Problems Index

| Day |  #   | Problem                                                                                                                         | Topic            | Difficulty | Optimal Approach                                            |         Time          |      Space      |
| :-: | :--: | :------------------------------------------------------------------------------------------------------------------------------ | :--------------- | :--------: | :---------------------------------------------------------- | :-------------------: | :-------------: |
| 01  | 0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)                                                         | Arrays & Hashing |    Easy    | Hash Set Membership                                         |        $O(N)$         |     $O(N)$      |
| 02  | 0242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                                                                   | Arrays & Hashing |    Easy    | Frequency Array / Map                                       |        $O(N)$         |     $O(1)$      |
| 03  | 0001 | [Two Sum](https://leetcode.com/problems/two-sum/)                                                                               | Arrays & Hashing |    Easy    | One-Pass Hash Map                                           |        $O(N)$         |     $O(N)$      |
| 04  | 0049 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                                                                 | Arrays & Hashing |   Medium   | Categorize by Sorted Str / Char Count Tuple                 | $O(N \cdot K \log K)$ | $O(N \cdot K)$  |
| 05  | 0347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)                                               | Arrays & Hashing |   Medium   | Bucket Sort / Min-Heap                                      |        $O(N)$         |     $O(N)$      |
| 06  | 0238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)                                     | Arrays & Hashing |   Medium   | Prefix & Postfix Running Products                           |        $O(N)$         |    $O(1)^*$     |
| 07  | 0125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                                             | Two Pointers     |    Easy    | Two Pointers (Inward Scan with `isalnum`)                   |        $O(N)$         |     $O(1)$      |
| 08  | 0167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)                           | Two Pointers     |   Medium   | Two Pointers (Converging Left/Right Bounds)                 |        $O(N)$         |     $O(1)$      |
| 09  | 0344 | [Reverse String](https://leetcode.com/problems/reverse-string/)                                                                 | Two Pointers     |    Easy    | Two Pointers (In-place Swap)                                |        $O(N)$         |     $O(1)$      |
| 10  | 0283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/)                                                                       | Two Pointers     |    Easy    | Fast & Slow Pointers (In-place Partition)                   |        $O(N)$         |     $O(1)$      |
| 11  | 0027 | [Remove Element](https://leetcode.com/problems/remove-element/)                                                                 | Two Pointers     |    Easy    | Fast & Slow Pointers (In-place Overwrite)                   |        $O(N)$         |     $O(1)$      |
| 12  | 0026 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)                       | Two Pointers     |    Easy    | Fast & Slow Pointers (Unique Element Placement)             |        $O(N)$         |     $O(1)$      |
| 13  | 0977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)                                           | Two Pointers     |    Easy    | Two Pointers (Outward-in Absolute Comparison)               |        $O(N)$         |    $O(N)^*$     |
| 14  | 0643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)                                         | Sliding Window   |    Easy    | Fixed-Size Sliding Window                                   |        $O(N)$         |     $O(1)$      |
| 15  | 0209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)                                           | Sliding Window   |   Medium   | Dynamic-Size Sliding Window (Shrinking Bounds)              |        $O(N)$         |     $O(1)$      |
| 16  | 0003 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window   |   Medium   | Dynamic Sliding Window + Last Seen Index Map                |        $O(N)$         | $O(\min(N, M))$ |
| 17  | 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)                                             | Sliding Window   |   Medium   | Dynamic Sliding Window with Zero Counter ($k$ flips)        |        $O(N)$         |     $O(1)$      |
| 18  | 0141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)                                                           | Linked List      |    Easy    | Floyd's Cycle-Finding Algorithm (Tortoise & Hare)           |        $O(N)$         |     $O(1)$      |
| 19  | 0142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)                                                     | Linked List      |   Medium   | Floyd's Cycle-Finding Algorithm + Phase 2 Intersection Scan |        $O(N)$         |     $O(1)$      |

> _\*Note on #238 & #977: The output array does not count as extra space for complexity analysis._

---

## Repository Organization

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
│   ├── README.md
│   └── product-of-array-except-self.py
└── 0125-valid-palindrome/
│   ├── README.md
│   └── valid-palindrome.py
└── 0167-two-sum-ii-input-array-is-sorted/
│   ├── README.md
│   └── two-sum-ii-input-array-is-sorted.py
└── 0344-reverse-string/
│   ├── README.md
│   └── reverse-string.py
└── 0283-move-zeroes/
│   ├── README.md
│   └── move-zeroes.py
└── 0027-remove-element/
│   ├── README.md
│   └── remove-element.py
├── 0026-remove-duplicates-from-sorted-array/
│   ├── README.md
│   └── remove-duplicates-from-sorted-array.py
└── 0977-squares-of-a-sorted-array/
│   ├── README.md
│   └── squares-of-a-sorted-array.py
├── 0643-maximum-average-subarray-i/
│   ├── README.md
│   └── maximum-average-subarray-i.py
└── 0209-minimum-size-subarray-sum/
│   ├── README.md
│   └── minimum-size-subarray-sum.py
├── 0003-longest-substring-without-repeating-characters/
│   ├── README.md
│   └── longest-substring-without-repeating-characters.py
└── 1004-max-consecutive-ones-iii/
│   ├── README.md
│   └── max-consecutive-ones-iii.py
├── 0141-linked-list-cycle/
│   ├── README.md
│   └── linked-list-cycle.py
└── 0142-linked-list-cycle-ii/
│   ├── README.md
│   └── linked-list-cycle-ii.py
└── .gitignore
└── Pattern Cheat Sheet.md
└── README.md
```

## Setup & Tools

**Platform:** LeetCode

**Automation:** LeetSync / LeetHub v3 (automatic Git commits upon acceptance)

**Primary Language:** Python 3
