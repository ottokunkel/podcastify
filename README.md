# Podcastify

Podcastify is a fullstack web app that provides a frontend to convert PDF documents into audio podcasts using an LLM pipeline and TTS Model. 

## Features

- PDF to audio conversion
- User authentication
- Secure file handling
- Browser-based audio playback
- Responsive web interface

## Tech Stack

### Frontend
- Next.js
- TypeScript
- Tailwind CSS
- Supabase Auth
- shadcn/ui components

### Backend
- FastAPI
- Python
- PDF processing libraries
- Text-to-Speech AI

### Demo
[![Demo](https://github.com/user-attachments/assets/25dd0ff1-2e08-46f2-9816-39bb9de48872)](https://github.com/user-attachments/assets/3d947133-a4a1-40af-a4de-b1ce606ffb8f)

## Getting Started

1. Clone the repository
2. Set up environment variables in frontend/.env and python/.env:
   ```
   NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_key
   NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
   ```
   ```
   OPENAI_API_KEY=
   SUPABASE_URL=
   SUPABASE_ANON_KEY=
   SUPABASE_SERVICE_ROLE_KEY=
   SERVICE_PASS=
   ``` 
3. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd python
   pip install -r requirements.txt
   ```
4. Run the development servers:
   ```bash
   # Frontend
   npm run dev

   # Backend
   python app.py
   ```

## Usage

1. Register or log in to your account
2. Upload a PDF file (max 10MB)
3. Wait for the processing to complete
4. Download or stream the generated audio file

## TODO
- [ ] Implement Register API call in frontend 
