FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /dummy_svc
COPY requirements.txt /dummy_svc/
RUN pip install -r requirements.txt
COPY . /dummy_svc/