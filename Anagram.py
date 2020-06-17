#Problem Definition: Check is two strings are anagrams


def Anagram(string1, string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    if len(string1) == len(string2):
        for i in range(len(string1)):
            if string1[i] in string2 and string2[i] in string1:
                continue
            return False
        return True
    else:
        return False


print(Anagram("clint eastwood", "old west action"))
print(Anagram("go go go", "gggooo"))
print(Anagram("hi man", "hi    man"))
print(Anagram("aabbcc", "aabbc"))
