#!/usr/bin/python3
def multiple_returns(sentence):
    """
    The function that returns a tuple with the length of a string and its first
    character.

    Args:
        sentence: The string to be evaluated against.
    """
    if not len(sentence):
        sentence_list = list(sentence)
        sentence_list.insert(0, 'None')
        sentence = ''.join(sentence_list)
    return (len(sentence), sentence[0])
