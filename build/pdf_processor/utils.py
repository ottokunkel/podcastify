import os
from typing import List

def validate_pdf(file_path: str) -> bool:
    """Validate if the file is a PDF."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return file_path.lower().endswith('.pdf')

def split_into_chunks(text: str, chunk_size: int) -> List[str]:
    """Split text into chunks of specified size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)] 