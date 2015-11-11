"""Given an array of strings containing three types of braces: round (), square [] and curly {}.
write a function that checks whether the braces in each string are correctly matched.
Solution: uses stacks"""


def matches(a):
	stack = []
	for i in a:
		if i in ["(", "[", "{"]:
			stack.append(i)
		else:
			if i == ")":
				left = stack.pop()
				if left != "(":
					return False
			elif i == "]":
				left = stack.pop()
				if left != "[":
					return False
			elif i == "}":
				left = stack.pop()
				if left != "{":
					return False
	return True





l=["(","[","{","}","]",")"]
q=["(", "[", "}", "["]

print matches(l)
print matches(q)


