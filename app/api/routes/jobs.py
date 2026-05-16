from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_jobs():
    return {"todo": True}


@router.post("")
def create_job():
    return {"todo": True}
