FROM python:3.8.6

EXPOSE 8080
ENV PYTHONUNBUFFERED 1
RUN mkdir /DjangoRestApisPostgreSQL
WORKDIR /DjangoRestApisPostgreSQL
ADD . /DjangoRestApisPostgreSQL/

RUN pip install -r requirements.txt

ADD launch.sh launch.sh
ENTRYPOINT [ "sh", "-c", "sh launch.sh" ]