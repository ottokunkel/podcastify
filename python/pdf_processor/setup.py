from setuptools import setup, find_packages

setup(
    name="pdf_processor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2>=3.0.0",
        "nltk>=3.7",
        "transformers>=4.0.0",
        "torch>=1.9.0",
        "spacy>=3.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for preprocessing and summarizing PDFs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pdf_processor",
) 