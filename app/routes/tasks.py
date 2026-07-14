from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas
from app.models import User
from app.security import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "/",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_task(db, task, current_user.id)


@router.get("/", response_model=list[schemas.Task])
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_tasks(db, current_user.id)


@router.put(
    "/{task_id}",
    response_model=schemas.Task
)
def update_task(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    updated_task = crud.update_task(db, task_id, task)

    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_200_OK
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted_task = crud.delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}