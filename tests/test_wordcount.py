from wordcount import __version__
import pytest
import textwrap
from wordcount.file_types.markdown import count_words_in_markdown
from wordcount.file_types.jupyter import count_words_in_jupyter

from wordcount.util.file_locate import locate_files
from wordcount.io.read_files import read_path_list

def test_version():
    assert __version__ == '0.1.0'

def test_markdown():
    text = textwrap.dedent("""
    test a b    c
    """)
    assert count_words_in_markdown(text) == 4

def test_locate_files():
    file_list = locate_files('./tests','.md')
    assert len(file_list) == 1

def test_read_files():
    file_list = locate_files('./tests','.md')
    file_content = read_path_list(file_list)
    assert len(file_content) == 1