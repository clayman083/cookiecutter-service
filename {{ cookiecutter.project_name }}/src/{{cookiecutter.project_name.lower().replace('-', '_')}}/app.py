import socket
from importlib.metadata import Distribution

from aiohttp import web
from structlog.stdlib import BoundLogger

from {{ cookiecutter.project_name.lower().replace('-', '_') }}.web.handlers import meta
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.web.middlewares.logging import logging_middleware
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.web.middlewares.metrics import metrics_middleware


def init(
    dist: Distribution, logger: BoundLogger, debug: bool = False
) -> web.Application:
    """Create application instance.

    Args:
        dist: Application distribution.
        logger: Bounded application logger.
        debug: Run application in debug mode.

    Return:
        New application instance.
    """
    app = web.Application(
        middlewares=(logging_middleware, metrics_middleware),
        logger=logger,  # type: ignore[arg-type]
    )

    app["hostname"] = socket.gethostname()
    app["distribution"] = dist

    app["debug"] = debug

    app.router.add_routes(routes=meta.routes)

    return app
