FROM nginx/unit:1.23.0-python3.9

COPY requirements.txt /fastapi/requirements.txt

RUN pip install -r /fastapi/requirements.txt

COPY config.json /docker-entrypoint.d/config.json

COPY . /fastapi

# For API - MeCab
RUN apt-get update && apt-get upgrade -y

RUN apt-get -q -y install sudo mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 && \
    python -m unidic download && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
    ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y