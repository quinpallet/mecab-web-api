from fastapi import FastAPI, Request
import uvicorn

from mecab import mecab_parser


app = FastAPI()


@app.get("/mecab/{text}")
async def get_mecab(text: str, request: Request):
    fmt, dic, result = mecab_parser(text, request.query_params)
    response = {
        'status': 500 if len(result) == 0 else 200,
        'format-type': fmt,
        'dictionary': dic,
        'result': result
    }

    return response


if __name__ == '__main__':
    # For local test using uvicorn
    uvicorn.run(app=app)
