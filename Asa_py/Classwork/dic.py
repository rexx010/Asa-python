def alpha(words):
    output = {}

    for letters in words:
        counter = 0
        for word in words:
            if word == letters:
                counter += 1
                output[word] = counter
    return output

def alpha2(words):
    output = {}
    for letters in words:
         output[letters] = words.count(letters)
    return output

def alpha3(words):
    return {word : words.count(word) for word in words}



words = "google"
print(alpha(words))

words2 = alpha2('apple')
print(words2)

words3 = alpha3('apple')
print(words3)

