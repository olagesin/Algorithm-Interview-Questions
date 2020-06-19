"""
Problem definition: Given a sentence, write a method that prints the reversal of the sentence
you get?
"""


def sentence_reversal(sentence):
    sentence = sentence.strip().split()
    new_list = []
    new_word = " "
    for i in reversed(range(len(sentence))):
        new_list.append(sentence[i])
    new_word = new_word.join(new_list)
    return new_word


print(sentence_reversal("Hello world, how are you doing"))
print(sentence_reversal("    Hello, how are you"))
print(sentence_reversal(" in the land of myth     "))
