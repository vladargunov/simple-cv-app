FROM python:3.9.1

# We copy this file first to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD [ "python", "app.py" ]