FROM python:3.6

WORKDIR /code

COPY requirements.txt ./
COPY requirements_dev.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_dev.txt