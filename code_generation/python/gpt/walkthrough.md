# Evaluation Results Walkthrough (GPT Python)

We evaluated all files from `01.py` to `20.py` in the directory [gpt](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt).

Here is a summary of the metrics gathered.

---

## 📊 Summary Table of Results

| File | Execution Success Rate | Functional Correctness | Passed Tests | Failed Tests | Syntax Errors | Runtime Errors | Notes / Observações |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [01.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/01.py) | 100% | Correct | 6 | 0 | 0 | 0 | - |
| [02.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/02.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [03.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/03.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [04.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/04.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [05.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/05.py) | 100% | Correct | 4 | 0 | 0 | 0 | Palindrome check (does not ignore punctuation) |
| [06.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/06.py) | 100% | Correct | 2 | 0 | 0 | 0 | Corrected user placement error |
| [07.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/07.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [08.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/08.py) | 100% | Correct | 7 | 0 | 0 | 0 | - |
| [09.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/09.py) | 100% | Correct | 3 | 0 | 0 | 0 | Reverses a list of characters in-place |
| [10.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/10.py) | 100% | Correct | 2 | 0 | 0 | 0 | LinkedList class-bound reverse method |
| [11.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/11.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [12.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/12.py) | 100% | Correct | 2 | 0 | 0 | 0 | Empty list validation |
| [13.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/13.py) | 100% | Correct | 3 | 0 | 0 | 0 | Case-sensitive anagram verification |
| [14.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/14.py) | 100% | Correct | 4 | 0 | 0 | 0 | Restricts input to non-negative integers |
| [15.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/15.py) | 100% | Correct | 2 | 0 | 0 | 0 | Mean and median (returns tuple) |
| [16.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/16.py) | 100% | Correct | 2 | 0 | 0 | 0 | - |
| [17.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/17.py) | 100% | Correct | 4 | 0 | 0 | 0 | - |
| [18.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/18.py) | 100% | Correct | 3 | 0 | 0 | 0 | - |
| [19.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/19.py) | 100% | Correct | 4 | 0 | 0 | 0 | Minimal JWT (flat single file implementation) |
| [20.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/20.py) | 100% | Correct | 16 | 0 | 0 | 0 | DFS, Articulation Points, and BCC output |

---

## 🔍 Key Insights and Scope Differences

### 1. File Placement Correction of [06.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/06.py)
A vowel-counting script was originally copied into this slot due to a user copy-paste error. The correct GPT solution implementing [multiply_3x3_matrices](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/06.py#L5) has since been placed in `06.py`, and it compiles and runs correctly.

### 2. Palindrome Check [05.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/05.py) vs Claude
*   **GPT**: Implements basic lowercase normalization, but does not strip spaces or punctuation characters. (e.g. `"A man, a plan..."` is not marked as a palindrome).
*   **Claude**: Strips all non-alphanumeric characters, making it pass standard complex palindrome sentences.

### 3. In-place Reversal [09.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/09.py) vs Claude
*   **GPT**: The function `reverse_string_in_place(chars: list[str])` takes a mutable list of characters and modifies it in-place (returning `None`). Since Python strings are immutable, this is the most direct implementation of an "in-place" reversal.
*   **Claude**: Replaces the string by casting to list, reversing, and returning a new string string (`str -> str`).

### 4. Case Sensitivity in Anagrams [13.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/13.py) vs Claude
*   **GPT**: Case-sensitive and includes space/punctuation counts. (e.g., `are_anagrams("Race", "Care")` is `False`).
*   **Claude**: Case-insensitive (converts strings to lowercase).

### 5. Decimal to Binary [14.py](file:///W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/14.py) vs Claude
*   **GPT**: Restricts values to non-negative numbers and raises `ValueError` if `n < 0`.
*   **Claude**: Support negative decimals (e.g., `-5` returns `"-101"`).
