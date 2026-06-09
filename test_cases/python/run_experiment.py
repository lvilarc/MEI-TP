#!/usr/bin/env python3
import csv
import importlib.util
import sys
import traceback
import trace
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'results.csv'


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def executable_lines(path):
    lines = path.read_text().splitlines()
    return {
        idx for idx, line in enumerate(lines, 1)
        if line.strip() and not line.lstrip().startswith('#')
    }


def run_suite(problem, model):
    ref_path = BASE / 'reference' / f'{problem}.py'
    test_path = BASE / model / f'{problem}.py'
    if not test_path.exists():
        return [problem, model, 0, 0, 'NA', 'missing_test']

    tests_declared = test_path.read_text().count('assert ')
    try:
        solution = load_module(ref_path, f'reference_{problem}_{model}')
        suite = load_module(test_path, f'{model}_{problem}')
        tracer = trace.Trace(count=True, trace=False)
        tracer.runfunc(suite.run_tests, solution)
        counts = tracer.results().counts
        executed = {line for (file_name, line), count in counts.items() if Path(file_name).resolve() == ref_path.resolve() and count > 0}
        total = executable_lines(ref_path)
        coverage = 'NA' if not total else f'{(len(executed & total) / len(total)) * 100:.2f}'
        return [problem, model, tests_declared, 1, coverage, '']
    except Exception as exc:
        return [problem, model, tests_declared, 0, 'NA', type(exc).__name__]


def main():
    rows = [['problem', 'model', 'tests_declared', 'executed_ok', 'coverage_pct', 'note']]
    for i in range(1, 21):
        problem = f'{i:02d}'
        for model in ('gpt', 'claude'):
            rows.append(run_suite(problem, model))
    with OUT.open('w', newline='') as fh:
        csv.writer(fh).writerows(rows)
    print(f'Done -> {OUT.name}')


if __name__ == '__main__':
    main()
