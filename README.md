# SkillPull API

Backend for SkillPull (Phase 1 MVP).

## Tech
- FastAPI
- PostgreSQL
- Redis
- Celery
- Alembic

## Local dev (Docker-first)
```bash
docker compose up --build
```

## Local dev (without Docker)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
