from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_profile():
    # TODO: auth required
    return {"todo": True}


@router.patch("")
def update_profile():
    # TODO: auth required
    return {"todo": True}
