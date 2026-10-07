## 1. Reverse Array / String (In-Place) (Leetcode #344)

- **Pattern:** Two Pointers (Opposite Ends)
- **Trigger:** Need to reverse a sequence in-place with O(1) extra memory.
- **Core Logic:**
  - Place `left = 0` and `right = len(s) - 1`.
  - While `left < right`, swap `s[left]` and `s[right]`.
  - Increment `left += 1`, decrement `right -= 1`.
  - Stop when pointers meet in the middle (`left >= right`).
- **Complexity:** Time: O(n) | Space: O(1)

## 2. Move Zeroes (In - Place) (Leetcode #283)

- **Pattern:** Two Pointers (Slow & Fast / Read & Write)
- **Trigger:** Need to filter or rearrange elements in-place while keeping relative order.
- **Core Logic:**
  - `write = 0` (points to where the next element go)
  - Loop `read` across the array:
    - If `nums[read] != 0`:
      - Swap `nums[write]` and `nums[read]`
      - Increment `write += 1`

* **Complexity:** Time: O(n) | Space: O(1)

## 3. Remove Element (In-Place Filter) (Leetcode #27)

- **Pattern:** Two Pointers (Slow & Fast / Read & Write)
- **Trigger:** Overwrite / remove matching elements in-place and return the count.
- **Core Logic:**
  - `write = 0`
  - Loop `read` over array:
    - If `nums[read] != val`:
      - `nums[write] = nums[read]`
      - `write += 1`
  - Return `write`
- **Complexity:** Time: O(n) | Space: O(1)

## 4. Remove Duplicates from Sorted Array (In-Place) (Leetcode #26)

- **Pattern:** Two Pointers (Slow & Fast / Read & Write)
- **Trigger:** Array is sorted, need to keep only unique elements in-place with O(1) space.
- **Core Logic:**
  - `write = 1` (index 0 is already unique)
  - Loop `read` from index 1 to end:
    - If `nums[read] != nums[read - 1]`:
      - `nums[write] = nums[read]`
      - `write += 1`
  - Return `write`
- **Complexity:** Time: O(n) | Space: O(1)

## 5. Squares of a Sorted Array (Leetcode #977)

- **Pattern:** Two Pointers (Opposite Ends, Filling Backward)
- **Trigger:** Array has negative and positive numbers sorted; need sorted squares in O(n) without calling sort().
- **Core Logic:**
  - The largest squares live at the outer edges (far left or far right).
  - Place `left = 0`, `right = n - 1`.
  - Fill result array from index `n - 1` down to `0`.
  - Compare `nums[left]**2` vs `nums[right]**2`; place the larger square at `pos` and move that pointer inward.
- **Complexity:** Time: O(n) | Space: O(n) (output array)

## 6. Valid Palindrome (LeetCode #125)

- **Pattern:** Two Pointers (Opposite Ends)
- **Trigger:** String symmetry check karni ho aur non-alphanumeric characters ko ignore karna ho.
- **Core Logic:**
  - `left = 0`, `right = len(s) - 1`.
  - Inner while loop se dono sides ke non-alphanumeric characters skip karo (`not char.isalnum()`).
  - Dono characters ko lowercase mein compare karo; agar mismatch mile toh return `False`.
  - Match hone par `left += 1` aur `right -= 1`.
  - Loop complete hone par return `True`.
- **Complexity:** Time: O(n) | Space: O(1)

## 7. Two Sum II - Input Array Is Sorted (LeetCode #167)

- **Pattern:** Two Pointers (Opposite Ends)
- **Trigger:** Array pehle se sorted hai aur target sum banane wale 2 numbers ke 1-based indices chahiye O(1) space mein.
- **Core Logic:**
  - `left = 0`, `right = len(numbers) - 1`.
  - `total = numbers[left] + numbers[right]`.
  - Agar `total == target`: return `[left + 1, right + 1]`.
  - Agar `total > target`: sum kam karne ke liye `right -= 1`.
  - Agar `total < target`: sum badhane ke liye `left += 1`.
- **Complexity:** Time: O(n) | Space: O(1)

## 8. Two Sum (LeetCode #1)

- **Pattern:** Hash Map (Single Pass Lookup)
- **Trigger:** Unsorted array mein 2 numbers ka target sum dhundhna ho O(n) time mein.
- **Core Logic:**
  - Ek empty hash map banao: `seen = {}`.
  - Har element `x` ke liye `diff = target - x` calculate karo.
  - Agar `diff` pehle se `seen` mein hai, toh `[seen[diff], current_index]` return kar do.
  - Warna `seen[x] = current_index` store karo.
- **Complexity:** Time: O(n) | Space: O(n)

## 9. Contains Duplicate (LeetCode #217)

- **Pattern:** Hash Set
- **Trigger:** Check karna ho ki array mein koi element ek se zyada baar repeat hua hai ya nahi.
- **Core Logic:**
  - Ek empty set banao: `seen = set()`.
  - Har number ke liye check karo: agar `num in seen` ho toh turant `True` return karo.
  - Warna `seen.add(num)`.
  - Pura loop khatam hone par return `False` (ya fir `len(nums) != len(set(nums))` check karo).
- **Complexity:** Time: O(n) | Space: O(n)

## 10. Valid Anagram (LeetCode #242)

- **Pattern:** Hash Map / Frequency Counting
- **Trigger:** Check karna ho ki do strings mein exact same characters aur same frequencies hain ya nahi.
- **Core Logic:**
  - Pehle length check karo: agar `len(s) != len(t)` toh return `False`.
  - Ek frequency count dictionary banao: string `s` ke chars ka count badhao (`+1`) aur string `t` ke chars ka count ghatao (`-1`).
  - Agar saare counts `0` bachte hain, toh strings anagrams hain (`True`).
- **Complexity:** Time: O(n) | Space: O(1) (kyunki total 26 lowercase alphabets hi hote hain)

## 11. Group Anagrams (LeetCode #49)

- **Pattern:** Hash Map with Categorization Key
- **Trigger:** Anagram words ko ek sath group/list mein collect karna ho.
- **Core Logic:**
  - Ek dictionary banao: `groups = defaultdict(list)`.
  - Har word ke liye sorted string (jaise `''.join(sorted(word))`) ya 26-element frequency tuple ko dictionary ka `key` banao.
  - Us key ke andar original word append karo: `groups[key].append(word)`.
  - Aakhiri mein `list(groups.values())` return karo.
- **Complexity:** Time: O(m _ n log n) ya O(m _ n) (m = words count, n = max word length) | Space: O(m \* n)

## 12. Top K Frequent Elements (LeetCode #347)

- **Pattern:** Frequency Map + Bucket Sort
- **Trigger:** Sabse zyada aane wale `k` elements return karne hon O(n) ya O(n log k) time mein.
- **Core Logic:**
  - Har element ka count nikalne ke liye frequency hash map banao (`Counter(nums)`).
  - Bucket sort use karo: size `len(nums) + 1` ki list of lists banao, jahan `index` frequency batata hai aur list mein wo numbers aate hain.
  - Bucket ko peeche se (highest frequency se) scan karke pehle `k` elements result mein bharo.
- **Complexity:** Time: O(n) | Space: O(n)

## 13. Product of Array Except Self (LeetCode #238)

- **Pattern:** Prefix & Suffix Products
- **Trigger:** Har element ke liye baaki sabhi numbers ka product chahiye bina division (`/`) operator use kiye aur O(n) time mein.
- **Core Logic:**
  - `left` array banao: index `i` ke left ke saare elements ka cumulative product store karo.
  - `right` array banao: index `i` ke right ke saare elements ka cumulative product store karo (peeche se iterate karke).
  - Final result: har index par `ans[i] = left[i] * right[i]`.
- **Complexity:** Time: O(n) | Space: O(n) (ya O(1) extra space agar output array ke andar hi right product calculate kar liya jaye)

## 14. Maximum Average Subarray I (LeetCode #643)

- **Pattern:** Sliding Window (Fixed Size)
- **Trigger:** Contiguous subarray of a fixed length `k` requiring maximum/minimum sum or average.
- **Core Logic:**
  - Calculate initial sum of the first `k` elements: `window_sum = sum(nums[:k])`.
  - Loop `i` from `k` to `len(nums) - 1`:
    - Slide window: `window_sum += nums[i] - nums[i - k]`.
    - Update max: `max_sum = max(max_sum, window_sum)`.
  - Return `max_sum / k`.
- **Complexity:** Time: O(n) | Space: O(1)

## 15. Minimum Size Subarray Sum (LeetCode #209)

- **Pattern:** Sliding Window (Dynamic / Variable Size)
- **Trigger:** Smallest contiguous subarray satisfying a condition (sum >= target).
- **Core Logic:**
  - `left = 0`, `current_sum = 0`, `min_length = infinity`.
  - Loop `right` across the array and add `nums[right]` to `current_sum`.
  - While `current_sum >= target`:
    - Record length: `min_length = min(min_length, right - left + 1)`.
    - Shrink window: `current_sum -= nums[left]`, then `left += 1`.
  - Return `min_length` (or `0` if impossible).
- **Complexity:** Time: O(n) | Space: O(1)
