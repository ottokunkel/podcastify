from transformers import pipeline
from typing import List, Optional

class PDFSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """Initialize the summarizer with specified model."""
        self.summarizer = pipeline("summarization", model=model_name)
    
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        """Generate summary of the input text."""
        summary = self.summarizer(text, 
                                max_length=max_length, 
                                min_length=min_length, 
                                do_sample=False)
        return summary[0]['summary_text']
    
    def summarize_chunks(self, text: str, chunk_size: int = 1024) -> str:
        """Summarize long text by breaking it into chunks."""
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        summaries = []
        
        for chunk in chunks:
            if len(chunk.strip()) > 0:
                summary = self.summarize(chunk)
                summaries.append(summary)
        
        return " ".join(summaries) 