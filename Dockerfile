FROM python:3.12.2

WORKDIR /src

ADD src/__main__.py .
ADD src/algorithms.py .

CMD [ "python", "./__main__.py" ]
