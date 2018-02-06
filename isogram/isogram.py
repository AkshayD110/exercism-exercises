def is_isogram(string):
    word = string.lower()

    lenght_of_word = len(word)
    sublenght = 1

    for i in range (0, lenght_of_word):
        for j in range (sublenght, lenght_of_word):
            if (word[i] ==  word[j] and not word[i] == word[j] =="-" and not word[i] == word[j] == " "):
                return False
        sublenght += 1

    return True

