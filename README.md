# mecab-web-api

MeCab Web API

## Requirements

- Docker

## Prerequisites

- Python >= 3.8
- fastapi == 0.63.0
- uvicorn == 0.13.4
- mecab-python3 == 1.0.3
- unidic == 1.0.3

- [MeCab](https://taku910.github.io/mecab)
- [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)
- [unidic-py](https://github.com/polm/unidic-py)

## Usage

```sh
$ cd mecab-web-api
$ docker build -t mecab-web-api .
$ docker run -p 80:80 mecab-web-api
```

When the web api server starts, access it with a browser as follows.

> `http://localhost/mecab/約束のネバーランド?O=wakati`
> ```sh
> $ echo 約束のネバーランド | mecab -Owakati
> ```
> Response:
> `{"status":200,"format-type":"wakati","dictionary":"mecab","result":["約束","の","ネバーランド"]}`

> `http://localhost/mecab/約束のネバーランド?d=unidic&O=wakati`
> ```sh
> $ echo 約束のネバーランド | mecab -Owakati -d dictionary-path-to-unidic
> ```
> Response:
> `{"status":200,"format-type":"wakati","dictionary":"mecab-unidic-neologd","result":["約束","の","ネバー","ランド"]}`

> `http://localhost/mecab/約束のネバーランド?d=ipadic&O=wakati`
> ```sh
> $ echo 約束のネバーランド | mecab -Owakati -d dictionary-path-to-ipadic
> ```
> Response:
> `{"status":200,"format-type":"wakati","dictionary":"mecab-ipadic-neologd","result":["約束のネバーランド"]}`

> `http://localhost/mecab/約束のネバーランド`
> ```sh
> $ echo 約束のネバーランド | mecab
> ```
> Response:
> `{"status":200,"format-type":"none","dictionary":"mecab","result":[{"表層形":"約束","品詞":"名詞","品詞細分類1":"サ変接続","品詞細分類2":"*","品詞細分類3":"*","活用型":"*","活用形":"*","原形":"約束","読み":"ヤクソク","発音":"ヤクソク"},{"表層形":"の","品詞":"助詞","品詞細分類1":"連体化","品詞細分類2":"*","品詞細分類3":"*","活用型":"*","活用形":"*","原形":"の","読み":"ノ","発音":"ノ"},{"表層形":"ネバーランド","品詞":"名詞","品詞細分類1":"一般","品詞細分類2":"*","品詞細分類3":"*","活用型":"*","活用形":"*","原形":"*"}]}`

> `http://localhost/mecab/約束のネバーランド?d=ipadic`
> ```sh
> $ echo 約束のネバーランド | mecab -d dictionary-path-to-ipadic
> ```
> Response:
> `{"status":200,"format-type":"none","dictionary":"mecab-ipadic-neologd","result":[{"表層形":"約束のネバーランド","品詞":"名詞","品詞細分類1":"固有名詞","品詞細分類2":"一般","品詞細分類3":"*","活用型":"*","活用形":"*","原形":"約束のネバーランド","読み":"ヤクソクノネバーランド","発音":"ヤクソクノネバーランド"}]}`


## License

&copy; 2021 [Ken Kurosaki](https://github.com/quinpallet).<br>
This project is [MIT](https://github.com/quinpallet/mecab-web-api/blob/master/LICENSE) licensed.
