import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

def register_error_handlers(app: FastAPI):
    
    # 1. Handle HTTP errors from external APIs (like 404, 401)
    @app.exception_handler(httpx.HTTPStatusError)
    async def httpx_status_error_handler(request: Request, exc: httpx.HTTPStatusError):
        try:
            error_details = exc.response.json()
        except ValueError:
            error_details = {"detail": exc.response.text or "Unknown API error occurred."}
            
        return JSONResponse(
            status_code=exc.response.status_code,
            content=error_details
        )

    # 2. Handle connection/timeout errors (when OpenWeatherMap is down)
    @app.exception_handler(httpx.RequestError)
    async def httpx_request_error_handler(request: Request, exc: httpx.RequestError):
        logging.error(f"Network error: {exc}")
        return JSONResponse(
            status_code=503,
            content={"detail": "The weather service is temporarily unavailable. Please try again later."}
        )

    # 3. Handle unexpected Python exceptions (internal bugs)
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logging.exception("An unexpected internal error occurred.")
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred. Please contact support."}
        )
