FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt install libc6-dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/