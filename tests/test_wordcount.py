from wordcount import __version__
import pytest
import textwrap
from wordcount.markdown import count_words_in_markdown

def test_version():
    assert __version__ == '0.1.0'

def test_markdown():
    text = textwrap.dedent("""
    test a b    c
    """)
    assert count_words_in_markdown(text) == 4