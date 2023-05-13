FROM python:3.9.6

WORKDIR /app

EXPOSE 8000

COPY ./requirements.txt /app/requrements.txt

RUN install --no-cash-dir --upgrade -r /app/requerements.txt

COPY . .

CMD ['uvicorn', 'app.lesson_1:app']