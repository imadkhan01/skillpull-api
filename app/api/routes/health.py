from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.health import ping_db

router = APIRouter()


@router.get("/db")
def db_health(db: Session = Depends(get_db)):
    return {"db": ping_db(db)}
