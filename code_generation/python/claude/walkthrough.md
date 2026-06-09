# Evaluation Results Walkthrough (02.py to 20.py)

We evaluated all files from `02.py` to `20.py` in the directory [claude](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude).

Here is a summary of the metrics gathered.

---

## 📊 Summary Table of Results

| File | Execution Success Rate | Functional Correctness | Passed Tests | Failed Tests | Syntax Errors | Runtime Errors | Notes / Errors |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [02.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/02.py) | 100% | Correct | 5 | 0 | 0 | 0 | - |
| [03.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/03.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [04.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/04.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [05.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/05.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [06.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/06.py) | 100% | Correct | 1 | 0 | 0 | 0 | Verified script stdout matrix output |
| [07.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/07.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [08.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/08.py) | 100% | Correct | 7 | 0 | 0 | 0 | - |
| [09.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/09.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [10.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/10.py) | 100% | Incorrect | 0 | 1 | 0 | 1 | **Runtime Error**: `AttributeError` (method `reverse_iterative` defined at module scope) |
| [11.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/11.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [12.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/12.py) | 100% | Correct | 2 | 0 | 0 | 0 | Verified empty list exception |
| [13.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/13.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [14.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/14.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [15.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/15.py) | 100% | Correct | 2 | 0 | 0 | 0 | Verified empty list exception |
| [16.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/16.py) | 100% | Correct | 2 | 0 | 0 | 0 | - |
| [17.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/17.py) | 100% | Correct | 5 | 0 | 0 | 0 | - |
| [18.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/18.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [19/script.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/19/script.py) | 0% / 100% | Incorrect / Correct | 0 / 4 | 1 / 0 | 0 | 1 / 0 | **Windows default locale error**: crashes with `UnicodeEncodeError` (default CP1252 cannot write unicode box/marks). Runs and passes all tests if `PYTHONUTF8=1` is set. |
| [20.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/20.py) | 100% | Correct | 16 | 0 | 0 | 0 | Verified DFS tree structure, APs, and BCC output |

---

## 🔍 Detailed Analysis of Failures

### 1. [10.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/10.py) — LinkedList Reverse
This file implements a linked list node, a LinkedList class, and a function to reverse the list.
*   **The Issue**: The `reverse_iterative` function is defined at the global module level (with `self` as a parameter) instead of being inside the `LinkedList` class block:
    ```python
    # Line 30:
    def reverse_iterative(self):
        # ...
    ```
*   **Result**: When the script attempts to call `ll.reverse_iterative()`, it raises:
    `AttributeError: 'LinkedList' object has no attribute 'reverse_iterative'`.

### 2. [19 (dir)](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/19) — Minimal JWT System
This folder contains `script.py` which outputs `minimal_jwt.py`.
*   **The Issue**: The script writes a code block to disk using:
    ```python
    with open("minimal_jwt.py", "w") as f:
        f.write(jwt_code)
    ```
    Since `jwt_code` contains UTF-8 characters (like box drawing symbols and checkmarks) and no `encoding="utf-8"` is specified in `open()`, it crashes with a `UnicodeEncodeError` under Windows when using standard default file open encodings (e.g., CP1252).
*   **Result**: In a standard Windows environment, it throws:
    `UnicodeEncodeError: 'charmap' codec can't encode characters in position 280-324: character maps to <undefined>`.
    Setting `PYTHONUTF8=1` makes the script pass 100%.
