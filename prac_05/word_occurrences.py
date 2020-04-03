TEXT_STRING = "this is a collection of words of nice words this is a fun thing it is"


def main ():
    words = TEXT_STRING.split(" ")
    words.sort()
    word_count_dict = {"Text": TEXT_STRING}

    for word in words:
        word_count_dict[word] = word_count_dict.get(word, 1) + 1

    longest_word_length = max(len(key) for key in word_count_dict.keys())

    for word in word_count_dict:
        print("{:{}} : {}".format(word, longest_word_length, word_count_dict[word]))


main()
