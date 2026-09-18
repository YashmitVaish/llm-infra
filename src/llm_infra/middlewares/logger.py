import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("api")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()

        response = await call_next(request)

        latency = time.perf_counter() - start_time

        logger.info(
            f"{request.method} : {request.url.path} -> "
            f"{response.status_code} : {latency * 1000:.2f}ms"
        )

        return response
