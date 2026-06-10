word =input("Enter a word:")

word_lower =word.lower()

reversed_word =word_lower[::-1]

if word_lower == reversed_word:
    print(f"'{word}' is a palindrom ")
else:
    print(F"'{word}' is not a palindrom ")