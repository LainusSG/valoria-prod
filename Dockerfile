FROM python:3.10
WORKDIR /code
COPY . /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt