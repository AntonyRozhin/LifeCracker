from fastapi import APIRouter, Depends
from .. import schemas, models
from ..dependencies import get_current_active_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user


