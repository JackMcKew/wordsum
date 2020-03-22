import pathlib
from typing import List
def locate_files(path: str,file_type:str) -> List[pathlib.Path]:
    topPath: pathlib.Path = pathlib.Path(path)

    if "." not in file_type:
        print("File types must include a period eg, '.md'")

    for singleFile in topPath.glob(f'**/*{file_type}'):
        if singleFile.suffix == '.md':        
            allMarkdown.append(singleFile)
        if singleFile.suffix == '.ipynb' and 'checkpoint' not in singleFile.name:
            allJupyter.append(singleFile)
