FROM alpine:latest

WORKDIR /app

RUN apk add --update py3-pip

RUN apk add --update pipenv

COPY Pipfile /app/

COPY . /app

ENV FLASK_ENV=development

ENV DATABASE_URL=postgres://name:password@houst:port/blog_api_db

ENV JWT_SECRET_KEY=hhgaghhgsdhdhdd

RUN pipenv shell
RUN pipenv install

CMD ["python3", "run.py"]
