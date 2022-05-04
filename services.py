from typing import TYPE_CHECKING

import database as _db
import models as _models
import schemas as _schemas
import side_api as _side
from sqlalchemy.orm import Session


def _add_tables():
    return _db.base.metadata.create_all(bind=_db.engine)


def get_db():
    db = _db.session_local()
    try:
        yield db
    finally:
        db.close()


# быстро, но работает не корректно при questions_num.questions_num = 1.
# def create_question(questions_num: _schemas.Q_questions_num, db: "Session"):
#     questions = _side.make_request(question_num={"count": questions_num.questions_num})
#     cur_id = 0
#     for q in questions:
#         if db.query(_models.Question).filter(_models.Question.question_text == q["question"]).first() is None:
#             question = {"question_text": q["question"], "answer_text": q['answer']}
#             question = _models.Question(question_text=question["question_text"], answer_text=question["answer_text"])
#             db.add(question)
#             db.commit()
#             db.refresh(question)
#             cur_id = question.id
#         else:
#             continue
#     return get_question(cur_id - 1, db)


# медленно, но работает корректно при questions_num.questions_num = 1.
def create_question(questions_num: _schemas.Q_questions_num, db: "Session"):
    i = 0
    cur_id = 0
    while i != questions_num.questions_num:
        questions = _side.make_request(question_num={"count": 1})
        for q in questions:
            if db.query(_models.Question).filter(_models.Question.question_text == q["question"]).first() is None:
                question = {"question_text": q["question"], "answer_text": q['answer']}
                question = _models.Question(question_text=question["question_text"],
                                            answer_text=question["answer_text"])
                db.add(question)
                db.commit()
                db.refresh(question)
                cur_id = question.id
                i += 1
            else:
                continue
    return get_question(cur_id - 1, db)


async def get_all_questions(db: "Session"):
    questions = db.query(_models.Question).all()
    return list(map(_schemas.Question.from_orm, questions))


async def get_question(question_id: int, db: "Session"):
    question = db.query(_models.Question).filter(_models.Question.id == question_id).first()
    return question


async def delete_question(question: _models.Question, db: "Session"):
    db.delete(question)
    db.commit()


def delete_all_q(db: "Session"):
    _models.Question.query.delete()
    db.commit()
    return "all deleted"


async def update_question(question_data: _schemas.CreateQuestion, question: _models.Question, db: "Session"):
    question.question_text = question_data.question_text
    question.answer_text = question_data.answer_text

    db.commit()
    db.refresh(question)

    return _schemas.Question.from_orm(question)
