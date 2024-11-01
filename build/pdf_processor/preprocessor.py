import PyPDF2
import re
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

class PDFPreprocessor:
    def __init__(self, language: str = "en"):
        """Initialize the preprocessor with specified language."""
        pass
    
    def extract_text(self, pdf_path: str) -> str:
        """Extract text from PDF file."""
        reader = PyPDF2.PdfReader(pdf_path)
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
        # Simple sentence segmentation using periods
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [sent.strip() for sent in sentences if sent.strip()]
    
    def process_text(self, text: str) -> str:
        # Initialize LLM and chain
        model = ChatOpenAI(model="gpt-4o", temperature=0)
        # Create runnable chain
        prompt = ChatPromptTemplate.from_template(
            """
                You are a world class text pre-processor, here is the raw data from a PDF, please parse and return it in a way that is crispy and usable to send to a podcast writer.

                The raw data is messed up with new lines, Latex math and you will see fluff that we can remove completely. Basically take away any details that you think might be useless in a podcast author's transcript.

                Remember, the podcast could be on any topic whatsoever so the issues listed above are not exhaustive

                Please be smart with what you remove and be creative ok?

                Remember DO NOT START SUMMARIZING THIS, YOU ARE ONLY CLEANING UP THE TEXT AND RE-WRITING WHEN NEEDED

                Be very smart and aggressive with removing details, you will get a running portion of the text and keep returning the processed text.

                PLEASE DO NOT ADD MARKDOWN FORMATTING, STOP ADDING SPECIAL CHARACTERS THAT MARKDOWN CAPATILISATION ETC LIKES

                ALWAYS start your response directly with processed text and NO ACKNOWLEDGEMENTS about my questions ok?

                Here is the text:
                {text}
            """)
        chain = prompt | model 
        # Process the text using the runnable chain
        processed_text = chain.invoke(text)
        return processed_text.content