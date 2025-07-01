import logging

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def http_errors_handler(request: Request, exc) -> JSONResponse:
    logging.error(f"HTTP error {exc.status_code}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "url": request.url.path,
            "method": request.method,
            "message": exc.detail,
            "headers": exc.headers,
            "client": {
                "host": request.client.host,
                "port": request.client.port
            }
        },
        headers=exc.headers
    )


def register_errors_handler(app: FastAPI) -> None:
    app.exception_handler(StarletteHTTPException)(http_errors_handler)


__all__ = ["register_errors_handler"]
