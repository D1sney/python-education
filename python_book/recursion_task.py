def palindrome(word):
    if len(word) <= 2:
        return word
    else:
        l = word[0]
        r = word[-1]
        new_word = palindrome(word[1:-1])
        new_word = r+'('+new_word+')'+l
        return new_word

print(palindrome('шалашhfehferihgehglgdsfsnvfdff'))