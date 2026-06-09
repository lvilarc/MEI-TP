#!/usr/bin/env bash
# Test Case Generation experiment harness.
# For each problem NN and each model (gpt, claude):
#   - compile reference/NN.c + MODEL/NN.c with coverage instrumentation
#   - run the resulting binary (assert-based test suite)
#   - measure line coverage of the reference via gcov
# Outputs results.csv at suite-level granularity.
#
# Columns:
#   problem,model,tests_declared,compiled,executed_ok,coverage_pct,note
#     compiled    = 1 if reference+test compiled and linked
#     executed_ok = 1 if the suite ran to completion with exit 0 (all asserts passed)
#     coverage_pct= line coverage of reference/NN.c achieved by the run (NA if not compiled)

set -u
cd "$(dirname "$0")"

OUT=results.csv
echo "problem,model,tests_declared,compiled,executed_ok,coverage_pct,note" > "$OUT"

for i in $(seq -w 1 20); do
  for model in gpt claude; do
    ref="reference/$i.c"
    test="$model/$i.c"
    note=""

    tests=$(grep -c -E '\bassert[[:space:]]*\(' "$test" 2>/dev/null)
    [ -z "$tests" ] && tests=0

    if [ ! -s "$test" ]; then
      echo "$i,$model,0,0,0,NA,missing_test" >> "$OUT"; continue
    fi

    W=$(mktemp -d)
    clog="$W/compile.log"

    gcc -std=c11 -O0 --coverage -c "$ref"  -o "$W/ref.o"  > "$clog" 2>&1 && \
    gcc -std=c11 -O0 --coverage -c "$test" -o "$W/test.o" >> "$clog" 2>&1 && \
    gcc --coverage "$W/ref.o" "$W/test.o" -o "$W/bin" -lm >> "$clog" 2>&1
    if [ $? -ne 0 ]; then
      echo "$i,$model,$tests,0,0,NA,compile_error" >> "$OUT"
      rm -rf "$W"; continue
    fi

    timeout 10 "$W/bin" > "$W/run.log" 2>&1
    rc=$?
    if [ $rc -eq 0 ]; then exec_ok=1; else exec_ok=0; fi
    [ $rc -eq 124 ] && note="timeout"
    [ $rc -eq 134 ] && note="assert_failed"
    [ $rc -ne 0 ] && [ $rc -ne 134 ] && [ $rc -ne 124 ] && note="runtime_rc$rc"

    # coverage is only meaningful when the suite ran to completion; on a crash
    # or assert-abort the .gcda data is not flushed, so report NA.
    if [ $exec_ok -eq 1 ]; then
      cov=$(gcov -n -o "$W" "$W/ref.o" 2>/dev/null \
            | grep "Lines executed" | head -1 \
            | sed -E 's/.*executed:([0-9.]+)%.*/\1/')
      [ -z "$cov" ] && cov="NA"
    else
      cov="NA"
    fi

    echo "$i,$model,$tests,1,$exec_ok,$cov,$note" >> "$OUT"
    rm -rf "$W" *.gcov 2>/dev/null
  done
done

echo "Done -> $OUT"
