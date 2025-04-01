from fastapi import APIRouter, Depends

from app.repositories.user import UserRepository

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{user_id}")
async def get_user(
    user_id: int,
    user_repository: UserRepository = Depends(UserRepository),
):
    return await user_repository.get_user_by_id(user_id)
