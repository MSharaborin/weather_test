FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /test_family_doctor
COPY . /test_family_doctor/
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
