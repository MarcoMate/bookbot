def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_content = f.read()
        words_list = file_content.split()
        print(len(words_list))


main()
