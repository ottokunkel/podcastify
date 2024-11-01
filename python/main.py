import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from rich.console import Console
from rich.progress import Progress
from pdf_processor.preprocessor import PDFPreprocessor
from pdf_processor.utils import validate_pdf

def main():
    """
    Main function to handle LangChain operations.
    Initializes LLM, creates chains, and manages prompt templates.
    """
    # Initialize console for rich output
    console = Console()
    
    pdf_path = os.path.join("pdfs", "sample.pdf")
    
    try:
        # Validate PDF file
        if validate_pdf(pdf_path):
            preprocessor = PDFPreprocessor()
            
            with Progress() as progress:
                # Extract text
                task = progress.add_task("[cyan]Extracting text...", total=1)
                text = preprocessor.extract_text(pdf_path)
                progress.update(task, advance=1)
                
                # Clean text
                task = progress.add_task("[green]Cleaning text...", total=1)
                cleaned_text = preprocessor.clean_text(text)
                progress.update(task, advance=1)
                
                # Segment text
                task = progress.add_task("[yellow]Segmenting text...", total=1)
                sentences = preprocessor.segment_text(cleaned_text)
                progress.update(task, advance=1)
            
            # Print results
            console.print("\n[bold green]Processing complete![/]")
            console.print(f"Found [cyan]{len(sentences)}[/] sentences")
            
            # Preview first few sentences
            console.print("\n[bold]First few sentences:[/]")
            for i, sent in enumerate(sentences[:3]):
                console.print(f"{i+1}. {sent}")
                
    except FileNotFoundError as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/] {str(e)}")

if __name__ == "__main__":
    main()
