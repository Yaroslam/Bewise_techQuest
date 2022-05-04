from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/questions/")
async def create_question(Question_data: _schemas.Q_questions_num, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.create_question(questions_num=Question_data, db=db)


@app.get("/api/questions/get", response_model=List[_schemas.Question])
async def get_questions(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_questions(db=db)


@app.get("/api/questions/get/{question_id}/", response_model=_schemas.Question)
async def get_question(
        question_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    question = await _services.get_question(db=db, question_id=question_id)
    if question is None:
        raise _fastapi.HTTPException(status_code=404, detail="question does not exist")

    return question


@app.delete("/api/questions/delete/{question_id}/")
async def delete_question(
        question_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    question = await _services.get_question(db=db, question_id=question_id)
    if question is None:
        raise _fastapi.HTTPException(status_code=404, detail="question does not exist")

    await _services.delete_question(question, db=db)

    return "successfully deleted the question"


@app.put("/api/questions/update/{question_id}/", response_model=_schemas.Question)
async def update_contact(question_id: int, question_data: _schemas.CreateQuestion, db: _orm.Session = _fastapi.Depends(_services.get_db),):
    question = await _services.get_question(db=db, question_id=question_id)
    if question is None:
        raise _fastapi.HTTPException(status_code=404, detail="question does not exist")

    return await _services.update_question(
        question_data=question_data, question=question, db=db
    )
