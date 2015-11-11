def check_braces(expressions):
    for s in expressions:
        print evaluate(s)
    return


def evaluate(st):
    stack = []
    for ch in st:
        if ch in ["(", "[", "{"]:
            stack.append(ch)
        else:
            try:
                left = stack.pop()
                if ch == ")":
                    if left != "(":
                        return 0
                if ch == "]":
                    if left != "[":
                        return 0
                if ch == "}":
                    if left != "{":
                        return 0

            except IndexError:
                return 0
    return 1

print check_braces(["([)]", "[]{}()"])