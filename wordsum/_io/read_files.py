import io
import pathlib
from typing import List, Dict
import nbformat

def read_markdown(path: pathlib.Path) -> str:
    with open(path, 'r', encoding='utf8') as f:
        text = f.read()
    return text

def read_jupyter(path: pathlib.Path):
    with io.open(path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f,nbformat.NO_CONVERT)
        # nb = current.read(f, 'json')
    return nb

supported_formats = {
    '.md': read_markdown,
    '.ipynb': read_jupyter
}

def read_file(path: pathlib.Path) -> str:

    if path.suffix not in supported_formats.keys():
        print(f"{path.suffix} is not supported yet.")
        return Exception

    return supported_formats[path.suffix](path)

def read_path_list(path_list: List[pathlib.Path]) -> Dict[pathlib.Path,str]:

    content_dict: Dict[pathlib.Path, str] = {}

    for path in path_list:
        content_dict[path] = read_file(path)

    return content_dict
