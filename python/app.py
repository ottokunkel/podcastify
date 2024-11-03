from fastapi import FastAPI, HTTPException, UploadFile, File, Header, Body
from fastapi.responses import FileResponse, StreamingResponse
from pdf_processor.preprocessor import PDFPreprocessor
from pdf_processor.summarizer import PDFSummarizer
from pdf_processor.utils import validate_pdf
from pdf_processor.podcast_generator import PodcastGenerator
from dotenv import load_dotenv
from io import BytesIO
from auth.supabase import get_user, verify_user
import uvicorn

load_dotenv()

app = FastAPI(
    title="PDF Processing API",
    description="API for processing and summarizing PDF documents",
    version="1.0.0"
)

@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...), authorization: str = Header(None)):
    """
    Process a PDF file and return the cleaned text. Requires authentication.
    """
    # Verify user is authenticated
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        # Verify the access token and get user
        user = await get_user(authorization.split(" ")[1])
    except:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    podcast_generator = PodcastGenerator()
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    try:
        contents = await file.read()
        pdf_file = BytesIO(contents)
        
        # Process PDF directly from bytes
        preprocessor = PDFPreprocessor()
        text = preprocessor.extract_text(pdf_file)
        cleaned_text = preprocessor.clean_text(text)
        processed_text = preprocessor.process_text(cleaned_text)
        # Generate the podcast script
        script = podcast_generator.generate_podcast_script(processed_text)
        
        # Generate audio from the script
        audio_output = podcast_generator.generate_audio(script)
        
        # Get the audio data as bytes
        audio_bytes = audio_output.read()
        
        # Create a BytesIO object to stream the audio
        audio_stream = BytesIO(audio_bytes)
        
        # Return the audio file as a streaming response
        return StreamingResponse(
            audio_stream,
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": f"attachment; filename=podcast.mp3"
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/login")
async def login(credentials: dict = Body(...)):
    """
    Login endpoint to authenticate users and return access token
    
    Args:
        credentials: Dict containing email and password
        
    Returns:
        dict: Session data including access token
        
    Raises:
        HTTPException: If credentials are invalid
    """
    try:
        email = credentials.get("email")
        password = credentials.get("password")
        
        if not email or not password:
            raise HTTPException(
                status_code=400,
                detail="Email and password required"
            )
            
        session = await verify_user(email, password)
        return session
        
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/")
async def root():
    """
    Root endpoint serving frontend/index.html
    """
    return FileResponse("frontend/index.html")

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000)