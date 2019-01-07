import sys

def make1shorter(word1, word2):
    if len(word1) > len(word2):
        # Make sure word1 is shorter
        temp = word1
        word1 = word2
        word2 = temp

    return word1, word2

def dj(word1, word2):
    if len(word1) == 0 or len(word2) == 0:
        raise Exception("Not words, mate")

    word1, word2 = make1shorter(word1, word2)

    word2chars = list(word2)
    m = 0
    for char in word1:
        if char in word2chars:
            m += 1
            word2chars.pop(word2chars.index(char))

    t = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            t += 1

    return 1/3*(m/len(word1) + m/len(word2) + (m - t / 2)/m)

def dw(word1, word2, p=0.1, lmax=4):
    word1, word2 = make1shorter(word1, word2)

    dj_ = dj(word1, word2)

    l = 0
    for i in range(min(len(word1), lmax)):
        if word1[i] == word2[i]:
            l += 1
        else:
            break

    return dj_ + l * p * (1 - dj_)

if len(sys.argv) < 3:
    raise Exception("I need two wodrs, mate")

word1 = sys.argv[1]
word2 = sys.argv[2]

print(f'word1: {word1}\nword2: {word2}\nJaro distance: {dj(word1, word2)}\nJaro-Winkler distance: {dw(word1, word2)}')