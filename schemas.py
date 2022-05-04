import datetime as _dt
import pydantic as _pydantic


class _BaseQuestion(_pydantic.BaseModel):
    question_text: str
    answer_text: str

class Question(_BaseQuestion):
    id: int
    datetime_create: _dt.datetime

    class Config:
        orm_mode = True

class Q_questions_num(_pydantic.BaseModel):
    questions_num: int

class CreateQuestion(_BaseQuestion):
    pass