from supabase import create_client, Client
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_ANON_KEY")
)

async def verify_user(email: str, password: str) -> dict:
    """
    Verify a user's credentials against Supabase auth
    
    Args:
        email: User's email address
        password: User's password
    
    Returns:
        dict: User session data if verification successful
        
    Raises:
        HTTPException: If verification fails
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        print(f"Supabase auth response: {response}")
        return response.session
    except Exception as e:
        print(f"Auth error: {str(e)}")
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

async def get_user(access_token: str) -> dict:
    """
    Get user details from an access token
    
    Args:
        access_token: JWT access token
        
    Returns:
        dict: User data if token is valid
        
    Raises:
        HTTPException: If token is invalid
    """
    try:
        user = supabase.auth.get_user(access_token)
        return user.user
    except Exception as e:
        raise HTTPException(
            status_code=401, 
            detail="Invalid or expired token"
        )

async def verify_service_role(service_pass: str) -> bool:
    """
    Verify if the provided service password matches
    
    Args:
        service_pass: Service role password to verify
        
    Returns:
        bool: True if password matches
        
    Raises:
        HTTPException: If password is invalid
    """
    if service_pass != os.getenv("SERVICE_PASS"):
        raise HTTPException(
            status_code=401,
            detail="Invalid service credentials"
        )
    return True
