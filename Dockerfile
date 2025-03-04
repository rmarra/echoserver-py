FROM python:3.13-bullseye

COPY . /app

RUN pip install uvicorn
RUN pip install -r /app/requirements.txt

EXPOSE 8000

WORKDIR /app

CMD ["uvicorn", "echoserver_py.main:app", "--host", "0.0.0.0"] 
