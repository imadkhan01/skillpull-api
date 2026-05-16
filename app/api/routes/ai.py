from fastapi import APIRouter

router = APIRouter()


@router.post("/parse-resume")
def parse_resume():
    return {"todo": True}


@router.post("/generate-score")
def generate_score():
    return {"todo": True}


@router.post("/job-match")
def job_match():
    return {"todo": True}
