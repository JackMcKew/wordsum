# from wordcount.util.file_locate import locate_files
# from wordcount.io.read_files import read_path_list

# if __name__ == "__main__":
#     file_list = locate_files('./tests','.md')
#     file_content = read_path_list(file_list)
#     print(file_content)

from wordcount.word_count import count_words

if __name__ == "__main__":
    print(count_words('./tests',['.md']))