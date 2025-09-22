from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from config import supabase

router = APIRouter(prefix="/tasks", tags=["Tasks"])
security = HTTPBearer()

class TaskCreate(BaseModel):
    title: str
    category: Optional[str] = None
    deadline: Optional[datetime] = None
    is_complete: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    deadline: Optional[datetime] = None
    is_complete: Optional[bool] = None

class TaskOut(BaseModel):
    id: str
    user_id: str
    title: str
    category: Optional[str] = None
    is_complete: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deadline: Optional[datetime] = None

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials
    res = supabase.auth.get_user(token)
    user = getattr(res, "user", None) or (res.get("user") if isinstance(res, dict) else None)
    if not user:
        raise HTTPException(status_code=401, detail="invalid_or_expired_token")
    uid = getattr(user, "id", None) or (user.get("id") if isinstance(user, dict) else None)
    if not uid:
        raise HTTPException(status_code=401, detail="invalid_or_expired_token")
    return str(uid)

@router.post("", response_model=TaskOut)
def create_task(payload: TaskCreate, uid: str = Depends(get_current_user)):
    data = {
        "user_id": uid,
        "title": payload.title,
        "category": payload.category,
        "deadline": payload.deadline.isoformat() if payload.deadline else None,
        "is_complete": bool(payload.is_complete),
    }
    res = supabase.table("tasks").insert(data).select("*").single().execute()
    row = (res.data or {}) if hasattr(res, "data") else res
    if not row:
        raise HTTPException(status_code=400, detail="create_failed")
    return row

@router.get("", response_model=List[TaskOut])
def list_tasks(
    uid: str = Depends(get_current_user),
    is_complete: Optional[bool] = None,
    category: Optional[str] = None,
    before: Optional[datetime] = None,
    after: Optional[datetime] = None,
    limit: int = 50,
    offset: int = 0,
):
    q = supabase.table("tasks").select("*").eq("user_id", uid)
    if is_complete is not None:
        q = q.eq("is_complete", is_complete)
    if category:
        q = q.eq("category", category)
    if before:
        q = q.lte("deadline", before.isoformat())
    if after:
        q = q.gte("deadline", after.isoformat())
    q = q.order("deadline", desc=False, nullsfirst=True).order("created_at", desc=True)
    if offset:
        q = q.range(offset, offset + limit - 1)
    else:
        q = q.limit(limit)
    res = q.execute()
    data = (res.data or []) if hasattr(res, "data") else res
    return data

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: str, payload: TaskUpdate, uid: str = Depends(get_current_user)):
    updates = {}
    if payload.title is not None:
        updates["title"] = payload.title
    if payload.category is not None:
        updates["category"] = payload.category
    if payload.deadline is not None:
        updates["deadline"] = payload.deadline.isoformat()
    if payload.is_complete is not None:
        updates["is_complete"] = bool(payload.is_complete)
    if not updates:
        raise HTTPException(status_code=400, detail="nothing_to_update")
    res = (
        supabase.table("tasks")
        .update(updates)
        .eq("id", task_id)
        .eq("user_id", uid)
        .select("*")
        .single()
        .execute()
    )
    row = (res.data or {}) if hasattr(res, "data") else res
    if not row:
        raise HTTPException(status_code=404, detail="not_found")
    return row

@router.delete("/{task_id}")
def delete_task(task_id: str, uid: str = Depends(get_current_user)):
    supabase.table("tasks").delete().eq("id", task_id).eq("user_id", uid).execute()
    return {"status": "deleted"}
