def main():
    text_string = input("Enter words here: ")
    words = text_string.split(" ")
    words.sort()
    print("words")
    word_count_dict = {"Text": text_string}

    for word in words:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    longest_word_length = max(len(key) for key in word_count_dict.keys())

    for word in word_count_dict:
        print("{:{}} : {}".format(word, longest_word_length, word_count_dict[word]))


main()
