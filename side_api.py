import requests


def make_request(question_num: dict):
    response = requests.get("https://jservice.io/api/random", json=question_num)
    return response.json()



import models as _models
for q in make_request({"count": 12}):
    question = {"question_text": q["question"], "answer_text": q['answer']}
    question = _models.Question(question_text=question["question_text"], answer_text=question["answer_text"])
    print(question.question_text)
