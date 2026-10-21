# Valid Sudoku

**Topic:** Arrays & Hashing  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Valid Sudoku — NeetCode](https://neetcode.io/problems/valid-sudoku)

## My Approach

In this problem, I need to check whether a Sudoku board is valid. I don't need to solve the Sudoku puzzle; I just need to check whether any number is repeated in the same row, column, or 3×3 box.

I used **sets and dictionaries** to keep track of the numbers I've already seen.

### How I Solved It

I created three dictionaries using `defaultdict(set)`:

- `rows` to store the numbers in each row.
- `cols` to store the numbers in each column.
- `sq` to store the numbers in each 3×3 box.

Then I went through every cell in the 9×9 board.

1. If the cell contains `"."`, I skipped it because it's an empty cell.
2. I calculated which 3×3 box the cell belongs to using `(r // 3, c // 3)`.
3. Before adding the number, I checked whether it was already present in that row, column, or box.
4. If the number was already present in any of them, I returned `False`.
5. Otherwise, I added it to all three sets.

If I finish checking every cell without finding a duplicate, I return `True`.

The useful thing about sets is that I can quickly check whether a number already exists instead of comparing it with every other number in the row, column, or box.

## Time and Space Complexity

Since the Sudoku board is always 9×9:

- **Time:** `O(1)` — the board has a fixed number of 81 cells.
- **Space:** `O(1)` — the sets store numbers from a fixed-size board.

If the board size were generalized to `n × n`, the time and space complexity would typically be expressed in terms of `n`.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Sets are useful for checking duplicates efficiently.
- I can use separate sets to track constraints such as rows, columns, and boxes.
- Integer division with `// 3` helps identify which 3×3 box a cell belongs to.
- I only need to check whether the current board is valid; I don't need to fill in the empty cells.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why I used `(r // 3, c // 3)` to identify each box.
- [ ] Test cases with duplicate numbers in a row, column, and box.
- [ ] Explain why empty cells are skipped.
- [ ] Explain the time and space complexity in my own words.

---

*Another DSA problem completed. I'm trying to understand why each data structure works, so I can use the same ideas in other problems.*
