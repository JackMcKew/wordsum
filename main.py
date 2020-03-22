# from wordcount.util.file_locate import locate_files
# from wordcount.io.read_files import read_path_list

# if __name__ == "__main__":
#     file_list = locate_files('./tests','.md')
#     file_content = read_path_list(file_list)
#     print(file_content)

import wordcount

if __name__ == "__main__":
    print(wordcount.count_words('./tests',['.md']))