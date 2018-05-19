FROM python:3.6

ADD . /code

WORKDIR /code

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt