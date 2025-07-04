from loguru import logger
from fastapi import Response,APIRouter,HTTPException
from sqlalchemy.exc import IntegrityError
from schemas.example_user_schemas import UserCreate, UserResponse
from services.example_service import insert_user

router=APIRouter()

@router.post("/example",response_model=UserResponse)
async def post_example(user:UserCreate)->Response:
    try:
        newuser=insert_user(user)  # Replace with your actual insert method
        logger.debug(newuser)
        return newuser

    except IntegrityError as e:
        if "Duplicate entry" in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already exists.")
        raise HTTPException(status_code=500, detail="Database error occurred.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/example")
async def get_example()->Response:
    return Response(content="All seems to be ok!",status_code=200) 
