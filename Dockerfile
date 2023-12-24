FROM --platform=linux/amd64 python:3.10.12-slim

WORKDIR /code

# set env variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install zip -y
RUN apt-get install git -y
RUN apt-get install wget
RUN apt-get install unzip

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["tail", "-f", "/dev/null"]