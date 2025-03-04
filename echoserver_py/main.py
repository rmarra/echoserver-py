from echoserver_py import services
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
@app.put("/")
@app.post("/")
@app.delete("/")
async def echo(request: Request):
    return await services.echo(request)
