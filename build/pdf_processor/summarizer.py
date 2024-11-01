from langchain_openai.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from typing import List, Optional

class PDFSummarizer:
    def __init__(self, model_name: str = "gpt-4o"):
        """Initialize the summarizer with specified model."""
        self.llm = OpenAI(model_name=model_name)
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="Please summarize the following text:\n\n{text}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        """Generate summary of the input text."""
        summary = self.chain.run(text=text)
        return summary.strip()
    
    def summarize_chunks(self, text: str, chunk_size: int = 1024) -> str:
        """Summarize long text by breaking it into chunks."""
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        summaries = []
        
        for chunk in chunks:
            if len(chunk.strip()) > 0:
                summary = self.summarize(chunk)
                summaries.append(summary)
        
        return " ".join(summaries)