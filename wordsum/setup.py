import setuptools
import wordsum
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordsum-JackMcKew", # Replace with your own username
    version=wordsum.__version__,
    author="JackMcKew",
    author_email="jackmckew2@gmail.com",
    description="Wordsum is a package for counting words within a folder of files recursively.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JackMcKew/wordsum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)