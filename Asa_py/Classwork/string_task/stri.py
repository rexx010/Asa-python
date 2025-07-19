def divide_word(word1):
    if len(word1) % 2 == 0:
        new_word = len(word1) // 2
        return word1[:new_word] + "ce" + word1[new_word:]
    else:
        return word1 + "ce"






