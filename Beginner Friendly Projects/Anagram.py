from collections import defaultdict


#example:

words = ['eat', 'tea', 'tan', 'nat', 'ant', 'tab', 'bat']


def group_the_anagrams(words):

    dfdic = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word))
        dfdic[sorted_word].append(word)

    return list(dfdic.values())


print (group_the_anagrams(words))


