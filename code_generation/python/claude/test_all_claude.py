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

def evaluate_02():
    # 02.py: fibonacci(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/02.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_02")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'fibonacci'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'fibonacci'"
        
    fib_fn = module.fibonacci
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    ]
    for inp, expected in test_cases:
        try:
            res = fib_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_03():
    # 03.py: bubble_sort_optimized(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/03.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_03")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'bubble_sort_optimized'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'bubble_sort_optimized'"
        
    sort_fn = module.bubble_sort_optimized
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3])
    ]
    for inp, expected in test_cases:
        try:
            # We copy list because sorting can be in-place
            res = sort_fn(list(inp))
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_04():
    # 04.py: binary_search(arr, x)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/04.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_04")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'binary_search'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'binary_search'"
        
    bs_fn = module.binary_search
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        (([2, 3, 4, 10, 40], 10), 3),
        (([2, 3, 4, 10, 40], 2), 0),
        (([2, 3, 4, 10, 40], 40), 4),
        (([2, 3, 4, 10, 40], 99), -1)
    ]
    for (arr, x), expected in test_cases:
        try:
            res = bs_fn(arr, x)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_05():
    # 05.py: is_palindrome(s)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/05.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_05")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'is_palindrome'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'is_palindrome'"
        
    pal_fn = module.is_palindrome
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ("Racecar", True),
        ("Madam", True),
        ("Python", False),
        ("A man, a plan, a canal, Panama", True)
    ]
    for inp, expected in test_cases:
        try:
            res = pal_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_06():
    # 06.py: Numpy matrix multiplication (executed as script)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/06.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    # Run as subprocess
    res = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
    if res.returncode != 0:
        return 100.0, False, 0, 1, 0, 1, f"Execution failed: {res.stderr.strip()}"
        
    # Check that output has correct matrix shape/values
    # Expected output contains:
    # [[ 30  24  18]
    #  [ 84  69  54]
    #  [138 114  90]]
    out = res.stdout.strip()
    passed = 0
    failed = 0
    
    if "30" in out and "24" in out and "18" in out and "84" in out and "69" in out and "54" in out and "138" in out and "114" in out and "90" in out:
        passed = 1
    else:
        failed = 1
        
    return 100.0, (failed == 0), passed, failed, 0, 0, ""

def evaluate_07():
    # 07.py: gcd(a, b)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/07.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_07")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'gcd'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'gcd'"
        
    gcd_fn = module.gcd
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ((48, 18), 6),
        ((100, 75), 25),
        ((17, 13), 1)
    ]
    for (a, b), expected in test_cases:
        try:
            res = gcd_fn(a, b)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_08():
    # 08.py: is_prime(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/08.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_08")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'is_prime'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'is_prime'"
        
    prime_fn = module.is_prime
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        (1, False),
        (2, True),
        (17, True),
        (18, False),
        (97, True),
        (0, False),
        (-5, False)
    ]
    for inp, expected in test_cases:
        try:
            res = prime_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_09():
    # 09.py: reverse_string_in_place(s)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/09.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_09")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'reverse_string_in_place'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'reverse_string_in_place'"
        
    rev_fn = module.reverse_string_in_place
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("", "")
    ]
    for inp, expected in test_cases:
        try:
            res = rev_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_10():
    # 10.py: LinkedList
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/10.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    # Run as subprocess to see if it executes correctly
    res = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
    if res.returncode != 0:
        # Expected failure since reverse_iterative is defined outside LinkedList
        return 100.0, False, 0, 1, 0, 1, f"Expected runtime error occurred: {res.stderr.strip()}"
    else:
        return 100.0, True, 1, 0, 0, 0, ""

def evaluate_11():
    # 11.py: digit_sum(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/11.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_11")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'digit_sum'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'digit_sum'"
        
    ds_fn = module.digit_sum
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        (123, 6),
        (0, 0),
        (-12, 3)
    ]
    for inp, expected in test_cases:
        try:
            res = ds_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_12():
    # 12.py: find_min_max(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/12.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_12")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'find_min_max'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'find_min_max'"
        
    mm_fn = module.find_min_max
    passed = 0
    failed = 0
    runtime_errs = 0
    
    # Check regular case
    try:
        res = mm_fn([23, 45, 12, 56, 78, 34])
        if res == (12, 78):
            passed += 1
        else:
            failed += 1
    except Exception as e:
        failed += 1
        runtime_errs += 1
        
    # Check empty list raises ValueError
    try:
        mm_fn([])
        failed += 1
    except ValueError:
        passed += 1
    except Exception as e:
        failed += 1
        runtime_errs += 1
        
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_13():
    # 13.py: are_anagrams(s1, s2)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/13.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_13")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'are_anagrams'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'are_anagrams'"
        
    an_fn = module.are_anagrams
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        (("listen", "silent"), True),
        (("Race", "Care"), True),
        (("hello", "world"), False)
    ]
    for (s1, s2), expected in test_cases:
        try:
            res = an_fn(s1, s2)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_14():
    # 14.py: decimal_to_binary(n)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/14.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_14")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'decimal_to_binary'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'decimal_to_binary'"
        
    db_fn = module.decimal_to_binary
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        (0, "0"),
        (10, "1010"),
        (255, "11111111"),
        (-5, "-101")
    ]
    for inp, expected in test_cases:
        try:
            res = db_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_15():
    # 15.py: calculate_stats(numbers)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/15.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_15")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'calculate_stats'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'calculate_stats'"
        
    cs_fn = module.calculate_stats
    passed = 0
    failed = 0
    runtime_errs = 0
    
    # Case 1
    try:
        res = cs_fn([3, 1, 4, 1, 5, 9, 2, 6])
        if res == {"mean": 3.875, "median": 3.5}:
            passed += 1
        else:
            failed += 1
    except Exception as e:
        failed += 1
        runtime_errs += 1
        
    # Case 2: Empty list
    try:
        cs_fn([])
        failed += 1
    except ValueError:
        passed += 1
    except Exception as e:
        failed += 1
        runtime_errs += 1
        
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_16():
    # 16.py: remove_duplicates(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/16.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_16")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'remove_duplicates'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'remove_duplicates'"
        
    rd_fn = module.remove_duplicates
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ([4, 2, 7, 2, 4, 1, 7, 3], [4, 2, 7, 1, 3]),
        ([], [])
    ]
    for inp, expected in test_cases:
        try:
            res = rd_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_17():
    # 17.py: second_largest(arr)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/17.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_17")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'second_largest'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'second_largest'"
        
    sl_fn = module.second_largest
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ([4, 1, 7, 3, 7, 4], 4),
        ([9, 9, 9], -1),
        ([10, 20, 30], 20),
        ([5], -1),
        ([], -1)
    ]
    for inp, expected in test_cases:
        try:
            res = sl_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_18():
    # 18.py: count_vowels(s)
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/18.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    module, run_err = import_and_run(file_path, "module_18")
    if run_err:
        return 100.0, False, 0, 0, 0, 1, f"Runtime Error during import: {run_err}"
        
    if not hasattr(module, 'count_vowels'):
        return 100.0, False, 0, 1, 0, 1, "Missing function: 'count_vowels'"
        
    cv_fn = module.count_vowels
    passed = 0
    failed = 0
    runtime_errs = 0
    
    test_cases = [
        ("Hello World", 3),
        ("aeiou", 5),
        ("bcdfg", 0)
    ]
    for inp, expected in test_cases:
        try:
            res = cv_fn(inp)
            if res == expected:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            runtime_errs += 1
            
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_19():
    # 19: script.py & minimal_jwt.py
    script_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/19/script.py"
    jwt_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/19/minimal_jwt.py"
    
    # Check syntax of script.py
    syntax_err = compile_check(script_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error in script.py: {syntax_err}"
        
    # Run script.py as a subprocess to output/generate minimal_jwt.py
    # Change working directory so it writes in its own directory
    res = subprocess.run([sys.executable, script_path], capture_output=True, text=True, cwd=os.path.dirname(script_path))
    if res.returncode != 0:
        return 100.0, False, 0, 1, 0, 1, f"script.py failed to execute: {res.stderr.strip()}"
        
    # Check syntax of generated minimal_jwt.py
    jwt_syntax = compile_check(jwt_path)
    if jwt_syntax:
        return 100.0, False, 0, 1, 1, 0, f"Syntax Error in minimal_jwt.py: {jwt_syntax}"
        
    # Import and test minimal_jwt.py
    module, run_err = import_and_run(jwt_path, "module_jwt")
    if run_err:
        return 100.0, False, 0, 1, 0, 1, f"minimal_jwt.py failed to load: {run_err}"
        
    if not hasattr(module, 'create_jwt') or not hasattr(module, 'verify_jwt'):
        return 100.0, False, 0, 1, 0, 1, "Missing functions create_jwt/verify_jwt in minimal_jwt.py"
        
    create_fn = module.create_jwt
    verify_fn = module.verify_jwt
    
    passed = 0
    failed = 0
    runtime_errs = 0
    
    try:
        header = '{"alg":"HS256","typ":"JWT"}'
        payload = '{"sub":"1234567890"}'
        secret = "secret"
        
        token = create_fn(header, payload, secret)
        if len(token.split('.')) == 3:
            passed += 1
        else:
            failed += 1
            
        # Verify valid
        if verify_fn(token, secret):
            passed += 1
        else:
            failed += 1
            
        # Verify wrong secret
        if not verify_fn(token, "wrong_secret"):
            passed += 1
        else:
            failed += 1
            
        # Verify tampered
        tampered = token[:-3] + "xyz"
        if not verify_fn(tampered, secret):
            passed += 1
        else:
            failed += 1
            
    except Exception as e:
        failed += 1
        runtime_errs += 1
        
    return 100.0, (failed == 0), passed, failed, 0, runtime_errs, ""

def evaluate_20():
    # 20.py: Graph AP / BCC
    file_path = "W:/MEI-UC-Repositorios/MEI/MEI-TP/code_generation/python/claude/20.py"
    syntax_err = compile_check(file_path)
    if syntax_err:
        return 0.0, False, 0, 0, 1, 0, f"Syntax Error: {syntax_err}"
        
    # Example graph input
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
    # Execute as subprocess and pipe standard input
    res = subprocess.run([sys.executable, file_path], input=graph_input, capture_output=True, text=True)
    if res.returncode != 0:
        return 100.0, False, 0, 1, 0, 1, f"Execution failed: {res.stderr.strip()}"
        
    out = res.stdout.strip()
    passed = 0
    failed = 0
    
    # Check for crucial parts of output:
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
            # Check for alternative spacing/ordering for BCC sets
            # e.g., {f, e} instead of {e, f}
            if sub == "{e, f}" and ("{f, e}" in out or "{e, f}" in out):
                passed += 1
            elif sub == "{h, a}" and ("{a, h}" in out or "{h, a}" in out):
                passed += 1
            else:
                failed += 1
                
    return 100.0, (failed == 0), passed, failed, 0, 0, ""

def main():
    evaluators = {
        "02.py": evaluate_02,
        "03.py": evaluate_03,
        "04.py": evaluate_04,
        "05.py": evaluate_05,
        "06.py": evaluate_06,
        "07.py": evaluate_07,
        "08.py": evaluate_08,
        "09.py": evaluate_09,
        "10.py": evaluate_10,
        "11.py": evaluate_11,
        "12.py": evaluate_12,
        "13.py": evaluate_13,
        "14.py": evaluate_14,
        "15.py": evaluate_15,
        "16.py": evaluate_16,
        "17.py": evaluate_17,
        "18.py": evaluate_18,
        "19 (dir)": evaluate_19,
        "20.py": evaluate_20
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
