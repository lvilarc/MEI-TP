import os
import sys
import importlib.util
import subprocess
import json

def compile_check(file_path):
    """Checks for compilation/syntax errors."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, file_path, 'exec')
        return None  # No syntax errors
    except SyntaxError as e:
        return e
    except Exception as e:
        return e

def import_and_run(file_path, module_name):
    """Loads and executes the module, suppressing stdout."""
    # Redirect stdout
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        # Restore stdout
        sys.stdout.close()
        sys.stdout = original_stdout
        return module, None
    except Exception as e:
        sys.stdout = original_stdout
        return None, e

def evaluate_01():
    # 01.py: factorial(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/01.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_01")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'factorial'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'factorial'"
    fn = module.factorial
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        (0, 1), (1, 1), (2, 2), (5, 120), (12, 479001600), (-1, ValueError)
    ]
    for inp, expected in test_cases:
        try:
            if isinstance(expected, type) and issubclass(expected, Exception):
                try:
                    fn(inp)
                    failed += 1
                except expected:
                    passed += 1
                except Exception:
                    failed += 1
            else:
                res = fn(inp)
                if res == expected:
                    passed += 1
                else:
                    failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_02():
    # 02.py: fibonacci(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/02.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_02")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'fibonacci'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'fibonacci'"
    fn = module.fibonacci
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        (0, []), (1, [0]), (5, [0, 1, 1, 2, 3]), (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_03():
    # 03.py: bubble_sort(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/03.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_03")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'bubble_sort'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'bubble_sort'"
    fn = module.bubble_sort
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]), ([], []), ([1, 2, 3], [1, 2, 3]), ([3, 2, 1], [1, 2, 3])
    ]
    for inp, expected in test_cases:
        try:
            res = fn(list(inp))
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_04():
    # 04.py: binary_search(arr, x)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/04.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_04")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'binary_search'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'binary_search'"
    fn = module.binary_search
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        (([2, 3, 4, 10, 40], 10), 3), (([2, 3, 4, 10, 40], 2), 0), (([2, 3, 4, 10, 40], 40), 4), (([2, 3, 4, 10, 40], 99), -1)
    ]
    for (arr, x), expected in test_cases:
        try:
            res = fn(arr, x)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_05():
    # 05.py: is_palindrome(s)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/05.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_05")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'is_palindrome'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'is_palindrome'"
    fn = module.is_palindrome
    passed, failed, rterrs = 0, 0, 0
    # Note: GPT's implementation is case-insensitive, but does not strip punctuation/spaces.
    test_cases = [
        ("Racecar", True), ("Madam", True), ("Python", False), ("level", True)
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_06():
    # 06.py: multiply_3x3_matrices(a, b)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/06.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_06")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'multiply_3x3_matrices'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'multiply_3x3_matrices'"
    fn = module.multiply_3x3_matrices
    passed, failed, rterrs = 0, 0, 0
    
    # Valid multiply
    try:
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected = [[30.0, 24.0, 18.0], [84.0, 69.0, 54.0], [138.0, 114.0, 90.0]]
        res = fn(a, b)
        if res == expected:
            passed += 1
        else:
            failed += 1
    except Exception:
        failed += 1
        rterrs += 1
        
    # Invalid size
    try:
        fn([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        failed += 1
    except ValueError:
        passed += 1
    except Exception:
        failed += 1
        rterrs += 1
        
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_07():
    # 07.py: gcd(a, b)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/07.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_07")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'gcd'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'gcd'"
    fn = module.gcd
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        ((48, 18), 6), ((100, 75), 25), ((17, 13), 1)
    ]
    for (a, b), expected in test_cases:
        try:
            res = fn(a, b)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_08():
    # 08.py: is_prime(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/08.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_08")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'is_prime'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'is_prime'"
    fn = module.is_prime
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        (1, False), (2, True), (17, True), (18, False), (97, True), (0, False), (-5, False)
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_09():
    # 09.py: reverse_string_in_place(chars: list[str])
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/09.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_09")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'reverse_string_in_place'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'reverse_string_in_place'"
    fn = module.reverse_string_in_place
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        ("hello", "olleh"), ("Python", "nohtyP"), ("", "")
    ]
    for inp, expected in test_cases:
        try:
            chars_list = list(inp)
            fn(chars_list)
            res = "".join(chars_list)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_10():
    # 10.py: LinkedList
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/10.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_10")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'LinkedList'):
        return 100.0, False, 0, 1, 0, 1, "Missing class: 'LinkedList'"
    
    passed, failed, rterrs = 0, 0, 0
    try:
        ll = module.LinkedList([1, 2, 3, 4, 5])
        if ll.to_list() == [1, 2, 3, 4, 5]:
            passed += 1
        else:
            failed += 1
            
        ll.reverse()
        if ll.to_list() == [5, 4, 3, 2, 1]:
            passed += 1
        else:
            failed += 1
    except Exception:
        failed += 1
        rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_11():
    # 11.py: sum_digits(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/11.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_11")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'sum_digits'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'sum_digits'"
    fn = module.sum_digits
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        (123, 6), (0, 0), (-12, 3)
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_12():
    # 12.py: find_min_max(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/12.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_12")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'find_min_max'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'find_min_max'"
    fn = module.find_min_max
    passed, failed, rterrs = 0, 0, 0
    try:
        res = fn([23, 45, 12, 56, 78, 34])
        if res == (12, 78):
            passed += 1
        else:
            failed += 1
    except Exception:
        failed += 1
        rterrs += 1
    try:
        fn([])
        failed += 1
    except ValueError:
        passed += 1
    except Exception:
        failed += 1
        rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_13():
    # 13.py: are_anagrams(s1, s2)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/13.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_13")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'are_anagrams'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'are_anagrams'"
    fn = module.are_anagrams
    passed, failed, rterrs = 0, 0, 0
    # Note: GPT's implementation is case-sensitive.
    test_cases = [
        (("listen", "silent"), True), (("Race", "Care"), False), (("hello", "world"), False)
    ]
    for (s1, s2), expected in test_cases:
        try:
            res = fn(s1, s2)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_14():
    # 14.py: decimal_to_binary(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/14.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_14")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'decimal_to_binary'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'decimal_to_binary'"
    fn = module.decimal_to_binary
    passed, failed, rterrs = 0, 0, 0
    # Note: GPT raises ValueError for negative inputs
    test_cases = [
        (0, "0"), (10, "1010"), (255, "11111111"), (-5, ValueError)
    ]
    for inp, expected in test_cases:
        try:
            if isinstance(expected, type) and issubclass(expected, Exception):
                try:
                    fn(inp)
                    failed += 1
                except expected:
                    passed += 1
                except Exception:
                    failed += 1
            else:
                res = fn(inp)
                if res == expected:
                    passed += 1
                else:
                    failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_15():
    # 15.py: mean_and_median(numbers)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/15.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_15")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'mean_and_median'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'mean_and_median'"
    fn = module.mean_and_median
    passed, failed, rterrs = 0, 0, 0
    try:
        res = fn([3, 1, 4, 1, 5, 9, 2, 6])
        if res == (3.875, 3.5):
            passed += 1
        else:
            failed += 1
    except Exception:
        failed += 1
        rterrs += 1
    try:
        fn([])
        failed += 1
    except ValueError:
        passed += 1
    except Exception:
        failed += 1
        rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_16():
    # 16.py: remove_duplicates(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/16.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_16")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'remove_duplicates'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'remove_duplicates'"
    fn = module.remove_duplicates
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        ([4, 2, 7, 2, 4, 1, 7, 3], [4, 2, 7, 1, 3]), ([], [])
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_17():
    # 17.py: second_largest_unique(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/17.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_17")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'second_largest_unique'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'second_largest_unique'"
    fn = module.second_largest_unique
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        ([4, 1, 7, 3, 7, 4], 4), ([9, 9, 9], -1), ([10, 20, 30], 20), ([], -1)
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_18():
    # 18.py: count_vowels(s)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/18.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_18")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'count_vowels'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'count_vowels'"
    fn = module.count_vowels
    passed, failed, rterrs = 0, 0, 0
    test_cases = [
        ("Hello World", 3), ("aeiou", 5), ("bcdfg", 0)
    ]
    for inp, expected in test_cases:
        try:
            res = fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_19():
    # 19.py: JWT
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/19.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    module, run_err = import_and_run(file_path, "module_19")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error: {run_err}"
    if not hasattr(module, 'create_jwt') or not hasattr(module, 'verify_jwt'):
        return 100.0, False, 0, 1, 0, 1, "Missing functions create_jwt/verify_jwt"
    create_fn = module.create_jwt
    verify_fn = module.verify_jwt
    passed, failed, rterrs = 0, 0, 0
    try:
        header = '{"alg":"HS256","typ":"JWT"}'
        payload = '{"sub":"1234567890"}'
        secret = "secret"
        token = create_fn(header, payload, secret)
        if len(token.split('.')) == 3:
            passed += 1
        else:
            failed += 1
        if verify_fn(token, secret):
            passed += 1
        else:
            failed += 1
        if not verify_fn(token, "wrong_secret"):
            passed += 1
        else:
            failed += 1
        tampered = token[:-3] + "xyz"
        if not verify_fn(tampered, secret):
            passed += 1
        else:
            failed += 1
    except Exception:
        failed += 1
        rterrs += 1
    return 100.0, (failed == 0), passed, failed, 0, rterrs, ""

def evaluate_20():
    # 20.py: Graph AP / BCC
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/gpt/20.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
    graph_input = """8 a
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
"""
    res = subprocess.run([sys.executable, file_path], input=graph_input, capture_output=True, text=True)
    if res.returncode != 0:
        return 100.0, False, 0, 1, 0, 1, f"Execution failed: {res.stderr.strip()}"
    out = res.stdout.strip()
    passed, failed = 0, 0
    expected_substrings = [
        "Graph:",
        "[a]: b, c, h",
        "[b]: a, c, d, f, g",
        "[e]: f",
        "Parent",
        "[a]: a",
        "[b]: a",
        "Height",
        "[a]: 0",
        "[e]: 4",
        "Articulation Points",
        "[a]: True",
        "[c]: False",
        "Biconnected Components",
        "{e, f}",
        "{h, a}"
    ]
    for sub in expected_substrings:
        if sub in out:
            passed += 1
        else:
            if sub == "{e, f}" and ("{f, e}" in out or "{e, f}" in out):
                passed += 1
            elif sub == "{h, a}" and ("{a, h}" in out or "{h, a}" in out):
                passed += 1
            else:
                failed += 1
    return 100.0, (failed == 0), passed, failed, 0, 0, ""

def main():
    evaluators = {
        f"{str(i).zfill(2)}.py": globals()[f"evaluate_{str(i).zfill(2)}"] for i in range(1, 21)
    }
    results = {}
    for filename, fn in evaluators.items():
        try:
            success_rate, correctness, passed, failed, syntax_errs, runtime_errs, details = fn()
            results[filename] = {
                "success_rate": success_rate,
                "correctness": correctness,
                "passed": passed,
                "failed": failed,
                "syntax_errors": syntax_errs,
                "runtime_errors": runtime_errs,
                "details": details
            }
        except Exception as e:
            results[filename] = {
                "success_rate": 0.0,
                "correctness": False,
                "passed": 0,
                "failed": 0,
                "syntax_errors": 0,
                "runtime_errors": 1,
                "details": f"Test suite crashed: {e}"
            }
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
