import re

def count_words_in_markdown(markdown_text_content: str) -> int:

    # Comments
    markdown_text_content = re.sub(r'<!--(.*?)-->', '', markdown_text_content, flags=re.MULTILINE)
    # Tabs to spaces
    markdown_text_content = markdown_text_content.replace('\t', '    ')
    # More than 1 space to 4 spaces
    markdown_text_content = re.sub(r'[ ]{2,}', '    ', markdown_text_content)
    # Footnotes
    markdown_text_content = re.sub(r'^\[[^]]*\][^(].*', '', markdown_text_content, flags=re.MULTILINE)
    # Indented blocks of code
    markdown_text_content = re.sub(r'^( {4,}[^-*]).*', '', markdown_text_content, flags=re.MULTILINE)
    # Custom header IDs
    markdown_text_content = re.sub(r'{#.*}', '', markdown_text_content)
    # Replace newlines with spaces for uniform handling
    markdown_text_content = markdown_text_content.replace('\n', ' ')
    # Remove images
    markdown_text_content = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', markdown_text_content)
    # Remove HTML tags
    markdown_text_content = re.sub(r'</?[^>]*>', '', markdown_text_content)
    # Remove special characters
    markdown_text_content = re.sub(r'[#*`~\-–^=<>+|/:]', '', markdown_text_content)
    # Remove footnote references
    markdown_text_content = re.sub(r'\[[0-9]*\]', '', markdown_text_content)
    # Remove enumerations
    markdown_text_content = re.sub(r'[0-9#]*\.', '', markdown_text_content)

    return len(markdown_text_content.split())
