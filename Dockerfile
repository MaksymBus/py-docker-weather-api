FROM python:3.13.7-slim
LABEL maintainer="maksbusl@gmail.com"

ENV PYTHOUNBUFFERED 1

WORKDIR ./

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
