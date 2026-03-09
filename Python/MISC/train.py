#! /user/bin/python3


import sys


text = input("Enter a sentence: ").lower()
words = text.split()
letter_count = {}
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

print ("\nWord frecuency:")
for word, count in word_count.items():
    print (f"{word}: {count}")
    for letter, count in letter_count.items():
        print (f"{letter}: {count}")

test = words[0].split()

print (test)



















