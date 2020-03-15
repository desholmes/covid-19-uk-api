FROM python:3.7-alpine3.10

WORKDIR /usr/src

COPY covid_19_uk/ ./covid_19_uk
COPY manage.py .
COPY gunicorn.py .
COPY requirements.txt .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "/usr/src/entrypoint.sh"]