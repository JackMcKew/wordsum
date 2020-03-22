import io
import pathlib
from typing import Optional, List, Dict

def read_file(path: pathlib.Path) -> str:
    with open(path,'r',encoding='utf-8') as f:
        text_content = f.read()

    return text_content

def read_path_list(path_list: List[pathlib.Path]) -> Dict[pathlib.Path,str]:

    content_dict: Dict[pathlib.Path, str] = {}

    for path in path_list:
        content_dict[path] = read_file(path)

    return content_dict
