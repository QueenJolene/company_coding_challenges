

def is_anagram(word1, word2):
	sorted_word1 = "".join(sorted(list(word1)))
	sorted_word2 = "".join(sorted(list(word2)))
	
	if sorted_word1 == sorted_word2:
		return 1

	else:
		return 0

print is_anagram("hi","ih")
print is_anagram("yo","yolo")