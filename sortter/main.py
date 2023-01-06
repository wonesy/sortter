
from fastapi import FastAPI
from loguru import logger

from support_request import SupportRequest
import db


app = FastAPI()


@app.on_event("startup")
async def startup():
    db.connect()


@app.on_event("shutdown")
async def shutdown():
    db.close()


@app.get("/")
async def root():
    return {"author": "Cameron Jones"}


@app.get("/support_request")
async def post_support_request() -> list[SupportRequest]:
    return db.get_support_requests()


@app.post("/support_request")
async def post_support_request(support_request: SupportRequest):
    logger.info(support_request)

    try:
        db.save_support_request(support_request)
        logger.info(f"Sending email to support@homework.fi: {support_request} but i'm not going to actually spend time on this since there are basic smtp libs that can do this and i don't want to set up an smtp server in docker at the moment!")
    except db.SortterDatabaseError:
        logger.info("Email has already been disseminated")
