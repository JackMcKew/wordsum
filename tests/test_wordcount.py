from wordcount import __version__
import pytest
import textwrap
from wordcount._file_types.markdown import count_words_in_markdown
from wordcount._file_types.jupyter import count_words_in_jupyter
from wordcount._util.file_locate import locate_files
from wordcount._io.read_files import read_path_list
import wordcount

def test_version():
    assert __version__ == '0.1.0'

def test_markdown():
    text = textwrap.dedent("""
    test a b    c
    """)
    assert count_words_in_markdown(text) == 4

def test_locate_files():
    file_list = locate_files('./example_files','.md')
    assert len(file_list) == 1

@pytest.mark.parametrize('file_type, expected', [
    ('.md',1),
    ('.ipynb',1),
])
def test_read_files(file_type,expected):
    file_list = locate_files('./example_files','.md')
    file_content = read_path_list(file_list)
    assert len(file_content) == expected

def test_count_markdown():
    assert wordcount.count_words('./example_files',['.md']) == 4

def test_count_jupyter():
    assert wordcount.count_words('./example_files',['.ipynb']) == 4

def test_count_all():
    assert wordcount.count_words('./example_files',wordcount.list_supported_formats()) == 8
