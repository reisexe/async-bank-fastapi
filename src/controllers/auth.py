from fastapi import APIRouter, HTTPException, status

from src.schemas.auth import LoginIn
from src.security import sign_jwt
from src.services.user import UserService
from src.views.auth import LoginOut

router = APIRouter(prefix="/auth")
service = UserService()


@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    user = await service.get_by_username(data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
    
    if not service.verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Senha incorreta")
    
    return sign_jwt(user_id=user.id)


@router.post("/register", response_model=LoginOut)
async def register(data: LoginIn):
    existing = await service.get_by_username(data.username)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário já existe")
    
    user_id = await service.create(data.username, data.password)
    return sign_jwt(user_id=user_id)