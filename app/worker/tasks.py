from app.worker.celery_app import celery_app


@celery_app.task(name="app.worker.tasks.parse_resume")
def parse_resume_task(resume_file_id: int):
    # TODO: fetch resume file, extract text, extract skills, store resume_parsed_data
    return {"todo": True, "resume_file_id": resume_file_id}


@celery_app.task(name="app.worker.tasks.generate_scores")
def generate_scores_task(candidate_user_id: int):
    # TODO: generate candidate intelligence scores
    return {"todo": True, "candidate_user_id": candidate_user_id}
