import nbformat

def count_words_in_jupyter(jupyter_json_content: nbformat.NotebookNode, return_type:str = 'markdown') -> int:
    word_count: int = 0
    for cell in jupyter_json_content.cells:
        if cell.cell_type != return_type:
            continue
        word_count += len(cell['source'].replace('#','').lstrip().split(' '))

    return word_count