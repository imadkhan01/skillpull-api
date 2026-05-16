from celery import Celery

from app.settings import settings

celery_app = Celery(
    "skillpull",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.task_routes = {
    "app.worker.tasks.*": {"queue": "default"},
}
