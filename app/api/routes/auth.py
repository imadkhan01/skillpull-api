from fastapi import APIRouter

router = APIRouter()


@router.post("/signup")
def signup():
    # TODO: create user, hash password, return JWT
    return {"todo": True}


@router.post("/login")
def login():
    # TODO: verify password, return JWT
    return {"todo": True}


@router.get("/google")
def google_oauth_start():
    # TODO: redirect to Google OAuth consent screen
    return {"todo": True}


@router.get("/google/callback")
def google_oauth_callback():
    # TODO: exchange code, get user profile, create/link account, return JWT
    return {"todo": True}
