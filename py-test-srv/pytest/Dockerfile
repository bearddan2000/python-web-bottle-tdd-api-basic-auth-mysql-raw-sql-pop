FROM python:latest

COPY bin/ /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN mkdir -p /app/allure-report

VOLUME [ "/app/allure-report" ]

RUN rm -Rf .pytest_cache

ENV WAIT_VERSION 2.7.2

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD [ "pytest", "-v", "-s", "--alluredir=/app/allure-report" ]
