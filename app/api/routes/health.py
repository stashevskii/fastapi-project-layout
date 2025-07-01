from fastapi import APIRouter

router = APIRouter(tags=["Health"], prefix="/health")


@router.get("/ping", summary="Check API works")
def ping():
    return {"message": "pong"}
