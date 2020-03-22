import wordsum

if __name__ == "__main__":
    print(wordsum.count_words('./example_files',['.md','.ipynb']))
    wordsum.list_supported_formats()
    print(wordsum.count_files('./example_files',['.md','.ipynb']))