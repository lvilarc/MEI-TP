# Evaluation of GPT Python Files (01.py to 20.py)

This plan outlines the approach to evaluate the Python files (`01.py` through `20.py`) in the `W:\MEI-UC-Repositorios\MEI\MEI-TP\code_generation\python\gpt` directory.

We will measure:
- Compilation or execution success rate
- Functional correctness
- Number of passed tests
- Number of failed tests
- Number of syntax errors
- Number of runtime errors

---

## User Review Required

> [!NOTE]
> - **`20.py`**: A script that reads graph edges from standard input (`sys.stdin`). We will run it as a subprocess and pipe the standard example graph input into it, verifying that the output matches the expected articulation points and biconnected components.

---

## Proposed Changes

We will create a new automated test runner script in the workspace scratch directory.

### Scratch Directory

#### [NEW] [test_all_gpt.py](file:///C:/Users/migue/.gemini/antigravity-ide/brain/05a8e524-9b66-4c33-9633-a673872f0919/scratch/test_all_gpt.py)
A single Python script that defines the test cases for each of the 20 files in `gpt/`, executes the tests, catches compiler/runtime exceptions, aggregates the counts, and outputs a formatted json/markdown summary.

---

## Test Suites & Verification Plan

Below are the test cases we will run for each file:

1. **`01.py`** (`factorial`):
   - `0` $\rightarrow$ `1`
   - `1` $\rightarrow$ `1`
   - `5` $\rightarrow$ `120`
   - `12` $\rightarrow$ `479001600`
   - `-1` $\rightarrow$ raises `ValueError`

2. **`02.py`** (`fibonacci`):
   - `0` $\rightarrow$ `[]`
   - `1` $\rightarrow$ `[0]`
   - `5` $\rightarrow$ `[0, 1, 1, 2, 3]`
   - `10` $\rightarrow$ `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

3. **`03.py`** (`bubble_sort`):
   - `[5, 1, 4, 2, 8]` $\rightarrow$ `[1, 2, 4, 5, 8]`
   - `[]` $\rightarrow$ `[]`

4. **`04.py`** (`binary_search`):
   - `([2, 3, 4, 10, 40], 10)` $\rightarrow$ `3`
   - `([2, 3, 4, 10, 40], 99)` $\rightarrow$ `-1`

5. **`05.py`** (`is_palindrome`):
   - `"Racecar"` $\rightarrow$ `True`
   - `"Python"` $\rightarrow$ `False`

6. **`06.py`** (`multiply_3x3_matrices`):
   - `([[1,2,3], [4,5,6], [7,8,9]], [[9,8,7], [6,5,4], [3,2,1]])` $\rightarrow$ `[[30, 24, 18], [84, 69, 54], [138, 114, 90]]`
   - Invalid size matrices $\rightarrow$ raises `ValueError`

7. **`07.py`** (`gcd`):
   - `(48, 18)` $\rightarrow$ `6`
   - `(100, 75)` $\rightarrow$ `25`

8. **`08.py`** (`is_prime`):
   - `1` $\rightarrow$ `False`
   - `2` $\rightarrow$ `True`
   - `17` $\rightarrow$ `True`
   - `18` $\rightarrow$ `False`

9. **`09.py`** (`reverse_string_in_place`):
   - `"hello"` $\rightarrow$ `"olleh"`
   - `"Python"` $\rightarrow$ `"nohtyP"`
   - `""` $\rightarrow$ `""`

10. **`10.py`** (`LinkedList`):
    - Initialize `LinkedList([1, 2, 3, 4, 5])`.
    - Run `.reverse()`.
    - `.to_list()` should return `[5, 4, 3, 2, 1]`.

11. **`11.py`** (`sum_digits`):
    - `123` $\rightarrow$ `6`
    - `0` $\rightarrow$ `0`
    - `-12` $\rightarrow$ `3`

12. **`12.py`** (`find_min_max`):
    - `[23, 45, 12, 56, 78, 34]` $\rightarrow$ `(12, 78)`
    - `[]` $\rightarrow$ raises `ValueError`

13. **`13.py`** (`are_anagrams`):
    - `("listen", "silent")` $\rightarrow$ `True`
    - `("hello", "world")` $\rightarrow$ `False`

14. **`14.py`** (`decimal_to_binary`):
    - `0` $\rightarrow$ `"0"`
    - `10` $\rightarrow$ `"1010"`
    - `255` $\rightarrow$ `"11111111"`

15. **`15.py`** (`mean_and_median`):
    - `[3, 1, 4, 1, 5, 9, 2, 6]` $\rightarrow$ `(3.875, 3.5)`
    - `[]` $\rightarrow$ raises `ValueError`

16. **`16.py`** (`remove_duplicates`):
    - `[4, 2, 7, 2, 4, 1, 7, 3]` $\rightarrow$ `[4, 2, 7, 1, 3]`

17. **`17.py`** (`second_largest_unique`):
    - `[5, 1, 3, 5, 2]` $\rightarrow$ `3`
    - `[4, 4, 4]` $\rightarrow$ `-1`
    - `[]` $\rightarrow$ `-1`

18. **`18.py`** (`count_vowels`):
    - `"Hello World"` $\rightarrow$ `3`
    - `"aeiou"` $\rightarrow$ `5`

19. **`19.py`** (JWT):
    - Verify manual SHA-256 and base64url encoding.
    - `create_jwt` and `verify_jwt` with correct, wrong and tampered inputs.

20. **`20.py`** (Graph DFS / AP / BCC):
    - Run script with example graph via standard input.
    - Verify correct output matches expected DFS tree, parent maps, heights, articulation points, and BCCs.
