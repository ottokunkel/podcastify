import PyPDF2
import re
from typing import List, Optional
import spacy

class PDFPreprocessor:
    def __init__(self, language: str = "en"):
        """Initialize the preprocessor with specified language."""
        self.nlp = spacy.load(f"{language}_core_web_sm")
    
    def extract_text(self, pdf_path: str) -> str:
        """Extract text from PDF file."""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    
    def clean_text(self, text: str) -> str:
        """Clean extracted text by removing special characters and extra whitespace."""
        # Remove special characters
        text = re.sub(r'[^\w\s.]', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def segment_text(self, text: str) -> List[str]:
        """Segment text into sentences."""
        doc = self.nlp(text)
        return [sent.text.strip() for sent in doc.sents] 