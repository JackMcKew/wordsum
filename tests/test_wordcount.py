from wordcount import __version__
import pytest
import textwrap
from wordcount.file_types.markdown import count_words_in_markdown
from wordcount.file_types.jupyter import count_words_in_jupyter

def test_version():
    assert __version__ == '0.1.0'

def test_markdown():
    text = textwrap.dedent("""
    test a b    c
    """)
    assert count_words_in_markdown(text) == 4