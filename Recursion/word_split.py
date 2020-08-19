def word_split(phrase, list_of_words, output=None):

    if output == None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):
            output.append(word)
            list_of_words.remove(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output


print(word_split('themanran', ['the', 'man', 'ran']))
