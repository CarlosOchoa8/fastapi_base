FROM python:3.11.4-slim

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN apt-get update \
    && apt-get clean \
    && apt-get -y install openssh-client libpq-dev curl nano
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV TZ="America/Mexico_City"
ENV NAME asdasd

COPY  . .

#ENTRYPOINT ["python", "-u","./python-api/main.py"]

CMD ["uvicorn", "python-api.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
