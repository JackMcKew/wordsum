import wordcount

if __name__ == "__main__":
    print(wordcount.count_words('./example_files',['.md','.ipynb']))
    wordcount.list_supported_formats()