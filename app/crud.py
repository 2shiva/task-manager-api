from sqlalchemy.orm import Session
from app import models, schemas


def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(db: Session, user_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.user_id == user_id)
        .all()
    )


def get_task(db: Session, task_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.id == task_id)
        .first()
    )


def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = get_task(db, task_id)

    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed

        db.commit()
        db.refresh(db_task)

    return db_task


def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)

    if db_task:
        db.delete(db_task)
        db.commit()

    return db_task