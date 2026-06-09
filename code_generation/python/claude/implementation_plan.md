# Evaluation of Python Files 02.py to 20.py

This plan outlines the approach to evaluate the remaining 19 Python files (`02.py` through `20.py`) in the `W:\MEI-UC-Repositorios\MEI\MEI-TP\code_generation\python\claude` directory.

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
> Some files require specialized evaluation because they do not expose a simple pure function or they depend on specific execution environments:
> - **`06.py`**: A matrix multiplication script using `numpy`. It will be evaluated by running the script and asserting that the stdout matches the expected matrix output.
> - **`10.py`**: Contains a runtime error by design/mistake in the Claude output (the class method `reverse_iterative` is defined at the module level rather than inside the class). We will verify that it compiles but fails with `AttributeError` at runtime.
> - **`19`**: A folder containing `script.py` and `minimal_jwt.py`. We will execute `script.py` and verify both standard execution success and functional behavior of the generated `minimal_jwt.py`.
> - **`20.py`**: A script that reads graph edges from standard input (`sys.stdin`). We will run it as a subprocess and pipe the standard example graph input into it, verifying that the output matches the expected articulation points and biconnected components.

---

## Proposed Changes

We will create a comprehensive, automated test runner script in the workspace scratch directory.

### Scratch Directory

#### [NEW] [test_all.py](file:///C:/Users/migue/.gemini/antigravity-ide/brain/05a8e524-9b66-4c33-9633-a673872f0919/scratch/test_all.py)
A single Python script that defines the test cases for each of the 19 files, executes the tests, catches compiler/runtime exceptions, aggregates the counts, and outputs a formatted markdown table.

---

## Test Suites & Verification Plan

Below are the test cases we will run for each file:

1. **`02.py`** (`fibonacci`):
   - `0` $\rightarrow$ `[]`
   - `1` $\rightarrow$ `[0]`
   - `2` $\rightarrow$ `[0, 1]`
   - `5` $\rightarrow$ `[0, 1, 1, 2, 3]`
   - `10` $\rightarrow$ `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

2. **`03.py`** (`bubble_sort_optimized`):
   - `[5, 1, 4, 2, 8]` $\rightarrow$ `[1, 2, 4, 5, 8]`
   - `[]` $\rightarrow$ `[]`
   - `[1, 2, 3]` $\rightarrow$ `[1, 2, 3]`
   - `[3, 2, 1]` $\rightarrow$ `[1, 2, 3]`

3. **`04.py`** (`binary_search`):
   - `([2, 3, 4, 10, 40], 10)` $\rightarrow$ `3`
   - `([2, 3, 4, 10, 40], 2)` $\rightarrow$ `0`
   - `([2, 3, 4, 10, 40], 40)` $\rightarrow$ `4`
   - `([2, 3, 4, 10, 40], 99)` $\rightarrow$ `-1`

4. **`05.py`** (`is_palindrome`):
   - `"Racecar"` $\rightarrow$ `True`
   - `"Madam"` $\rightarrow$ `True`
   - `"Python"` $\rightarrow$ `False`
   - `"A man, a plan, a canal, Panama"` $\rightarrow$ `True`

5. **`06.py`** (Numpy matrix multiplication):
   - Script execution output should match:
     `[[ 30  24  18]`
     ` [ 84  69  54]`
     ` [138 114  90]]`

6. **`07.py`** (`gcd`):
   - `(48, 18)` $\rightarrow$ `6`
   - `(100, 75)` $\rightarrow$ `25`
   - `(17, 13)` $\rightarrow$ `1`

7. **`08.py`** (`is_prime`):
   - `1` $\rightarrow$ `False`
   - `2` $\rightarrow$ `True`
   - `17` $\rightarrow$ `True`
   - `18` $\rightarrow$ `False`
   - `97` $\rightarrow$ `True`
   - `0` $\rightarrow$ `False`
   - `-5` $\rightarrow$ `False`

8. **`09.py`** (`reverse_string_in_place`):
   - `"hello"` $\rightarrow$ `"olleh"`
   - `"Python"` $\rightarrow$ `"nohtyP"`
   - `""` $\rightarrow$ `""`

9. **`10.py`** (`LinkedList`):
   - Executing the script should fail at runtime due to the method `reverse_iterative` being placed outside the class `LinkedList` (AttributeError).

10. **`11.py`** (`digit_sum`):
    - `123` $\rightarrow$ `6`
    - `0` $\rightarrow$ `0`
    - `-12` $\rightarrow$ `3`

11. **`12.py`** (`find_min_max`):
    - `[23, 45, 12, 56, 78, 34]` $\rightarrow$ `(12, 78)`
    - `[]` $\rightarrow$ `ValueError`

12. **`13.py`** (`are_anagrams`):
    - `("listen", "silent")` $\rightarrow$ `True`
    - `("Race", "Care")` $\rightarrow$ `True`
    - `("hello", "world")` $\rightarrow$ `False`

13. **`14.py`** (`decimal_to_binary`):
    - `0` $\rightarrow$ `"0"`
    - `10` $\rightarrow$ `"1010"`
    - `255` $\rightarrow$ `"11111111"`
    - `-5` $\rightarrow$ `"-101"`

14. **`15.py`** (`calculate_stats`):
    - `[3, 1, 4, 1, 5, 9, 2, 6]` $\rightarrow$ `{"mean": 3.875, "median": 3.5}`
    - `[]` $\rightarrow$ `ValueError`

15. **`16.py`** (`remove_duplicates`):
    - `[4, 2, 7, 2, 4, 1, 7, 3]` $\rightarrow$ `[4, 2, 7, 1, 3]`
    - `[]` $\rightarrow$ `[]`

16. **`17.py`** (`second_largest`):
    - `[4, 1, 7, 3, 7, 4]` $\rightarrow$ `4`
    - `[9, 9, 9]` $\rightarrow$ `-1`
    - `[10, 20, 30]` $\rightarrow$ `20`
    - `[]` $\rightarrow$ `-1`

17. **`18.py`** (`count_vowels`):
    - `"Hello World"` $\rightarrow$ `3`
    - `"aeiou"` $\rightarrow$ `5`
    - `"bcdfg"` $\rightarrow$ `0`

18. **`19`** (JWT):
    - Execute `script.py` which generates `minimal_jwt.py`.
    - Verify that generated functions can encode/decode JWTs.

19. **`20.py`** (Graph DFS / Articulation Points / BCC):
    - Run the script as a subprocess.
    - Provide the graph from the example input:
      ```
      8 a
      a b
      a c
      a h
      b c
      b d
      b f
      b g
      c g
      d f
      e f
      ```
    - Verify that output matches the expected DFS traversal structure (Parent, Height, Articulation Points, Biconnected Components).
