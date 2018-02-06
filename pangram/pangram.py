def is_pangram(sentence):
    import collections
    list_of_alph = collections.deque()
    for i in range(ord('a'), ord('z')+1):
        list_of_alph.append(chr(i))

    checkString = sentence
    checkString = checkString.lower()

    charsOfString = list(checkString)
    for i in range(len(charsOfString)):
        if list_of_alph.__contains__(charsOfString[i]):
            list_of_alph.remove(charsOfString[i])

    if (len(list_of_alph)==0):
        return True
    else:
        return False