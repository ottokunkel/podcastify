import os
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from rich.console import Console
from rich.progress import Progress
from pdf_processor.preprocessor import PDFPreprocessor
from pdf_processor.summarizer import PDFSummarizer
from pdf_processor.utils import validate_pdf, split_into_chunks
from dotenv import load_dotenv
from pdf_processor.podcast_generator import PodcastGenerator

load_dotenv()

def main():
    """
    Main function to handle LangChain operations.
    Initializes LLM, creates chains, and manages prompt templates.
    """
    # Initialize console for rich output
    console = Console()
    
    pdf_path = os.path.join("pdfs", "./book1.pdf")
    
    try:
        # Validate PDF file
        if validate_pdf(pdf_path):
            preprocessor = PDFPreprocessor()
            podcast_generator = PodcastGenerator()
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
                task = progress.add_task("[yellow]Processing text...", total=1)
                sentences = preprocessor.process_text(cleaned_text)
                progress.update(task, advance=1)

                # Generate podcast script
                task = progress.add_task("[magenta]Generating podcast script...", total=1)
                podcast_script = podcast_generator.generate(sentences)
                progress.update(task, advance=1)
            
            # Print results
            console.print("\n[bold green]Processing complete![/]")
            console.print(f"Found [cyan]{len(sentences)}[/] sentences")
            
            # Save processed text to file
            # Create output directory
            os.makedirs("output", exist_ok=True)
            
            # Save processed text
            text_output_path = os.path.join("output", "processed_text.txt")
            podcast_output_path = os.path.join("output", "podcast_script.txt")
            
            with Progress() as progress:
                # Save processed text
                task = progress.add_task("[magenta]Saving processed text...", total=1)
                with open(text_output_path, "w", encoding="utf-8") as f:
                    f.write(sentences)
                progress.update(task, advance=1)
                
                # Save podcast script
                task = progress.add_task("[magenta]Saving podcast script...", total=1) 
                with open(podcast_output_path, "w", encoding="utf-8") as f:
                    f.write(podcast_script)
                progress.update(task, advance=1)
            
            console.print(f"\nProcessed text saved to: [cyan]{text_output_path}[/]")
            console.print(f"Podcast script saved to: [cyan]{podcast_output_path}[/]")
                
    except FileNotFoundError as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/] {str(e)}")

if __name__ == "__main__":
    main()
