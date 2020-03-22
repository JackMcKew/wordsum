from wordcount._util.file_locate import locate_files
from wordcount._io.read_files import read_path_list
from wordcount._file_types.markdown import count_words_in_markdown
from wordcount._file_types.jupyter import count_words_in_jupyter

from typing import List

def count_words(path: str,file_types: List[str]) -> int:
    total_word_count: int = 0
    for file_type in file_types:
        if "." not in file_type:
            print(f"File Type: '{file_type}' must be formatted with a period (eg, '.md')")
            continue
        file_list = locate_files(path,file_type)
        file_content = read_path_list(file_list)
        for single_path, content in file_content.items():
            ## TODO Add supported types list
            if file_type == '.md':
                total_word_count += count_words_in_markdown(content)
            elif file_type == '.ipynb':
                total_word_count += count_words_in_jupyter(content)

    return total_word_count



