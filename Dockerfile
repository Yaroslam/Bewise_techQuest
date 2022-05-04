FROM python:3
COPY requirements.txt .
RUN pip install --user -r requirements.txt
ADD main.py /
ADD database.py /
ADD models.py /
ADD schemas.py /
ADD services.py /
ADD side_api.py /

CMD ["python", "-u", "./test.py"]