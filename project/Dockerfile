FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

ENV FLASK_ENV=development

ENV PORT=5000

ENV JWT_SECRET_KEY=hhgaghhgsdhdhdd

CMD sh startup.sh

# 'upgrade' should be 'init' when installing fresh i believe
# CMD ["python", "manage.py", "db", "init"]
# CMD ["python", "manage.py", "db", "migrate"]
# CMD ["python", "manage.py", "db", "upgrade"]
