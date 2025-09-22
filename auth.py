from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from config import supabase
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

class SignupData(BaseModel):
    email: EmailStr
    password: str

class SigninData(BaseModel):
    email: EmailStr
    password: str

@router.post("/signup")
def signup(data: SignupData):
    res = supabase.auth.sign_up({"email": data.email, "password": data.password})
    if not res or not getattr(res, "user", None):
        raise HTTPException(status_code=400, detail="Signup failed")
    return {"message": "Signup successful"}

@router.post("/signin")
def signin(data: SigninData):
    res = supabase.auth.sign_in_with_password({"email": data.email, "password": data.password})
    if not res or not getattr(res, "session", None):
        raise HTTPException(status_code=400, detail="Signin failed")
    return {"access_token": res.session.access_token, "refresh_token": res.session.refresh_token}

@router.get("/me")
def get_me(token: str):
    res = supabase.auth.get_user(token)
    user = getattr(res, "user", None) or (res.get("user") if isinstance(res, dict) else None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"id": user.id, "email": user.email}
