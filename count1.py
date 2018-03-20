import string
def count_letters(word):
    global count
    wordsList = string.split(word)
    count = Counter()
    for words in wordsList:
        for letters in set(words):
            return count[letters]
word = "i likes driving"
print count_letters(word)
