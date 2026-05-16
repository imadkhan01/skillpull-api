from fastapi import APIRouter

router = APIRouter()


@router.post("")
def create_company():
    return {"todo": True}


@router.get("")
def get_company():
    return {"todo": True}
