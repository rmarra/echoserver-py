from fastapi import Request

async def echo(request: Request):
    body = await request.body() and await request.json()
    data = {
        "method": request.method,
        "schema":  request.url.scheme,
        "host": request.url.hostname,
        "path": request.url.path,
        "query": request.query_params,
        "headers": request.headers,
        "cookies": request.cookies,
        "body": body
    }
    return data
