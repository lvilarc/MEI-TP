def longestValidParentheses(s):
    stack = [-1]
    best = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                best = max(best, i - stack[-1])
            else:
                stack.append(i)
    return best
