# Word Sum

Wordsum is a package for counting words within a folder of files recursively.

## Usage
``` python
import wordsum

if __name__ == "__main__":
    print(wordsum.count_words('./example_files',['.md','.ipynb']))
    wordsum.list_supported_formats()
```

## Supported Formats
Currently wordsum only supports markdown `.md` and jupyter notebooks `.ipynb`.

## Contribute

PRs are welcome for anything!