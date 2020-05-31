"""Wikipedia Practical"""
import wikipedia


def main():
    print("Wikipedia Search\n")

    search_phrase = input("Enter search phrase: ")

    while search_phrase != "":
        try:
            display_page_details(search_phrase)
        except wikipedia.exceptions.DisambiguationError as search_phrase:
            print(search_phrase.options)
        except wikipedia.exceptions.PageError:
            print("Page not found")
        search_phrase = input("Enter search phrase: ")


def display_page_details(search_phrase):
    page = wikipedia.page(search_phrase)
    print("Title: {}".format(page.title))
    print("Summary: {}".format(page.summary))
    print("Url: {}".format(page.url))


main()
