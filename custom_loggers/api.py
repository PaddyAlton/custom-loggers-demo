# custom_loggers/api.py

import logging
import uvicorn

from fastapi import FastAPI
from custom_loggers import workhorse


logging.basicConfig(format="{levelname}:{name}:{message}", style="{", level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
def startup_event():
    logger.info("Application has started!")


@app.get("/")
def read_root() -> str:
    logger.info("I'll ask the workhorse to do something")
    workhorse.do_something()
    logging.info("Well that went well")
    return "Welcome!"


if __name__ == "__main__":

    uvicorn_error_logger = logging.getLogger("uvicorn.error")
    uvicorn_error_logger.propagate = False
    uvicorn.run(
        app, host="0.0.0.0", port=8000#, log_config=None  # suppress default logger
    )
